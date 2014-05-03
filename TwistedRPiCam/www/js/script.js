$(function(){
  url = "cam.jpeg?";
  $("#cam").attr("src", url);
  function cam() {
    sec = new Date().getTime();
    $("#cam").attr("src", url+sec);
  };
  setInterval(cam, 500);
})
