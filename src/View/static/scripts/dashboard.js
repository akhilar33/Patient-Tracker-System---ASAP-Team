function redirectToPage(role) {
  // Check the user's role and redirect accordingly
  if (role === "medical_records") {
    // Redirect to the Medical Records page
    window.location.href = "src/View/templates/medical_records.html";
  } else if (role === "appointment_request") {
    // Redirect to the Appointment Request page
    window.location.href = "src/View/templates/appointment_request.html";
  }
}
