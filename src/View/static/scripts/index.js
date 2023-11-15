function redirectToPage(role) {
    if (role === 'patient') {
        window.location.href = "src/View/templates/patient.html";
    } else if (role === 'doctor') {
        window.location.href = 'src/View/templates/doctor.html';
    }
}