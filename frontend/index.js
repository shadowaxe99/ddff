$(document).ready(function() {
    // Load dashboard on page load
    $.get("/dashboard", function(data) {
        $("#dashboard").html(data);
    });

    // Event handler for theme selection
    $("#themes").change(function() {
        var theme = $(this).val();
        $("body").attr("class", theme);
    });

    // Event handler for responsive design testing
    $(window).resize(function() {
        if ($(window).width() < 768) {
            $("body").addClass("mobile");
        } else {
            $("body").removeClass("mobile");
        }
    });

    // AJAX calls for content management
    $("#content").on("click", ".edit", function() {
        var postId = $(this).data("id");
        $.get("/content/edit/" + postId, function(data) {
            $("#content").html(data);
        });
    });

    // AJAX calls for writer coordination
    $("#writers").on("click", ".assign", function() {
        var writerId = $(this).data("id");
        $.get("/writers/assign/" + writerId, function(data) {
            $("#writers").html(data);
        });
    });

    // AJAX calls for editorial calendar
    $("#calendar").on("click", ".schedule", function() {
        var postId = $(this).data("id");
        $.get("/calendar/schedule/" + postId, function(data) {
            $("#calendar").html(data);
        });
    });

    // AJAX calls for content analytics
    $("#analytics").on("click", ".view", function() {
        var postId = $(this).data("id");
        $.get("/analytics/view/" + postId, function(data) {
            $("#analytics").html(data);
        });
    });

    // AJAX calls for social media integration
    $("#socialMedia").on("click", ".post", function() {
        var postId = $(this).data("id");
        $.get("/socialMedia/post/" + postId, function(data) {
            $("#socialMedia").html(data);
        });
    });
});