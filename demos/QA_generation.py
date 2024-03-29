import os
import nltk
import gradio as gr
import torch

from typing import List

from pytorch_lightning import LightningModule
from transformers import MT5ForConditionalGeneration, AutoTokenizer, pipeline


class MT5(LightningModule):
    """
    Google MT5 transformer class.
    """

    def __init__(self, model_name_or_path: str = None):
        """
        Initialize module.

        :param model_name_or_path: model name
        """

        super().__init__()

        # Load model and tokenizer
        self.save_hyperparameters()
        self.model = MT5ForConditionalGeneration.from_pretrained(
            model_name_or_path) if model_name_or_path is not None else None
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path,
                                                       use_fast=True) if model_name_or_path is not None else None

    def forward(self, **inputs):
        """
        Forward inputs.

        :param inputs: dictionary of inputs (input_ids, attention_mask, labels)
        """

        return self.model(**inputs)

    def ae(self, batch: List[str], max_length: int = 512, **kwargs):
        """
        Answer extraction prediction.

        :param batch: list of context
        :param max_length: max length of output
        """

        # Transform inputs
        inputs = [f"extract: {context}" for context in batch]

        # Predict
        outputs = self.predict(inputs=inputs, max_length=max_length, **kwargs)

        return outputs


    def qg(self, batch: List[str] = None, max_length: int = 512, **kwargs):
        """
        Question generation prediction.

        :param batch: batch of context with highlighted elements
        :param max_length: max length of output
        """

        # Transform inputs
        inputs = [f"generate: {context}" for context in batch]

        # Predict
        outputs = self.predict(inputs=inputs, max_length=max_length, **kwargs)

        return outputs


    def qa(self, batch: List[dict], max_length: int = 512, **kwargs):
        """
        Question answering prediction.

        :param batch: batch of dict {question: q, context: c}
        :param max_length: max length of output
        """

        # Transform inputs
        inputs = [f"question: {context['question']}  context: {context['context']}" for context in batch]

        # Predict
        outputs = self.predict(inputs=inputs, max_length=max_length, **kwargs)

        return outputs


    def multitask(self, batch: List[str], max_length: int = 512, **kwargs):
        """
        Answer extraction + question generation + question answering.

        :param batch: list of context
        :param max_length: max length of outputs
        """

        # Build output dict
        dict_batch = {'context': [context for context in batch], 'answers': [], 'questions': [], 'answers_bis': []}

        # Iterate over context
        for context in batch:
            answers = self.ae(batch=[context], max_length=max_length, **kwargs)[0]
            answers = answers.split('<sep>')
            answers = [ans.strip() for ans in answers if ans != ' ']
            dict_batch['answers'].append(answers)
            for_qg = [f"{context.replace(ans, f'<hl> {ans} <hl> ')}" for ans in answers]
            questions = self.qg(batch=for_qg, max_length=max_length, **kwargs)
            dict_batch['questions'].append(questions)
            new_answers = self.qa([{'context': context, 'question': question} for question in questions],
                                  max_length=max_length, **kwargs)
            dict_batch['answers_bis'].append(new_answers)
        return dict_batch

    def predict(self, inputs, max_length, **kwargs):
        """
        Inference processing.

        :param inputs: list of inputs
        :param max_length: max_length of outputs
        """

        # Tokenize inputs
        inputs = self.tokenizer(inputs, max_length=max_length, padding='max_length', truncation=True,
                                return_tensors="pt")

        # Retrieve input_ids and attention_mask
        input_ids = inputs.input_ids.to(self.model.device)
        attention_mask = inputs.attention_mask.to(self.model.device)

        # Predict
        outputs = self.model.generate(input_ids=input_ids, attention_mask=attention_mask, max_length=max_length,
                                      **kwargs)

        # Decode outputs
        predictions = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)

        return predictions


# Load nltk punkt tokenizer
nltk.download('punkt')


with gr.Blocks() as demo:

    with gr.Row():
        with gr.Column():
        # Define input
            context = gr.Textbox(lines=5, label="Context")

        with gr.Column():
            qa = gr.Textbox(lines=5, label="QA pair")

    gen_btn = gr.Button(label="Generate", variant="primary")

    def generate(context):
        model = MT5(model_name_or_path="google/mt5-small")
        qa = model.multitask([context])
        return qa

    gen_btn.click(
        fn=generate,
        inputs=context,
        outputs=qa)

demo.launch(debug=True)