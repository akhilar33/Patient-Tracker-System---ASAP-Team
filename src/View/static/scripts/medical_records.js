// called.js

function fetchMedicalRecords() {
    fetch('/dashboard/medical_records')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('medical-table-body');
            tableBody.innerHTML = ''; // Clear existing rows

            data.forEach(record => {
                const row = document.createElement('tr');

                const dateCell = document.createElement('td');
                dateCell.textContent = record['Date_of_Visit'];
                row.appendChild(dateCell);

                const conditionCell = document.createElement('td');
                conditionCell.textContent = record['Medical_Condition'];
                row.appendChild(conditionCell);

                const medicationCell = document.createElement('td');
                medicationCell.textContent = record['Medication_Prescribed'];
                row.appendChild(medicationCell);

                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching medical records:', error));
}

// Call fetchMedicalRecords on page load or as needed
document.addEventListener('DOMContentLoaded', function () {
    fetchMedicalRecords();
});
