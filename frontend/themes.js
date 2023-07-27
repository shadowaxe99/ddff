$(document).ready(function() {
    // Array of themes
    var themes = ["default", "dark", "light", "colorful"];

    // Function to change theme
    function changeTheme(theme) {
        $("#theme-link").attr("href", "css/" + theme + ".css");
    }

    // Event listener for theme selection
    $(".theme-option").click(function() {
        var theme = $(this).attr("data-theme");
        changeTheme(theme);
    });

    // Set the initial theme
    changeTheme(themes[0]);
});