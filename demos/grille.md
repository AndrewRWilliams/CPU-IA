<!--- 
https://stackoverflow.com/questions/5379120/get-the-highlighted-selected-text
-->

# Grille d'évaluation
Here is some initial text. 

<script>
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
