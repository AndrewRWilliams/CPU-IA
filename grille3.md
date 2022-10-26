# Grille 3


<script>

// Modify a function to take as input the id of the input box and the output box and take the selected text from the input box and put it in the output box.

function transferHighlightedText(input_id) {
    var text = "";
    var activeEl = document.activeElement;
    var activeElTagName = activeEl ? activeEl.tagName.toLowerCase() : null;
    if (input_id == activeEl.id) {
        if (window.getSelection) {
        text = window.getSelection().toString();
    }
    return text;
    } else {
        return "error";
    }
    
}

document.onmouseup = function() {
    var inputOutputdict = {"critere1_excel": "sel_critere1", "critere1_moyen": "sel_critere1", "critere1_poche": "sel_critere1", "critere2_excel": "sel_critere2" , "critere2_moyen": "sel_critere2", "critere2_poche": "sel_critere2", "critere3_excel": "sel_critere3", "critere3_moyen": "sel_critere3", "critere3_poche": "sel_critere3"};
    var activeEl = document.activeElement;
    if (activeEl.id in inputOutputdict) {
        // if the output box is not empty, then append the new text to the old text
        var outputBox = document.getElementById(inputOutputdict[activeEl.id]);
        if (outputBox.value == "" || outputBox.value == "L'extrait du critère 1." || outputBox.value == "L'extrait du critère 2." || outputBox.value == "L'extrait du critère 3.") {
            outputBox.value = transferHighlightedText(activeEl.id);
        } else {
            outputBox.value = outputBox.value + " " + transferHighlightedText(activeEl.id);
        }
        var output_id = inputOutputdict[activeEl.id];
        // document.getElementById(output_id).value = transferHighlightedText(activeEl.id);
    } 


};

function id(e) {
  e.currentTarget.style.visibility = 'hidden';
  console.log(e.currentTarget);
  // When this function is used as an event handler: this === e.currentTarget
}

</script>

<!-- <br><textarea id="sel_textid" rows="3" cols="50"></textarea> -->
<!-- <textarea id="textid" value="Some text in a text input"></textarea>
<br> -->
<p>Critère 1.</p>

<textarea id="critere1">Critère 1.</textarea> <textarea id="critere1_excel">Critère 1 est excellent.</textarea> <textarea id="critere1_moyen">Critère 1 est moyen.</textarea> <textarea id="critere1_poche">Critère 1 est poche.</textarea>

<textarea id="critere2">Critère 2.</textarea> <textarea id="critere2_excel">Critère 2 est excellent.</textarea> <textarea id="critere2_moyen">Critère 2 est moyen.</textarea> <textarea id="critere2_poche">Critère 2 est poche.</textarea>

<textarea id="critere3">Critère 3.</textarea> <textarea id="critere3_excel">Critère 3 est excellent.</textarea> <textarea id="critere3_moyen">Critère 3 est moyen.</textarea> <textarea id="critere3_poche">Critère 3 est poche.</textarea>

<br>
<p>Les extraits.</p>
<br><textarea id="sel_critere1" cols=90>L'extrait du critère 1.</textarea>
<br><textarea id="sel_critere2" cols=90>L'extrait du critère 2.</textarea>
<br><textarea id="sel_critere3" cols=90>L'extrait du critère 3.</textarea> 

<p>Le texte final.</p>
<br><textarea id="retroaction"></textarea> 

<!-- <table>
<thead>
  <tr>
    <th class="tg-0pky">Critère</th>
    <th class="tg-0pky">Excellent</th>
    <th class="tg-0pky">Moyen</th>
    <th class="tg-0pky">Poche</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Critère 1<br></td>
    <td class="tg-0pky" id="excellent1"><textarea id="textid"></textarea></td>
    <td class="tg-0pky" id="moyen1">Le critère 1 est moyen.</td>
    <td class="tg-0pky" id="poche1">Le critère 1 est poche.</td>
  </tr>
  <tr>
    <td class="tg-0pky">Critère 2</td>
    <td class="tg-0pky" id="excellent2">Le critère 2 est excellent.</td>
    <td class="tg-0pky" id="moyen2">Le critère 2 est moyen.</td>
    <td class="tg-0pky" id="poche2">Le critère 2 est poche.</td>
  </tr>
  <tr>
    <td class="tg-0pky">Critère 3</td>
    <td class="tg-0pky" id="excellent3">Le critère 3 est excellent.</td>
    <td class="tg-0pky" id="moyen3">Le critère 3 est moyen.</td>
    <td class="tg-0pky" id="poche3">Le critère 3 est poche.</td>
  </tr>
</tbody>
</table> -->