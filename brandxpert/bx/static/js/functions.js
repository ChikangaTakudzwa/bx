jQuery(document).ready(function () {
  $(window).scroll(function () {
    $(".topnav").toggleClass(
      "bg-white navbar-light shadow-sm scrollednav py-0",
      $(this).scrollTop() > 50
    );
  });

  $("#modal_newsletter").on("show.bs.modal", function () {
    $(".downloadzip")[0].click();
  });
});

$(document).ready(function () {
  $("#back-to-top").click(function () {
    $("html, body").animate({ scrollTop: 0 }, "slow");
    return false;
  });
});

$(window).scroll(function () {
  if ($(this).scrollTop() > 100) {
    $("#back-to-top").fadeIn();
  } else {
    $("#back-to-top").fadeOut();
  }
});

// $('#mymodal').on('show.bs.modal', function () {
//   $.ajax({
//       url: "{% url 'portfolio' %}",
//       success: function (data) {
//           // Handle the response from the view function
//       }
//   });
// });
