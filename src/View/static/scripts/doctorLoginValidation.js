
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

function validateDoctorLogin() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const data = { username, password };

    fetch('/validate_doctor_login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if ('success' in data) {
            // Login successful, redirect to another page
            window.location.href = '/templates/index.html';
        } else {
            // Login failed, display an error message or take appropriate action
            console.error('Login failed');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });

    return false;  // Prevent the form from submitting
}

