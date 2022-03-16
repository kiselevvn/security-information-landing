

$(document).ready(function () {

  $('a[href^="#"]').click(function () {
    let anchor = $(this).attr('href');
    $('html, body').animate({
      scrollTop: $(anchor).offset().top
    }, 600);
  });

  var currentLocation = window.location;
  if (currentLocation.hash !== "") {
    $('html, body').animate({
      scrollTop: $(currentLocation.hash).offset().top
    }, 600);
  }

});
