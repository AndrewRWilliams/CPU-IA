# Grille de correction

<style>
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.switch input { 
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>

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

function toggleEditing() {
    var textareas = document.getElementsByTagName("*");
    for (var i = 0; i < textareas.length; i++) {
        if (textareas[i].readOnly == "true") {
            textareas[i].readOnly = "false";
        } else {
            textareas[i].readOnly = "true";
        }
    }
}

// write a function that changes the value of the critere1 textarea to a "test change".
function testChange() {
    var textareas = document.getElementsByTagName("*");
    for (var i = 0; i < textareas.length; i++) {
        if (textareas[i].id == "retroaction") {
          // get the text from textareas sel_critere1, sel_critere2, sel_critere3
          // concatenate the text from the textareas with commas between them and put it in the textarea retroaction 
          textareas[i].value = 'Critère 1.1 : \n\nVous avez fait un excellent travail avec ce critère. Continuez à faire du bon travail !\n\nCritère 2.2 : \n\nVous avez fait un travail moyen pour ce critère. Continuez à travailler et vous allez vous améliorer !\n\nCritère 3.3 : \n\nVous avez fait un travail médiocre pour ce critère. Vous devez travailler dur pour vous améliorer.';
        } 
    }
}

// write a function that clears the value of a textarea. The input of the function should be the id of the textarea.
function clearTextarea(id) {
    document.getElementById(id).value = "";
}


// write a function that sends a POST request to the server with the data from the textarea retroaction


</script>

<!-- <br><textarea id="sel_textid" rows="3" cols="50"></textarea> -->
<!-- <textarea id="textid" value="Some text in a text input"></textarea>
<br> -->



<textarea id="critere1" cols=10 rows=5>Critère 1.</textarea> <textarea id="critere1_excel" cols=25 rows=5>Critère 1.1 est excellent. Critère 1.2 est excellent. Critère 1.3 est excellent.</textarea> <textarea id="critere1_moyen" cols=25 rows=5>Critère 1.1 est moyen. Critère 1.2 est moyen. Critère 1.3 est moyen. </textarea> <textarea id="critere1_poche" cols=25 rows=5>Critère 1.1 est poche. Critère 1.2 est poche. Critère 1.3 est poche.</textarea>

<br>

<textarea id="critere2" cols=10 rows=5>Critère 2.</textarea> <textarea id="critere2_excel" cols=25 rows=5>Critère 2.1 est excellent. Critère 2.2 est excellent. Critère 2.3 est excellent.</textarea> <textarea id="critere2_moyen" cols=25 rows=5>Critère 2.1 est moyen. Critère 2.2 est moyen. Critère 2.3 est moyen. </textarea> <textarea id="critere2_poche" cols=25 rows=5>Critère 2.1 est poche. Critère 2.2 est poche. Critère 2.3 est poche. </textarea>

<br>

<textarea id="critere3" cols=10 rows=5> Critère 3.</textarea> <textarea id="critere3_excel" cols=25 rows=5>Critère 3.1 est excellent. Critère 3.2 est excellent. Critère 3.3 est excellent.</textarea> <textarea id="critere3_moyen" cols=25 rows=5>Critère 3.1 est moyen. Critère 3.2 est moyen. Critère 3.3 est moyen. </textarea> <textarea id="critere3_poche" cols=25 rows=5>Critère 3.1 est poche. Critère 3.2 est poche. Critère 3.3 est poche. </textarea>

<!--<label class="switch">
  <input type="checkbox" checked onclick="toggleEditing()">
  <span class="slider round"></span>
</label>
-->

<br>
<h2>Les extraits.</h2>
<br><textarea id="sel_critere1" cols=90>L'extrait du critère 1.</textarea> <button onclick="clearTextarea('sel_critere1')">Effacer</button>
<br><textarea id="sel_critere2" cols=90>L'extrait du critère 2.</textarea> <button onclick="clearTextarea('sel_critere2')">Effacer</button>
<br><textarea id="sel_critere3" cols=90>L'extrait du critère 3.</textarea> <button onclick="clearTextarea('sel_critere3')">Effacer</button>

<br>
<h2>La rétroaction.</h2>
<br><textarea id="retroaction" cols=90 rows=20></textarea> 


<button onclick="testChange()">Générer la rétroaction.</button>

<h2>Les trois questions de Hattie.</h2>

<h3> Òu vais-je? (but final) </h3>
<h3> Òu suis-je? (évaluation présente) </h3>
<h3> Òu aller maintenant? (prochaines étapes) </h3>

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