$(document).ready(function() {
    // Hide Text
    $("#hideBtn").click(function() {
        $("#intro").hide();
    });

    // Show Text
    $("#showBtn").click(function() {
        $("#intro").show();
    });

    // Toggle Text
    $("#toggleBtn").click(function() {
        $("#intro").toggle();
    });

    // Change Color on Click
    $("#colorBtn").click(function() {
        $("#box").css("background-color", "blue");
    });

    // Fade In Effect
    $("#fadeInBtn").click(function() {
        $("#box").fadeIn();
    });

    // Fade Out Effect
    $("#fadeOutBtn").click(function() {
        $("#box").fadeOut();
    });
});
