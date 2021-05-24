$(document).on("submit", "#post-form", function (e) {
  e.preventDefault();

  $.ajax({
    type: "POST",
    url: "/trans",
    data: {
      text: $("#entering_text").val(),
      src1: $("#lang_enter").val(),
      dest1: $("#lang_exit").val(),
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
    },
    success: function(data) {
      $('#exit_text').html(data);
    },
  });
});


function Clear() {
  document.getElementById("entering_text").value = "";
}

function Copy() {
  var copyText = document.getElementById("exit_text");
  copyText.select();
  document.execCommand("copy");
}

function Change() {
  var src = document.getElementById("lang_enter").value;
  document.getElementById("lang_enter").value = document.getElementById("lang_exit").value;
  document.getElementById("lang_exit").value = src;

  // var text = document.getElementById("lang_enter").text;
  
  // console.log(document.getElementById("lang_enter").value);
  // console.log(document.getElementById("lang_exit").value);
}
