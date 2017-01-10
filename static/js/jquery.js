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
    
    
    // layout nav bar
    $(".search-button").hover(function() {
        $(this).parent().siblings("#find-friends-form").children("#submit-find-friends").css("display", "inline");
        $(this).next().css("display", "inline");
    });
    
    $(".top-bar").mouseleave(function() {
        $(this).next().css("display", "none");
    });

    $(".submit-find-friends").click(function () {
        $("#find-friends-form").submit();
    });
    
    
    // chat.html
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
    
    $("#share").click(function() {
        var share = $(this).children().val();
        if (share == "Private Message") {
            $("#only-me").css("display", "block");
        } else {
            $("#only-me").css("display", "none");
        }
    });

    
    // comment_loop.html
     $(".like-button").click(function() {
         console.log("like button pressed");
         $(this).parent().siblings('.like-unlike-form').submit();
     });

    $(".like").hover(function() {
        var likes = $(this).siblings(".like-amount").val();
        if ($(this).parent().siblings(".likes").css("display", "hidden") && likes > 0) {
            $(this).parent().siblings(".likes").css("display", "inline");
        }
    });
    
    $(".reply").click(function () {
        // reveals form to reply to post
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
        alert("Whats with this");
        console.log("replies hidden");
    });
});

