  // FUNCTION O1: Copies "Link Share" Link to Clipboard
function myFunction(id) {
  // Get the text field
  let element = document.getElementById("link" + id);
  console.log(id)
  console.log(element)

  // let text = element.getAttribute("value");
  // console.log(text)

  // Select the text field
  element.select();
  element.setSelectionRange(0, 99999); // For mobile devices

   // Copy the text inside the text field
  navigator.clipboard.writeText(element.value);

  // Alert the copied text
  alert("Copied the text: " + element.value);
}

// FUNCTION 02: Still Under Development Message
function message() { 
  alert("Under Construction!");
}
