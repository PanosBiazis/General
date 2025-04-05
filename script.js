// Initialize Bootstrap modal
$("#myModal").modal();

// Initialize Bootstrap modal with keyboard option disabled
$("#myModal").modal({ keyboard: false });

// Show Bootstrap modal
$("#myModal").modal('show');

// Toggle Bootstrap button state and add a class
$(".btn.danger").button("toggle").addClass("fat");

// Store original Bootstrap button function and create an alias
var bootstrapButton = $.fn.button.noConflict();
$.fn.bootstrapBtn = bootstrapButton;

// Event handler for modal show event
$('#myModal').on('show.bs.modal', function(e) {
    if (!data) {
        e.preventDefault();
    }
});
