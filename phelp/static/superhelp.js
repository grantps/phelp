function getHelp() {

  var code_content = code_editor.getValue();
  var help = document.getElementById("code-help");

  $.ajax({
    type: "POST",
    url: "/get_help",
    data: JSON.stringify(code_content),
    contentType: "application/json",
    dataType: 'json',
    success: function(result) {
      help.srcdoc = result; 
   } 
 });
}
