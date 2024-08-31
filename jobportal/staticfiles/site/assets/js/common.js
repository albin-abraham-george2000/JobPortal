$(document).ready(function () {
  $(function () {
    $("#header").load("header.html");
    $("#footer").load("footer.html");
  });

  // Configure/customize these variables.
  var showChar = 200; // How many characters are shown by default
  var texts = "........";
  var readtext = "Read More";
  var readlesstext = "Read Less";

  $(".readmores").each(function () {
    var content = $(this).html();

    if (content.length > showChar) {
      var c = content.substr(0, showChar);
      var h = content.substr(showChar, content.length - showChar);

      var html =
        c +
        '<span class="readellipses">' +
        texts +
        '&nbsp;</span><span class="readcontent"><span>' +
        h +
        '</span>&nbsp;&nbsp;<a href="" class="readmorelink">' +
        readtext +
        "</a></span>";

      $(this).html(html);
    }
  });

  $(".readmorelink").click(function () {
    if ($(this).hasClass("readless")) {
      $(this).removeClass("readless");
      $(this).html(readtext);
    } else {
      $(this).addClass("readless");
      $(this).html(readlesstext);
    }
    $(this).parent().prev().slideToggle();
    $(this).prev().slideToggle();
    return false;
  });
});

$(document).ready(function () {
  // Add up icon for collapse element which is open by default
  $(".collapse.show").each(function () {
    $(this)
      .prev(".accordion-header")
      .find(".fa")
      .addClass("fa-angle-down")
      .removeClass("fa-angel-up");
  });
  // Toggle down minus icon on show hide of collapse element
  $(".collapse")
    .on("show.bs.collapse", function () {
      $(this)
        .prev(".accordion-header")
        .find(".fa")
        .removeClass("fa-angle-down")
        .addClass("fa-angle-up");
    })
    .on("hide.bs.collapse", function () {
      $(this)
        .prev(".accordion-header")
        .find(".fa")
        .removeClass("fa-angle-up")
        .addClass("fa-angle-down");
    });
});
