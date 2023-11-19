document.addEventListener('DOMContentLoaded', function () {
    const addMedicalRecordsBtn = document.getElementById('addMedicalRecordsBtn');

    if (addMedicalRecordsBtn) {
        addMedicalRecordsBtn.addEventListener('click', function () {
            // Retrieve the patient_id from the button's data attribute
            const patientIdElement = document.getElementById('patientId');
            const patientId = patientIdElement.innerText.split(': ')[1].trim();
            // Redirect to the addMedicalRecords endpoint with the patient_id
            window.location.href = `/doctorDashboard/addMedicalRecords?patient_id=${patientId}`;
        });
    }
});