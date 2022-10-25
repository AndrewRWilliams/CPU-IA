<!--- 
https://stackoverflow.com/questions/5379120/get-the-highlighted-selected-text
-->

# Grille d'évaluation
Here is some initial text. 

<script>
  function getSelectionText() {
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
  document.getElementById("sel").value = getSelectionText();
};
</script>

<br>
<textarea id="sel" rows="3" cols="50"></textarea>
<p>Please select some text.</p>
<input value="Some text in a text input">
<br>
<textarea id="sel2" rows="3" cols="50"></textarea>
<input type="search" value="Some text in a search input">
<br>
<input type="tel" value="4872349749823">
<br>
<textarea>Some text in a textarea</textarea>
