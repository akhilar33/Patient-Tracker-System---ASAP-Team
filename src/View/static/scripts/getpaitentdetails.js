// view_patient_records.js

function getPatientRecords() {
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const mobileNumber = document.getElementById('mobileNumber').value;
    var url = '/doctorDashboard/view_Paitent_Records/getPaitentRecords';

    // Use fetch or another method to send the data to the server
    fetch(url + `?firstName=${firstName}&lastName=${lastName}&mobileNumber=${mobileNumber}`)
    .then(response => {
        if (!response.ok) {
            throw new Error(`Patient not found: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        // Redirect to medical_data.html with the received data
        window.location.href = `/doctorDashboard/view_Paitent_Records/viewRecords?data=${JSON.stringify(data)}`;
    })
    .catch(error => {
        // Handle errors and redirect to a page to add a patient
        console.error('Error:', error);
        window.location.href = '/doctorDashboard/addPatient';
    });
}

