function redirectToPage(role) {
    if (role === 'medical_records') {
        window.location.href = "src/View/templates/medical_records.html";
    } else if (role === 'appointment_request') {
        window.location.href = 'src/View/templates/appointment_request.html';
    }
}