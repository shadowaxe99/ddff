$(document).ready(function() {
    function checkWidth() {
        var windowSize = $(window).width();

        if (windowSize <= 768) {
            $('body').addClass('mobile');
            $('body').removeClass('desktop');
        } 
        else {
            $('body').addClass('desktop');
            $('body').removeClass('mobile');
        }
    }

    // Execute on load
    checkWidth();

    // Bind event listener
    $(window).resize(checkWidth);
});