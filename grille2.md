#Grille 2

<script>
  function onMouseUp(e) {
    const activeTextarea = document.activeElement;
    const selection = activeTextarea.value.substring(
      activeTextarea.selectionStart, activeTextarea.selectionEnd
    );

    const outputElement = document.getElementById('output-element');
    const outputText = document.getElementById('output-text');
    outputElement.innerHTML = activeTextarea.id;
    outputText.innerHTML = selection;
  }

  const textarea1 = document.getElementById('ta-example-one');
  const textarea2 = document.getElementById('ta-example-two');
  textarea1.addEventListener('mouseup', onMouseUp, false);
  textarea2.addEventListener('mouseup', onMouseUp, false);
</script>

<p>Select some text from one of the text areas below:</p>

<form>
  <textarea name="ta-example-one" id="ta-example-one" rows="7" cols="40">
This is Text Area One. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tincidunt, lorem a porttitor molestie, odio nibh iaculis libero, et accumsan nunc orci eu dui.</textarea
  >
  <textarea name="ta-example-two" id="ta-example-two" rows="7" cols="40">
This is Text Area Two. Fusce ullamcorper, nisl ac porttitor adipiscing, urna orci egestas libero, ut accumsan orci lacus laoreet diam. Morbi sed euismod diam.</textarea
  >
</form>

<p>Active element ID: <em id="output-element"></em></p>
<p>Selected text: <em id="output-text"></em></p>

  
