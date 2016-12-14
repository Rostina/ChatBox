/**
 * Created by yosef on 12/13/2016.
 */
$(document).ready(function () {
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

    $(function () {
        // shows images
        var image;
        $(".image-link").click(function (event) {
            event.preventDefault();
            var pk = $(this).next(type = "hidden");
            if ($(this).next().hasClass("image-link") === true) {
                // meaning X button was pressed
                $(this).css("display", "none");
                image = $(this).siblings('.image-field').children('.image').detach();
                if (image) {
                }
                // $(this).siblings('.hidden-items').css("display", "none");
                $(this).siblings("#image-button").css("display", "inline");
            } else {
                // meaning camera button was pressed
                if (image) {
                    image.appendTo($(this).siblings(".image-field"));
                    image = null;
                } else {

                    $(this).siblings(".image-field").append("<input type='file' name='image' id='image' placeholder='image' class='image' />");
                }
                $(this).siblings('.hidden-items').css("display", "inline");
                $(this).next(type = "hidden").submit();
                $(this).css("display", "none")
            }


        });
    });

    $(".reply").click(function () {
        $(this).parents().siblings(".comment-form").css("display", "inline");
        $(this).hide();
        console.log("Reply form revealed");
    });

    $(".show_replies").click(function () {
        var comment = $(this).next().val();
        $(this).next().css("display", "block");
        $(this).css("display", "none");
        console.log("Went through");
    });

    $(".hide-replies").click(function () {
        $(this).parent().css("display", "none");
        $(this).parent().prev().css("display", "block");
        console.log("replies hidden");
    });

});

