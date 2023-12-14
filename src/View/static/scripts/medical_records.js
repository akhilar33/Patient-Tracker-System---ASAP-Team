// called.js

function fetchMedicalRecords() {
  // Make a fetch request to the server endpoint for medical records
  fetch("/dashboard/medical_records")
    .then((response) => response.json())
    .then((data) => {
      // Get the table body element
      const tableBody = document.getElementById("medical-table-body");
      // Clear existing rows in the table
      tableBody.innerHTML = ""; // Clear existing rows

      // Iterate through each medical record in the data
      data.forEach((record) => {
        // Create a new table row for each record
        const row = document.createElement("tr");
        // Create cells for Date of Visit, Medical Condition, and Medication Prescribed
        const dateCell = document.createElement("td");
        dateCell.textContent = record["Date_of_Visit"];
        row.appendChild(dateCell);

        const conditionCell = document.createElement("td");
        conditionCell.textContent = record["Medical_Condition"];
        row.appendChild(conditionCell);

        const medicationCell = document.createElement("td");
        medicationCell.textContent = record["Medication_Prescribed"];
        row.appendChild(medicationCell);
        // Append the row to the table body
        tableBody.appendChild(row);
      });
    })
    .catch((error) => console.error("Error fetching medical records:", error));
}

// Call fetchMedicalRecords on page load or as needed
document.addEventListener("DOMContentLoaded", function () {
  fetchMedicalRecords();
});
