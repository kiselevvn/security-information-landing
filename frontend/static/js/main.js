$('a[href^="#"]').click(function(){
  let anchor = $(this).attr('href');
  $('html, body').animate({
    scrollTop:  $(anchor).offset().top
  }, 600);
});




$(document).ready(function () {
  var currentLocation = window.location;
  if (currentLocation.hash !== "") {
    $('html, body').animate({
      scrollTop: $(currentLocation.hash).offset().top
    }, 600);
  }
  console.log(currentLocation);
});
