function getHelp() {

  var code = document.getElementById("code").value;
  var help = document.getElementById("code-help");

  $.ajax({
    type: "POST",
    url: "/get_help",
    data: JSON.stringify(code),
    contentType: "application/json",
    dataType: 'json',
    success: function(result) {
      help.srcdoc = result; 
   } 
 });
}
