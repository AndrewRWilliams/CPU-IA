<!--- 
https://stackoverflow.com/questions/5379120/get-the-highlighted-selected-text
-->

# Grille d'évaluation
Here is some initial text. 

<script>
  // Current functionality: any selected texts gets put in the same box
  // desired functionality: selected text in a specific textarea gets put in its respective box
  function getSelectionText(input_id) {
    var text = "";
    var activeEl = document.activeElement;
    var activeElTagName = activeEl ? activeEl.tagName.toLowerCase() : null;
    if (
      (activeElTagName == "textarea") || (activeElTagName == "input" &&
      /^(?:text|search|password|tel|url)$/i.test(activeEl.type)) &&
      (typeof activeEl.selectionStart == "number")
    ) {
        text = activeEl.value.slice(activeEl.selectionStart, activeEl.selectionEnd);
    } else if (window.getSelection) {
        text = window.getSelection().toString();
    }
    return text;
  }

document.onmouseup = document.onkeyup = document.onselectionchange = function() {
  var activeE1 = document.activeElement;
//  var activeElId = activeEl.id;
//  var prefix = "sel_";
//  var inputElement = prefix.concat(activeElId);
//  document.getElementById("debug").value = activeEl.id;
  document.getElementById("sel_text").value = getSelectionText();
};

// write a function that takes the id of the input box and the id of the output box as arguments and then does the following: takes the selected text from the output box and puts it in the output box.
</script>
<!--- 
how to use
selection box has an id e.g. "text"
associated output box must have id that is "sel_" concat with id, e.g. "sel_text"
-->
<br>
<textarea id="sel_text" rows="3" cols="50"></textarea>
<p>Please select some text.</p>
<textarea id="text" value="Some text in a text input"></textarea>
