function validatePatientLogin() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('patient-password').value;

    const data = { username, password };

    fetch('/validate-patient-login', {
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
            window.location.href = '/templates/index.html';  // Change to the desired page
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
