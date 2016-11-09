/**
 * Created by yosef on 9/27/2016.
 */
$(document).ready(function () {
    $(".sumit-comment").click(function (event) {
        event.preventDefault();
        var formData = {
            image: $(this).siblings("input[type='file']"),
            text: $(this).siblings("input[type='text']")
        };

        $.ajax({
            type: $(this).attr('method'),
            url: "{% url 'chat:chat' %}",
            data: formData,
            success: function (data) {
                alert("Went well");
            },
            error: function (response, error) {
                alert("Need to reload");
            }
        })
    });
});


function showFlashMessage(message) {
    // var template = "{% include 'alert.html' with message='" + message + "' %}";
    var template = "<div class='container container-alert-flash'>" +
        "<div class='col-sm-3 col-sm-offset-8'>" +
        "<div class='alert alert-success alert-dismissible' role='alert'>" +
        "<button type='button' class='close' data-dismiss='alert' aria-label='Close'>" +
        "<span aria-hidden='true'>&times;</span></button>" + message + "</div></div></div>";
    console.log(template);
    $("body").append(template);
    $(".container-alert-flash").fadeIn();
    setTimeout(function () {
        $(".container-alert-flash").fadeOut();
    }, 1800)
}

$(document).ready(function () {
    $(".remove-picture").click(function(event) {
        $(this).css("display", "none");
        event.preventDefault();
        $(this).prev('.image').remove();
        $(this).prev('.image').css("display", "none");
        $(this).siblings(".image-link").css("display", "inline")
    });

    $(".image-link").click(function(event) {
        // make it that when click on image-link it automatically brings up image choice
        // and not show defoult
        event.preventDefault();
        $(this).next().css("display", "inline");
        $(this).css("display", "none");
    });


});