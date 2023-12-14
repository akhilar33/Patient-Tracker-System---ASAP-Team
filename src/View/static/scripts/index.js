function redirectToPage(role) {
  // Check if the user is a patient
  if (role === "patient") {
    // Redirect to the patient page
    window.location.href = "src/View/templates/patient.html";
  } else if (role === "doctor") {
    // Redirect to the doctor page
    window.location.href = "src/View/templates/doctor.html";
  }
}
