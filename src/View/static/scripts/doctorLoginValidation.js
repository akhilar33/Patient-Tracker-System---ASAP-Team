$(document).ready(function() {
    $('#doctor_login_form').submit(function(e) {
        e.preventDefault(); // Prevent the form from submitting in the traditional way

        // Collect form data
        var formData = {
            'username': $('#username').val(),
            'password': $('#password').val()
        };

        // Send the AJAX request
        $.ajax({
            type: 'POST',
            url: '/doctor_login',
            data: formData,
            dataType: 'json',
            encode: true,
            success: function(data) {
                // Redirect to the dashboard upon successful login
                window.location.href = data.redirect;
            },
            error: function(error) {
                console.log('Error:', error);
                // Handle the error if needed
            }

        });
    });
});