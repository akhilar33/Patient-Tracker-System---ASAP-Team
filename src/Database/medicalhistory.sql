-- Create the MedicalHistory table
CREATE TABLE medical_history (
    reco_id INT NOT NULL AUTO_INCREMENT,
    PatientID INT NOT NULL,
    Date_of_Visit DATE NOT NULL,
    Medical_Condition TEXT,
    Medication_Prescribed TEXT,
    PRIMARY KEY (reco_id),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
);

--
@block
select * from  medical_history
-- 
@block
INSERT INTO medical_history (PatientID, Date_of_Visit, Medical_Condition, Medication_Prescribed)
VALUES
    (1, '2023-04-10', 'Fever and cough', 'Prescribed antibiotics.'),
    (1, '2023-08-20', 'Sprained ankle', 'Recommended rest and pain relievers.'),
    (2, '2023-03-15', 'Headache and fatigue', 'Prescribed pain relievers and rest.'),
    (2, '2023-07-05', 'Allergies', 'Prescribed antihistamines.'),
    (3, '2023-02-28', 'High blood pressure', 'Prescribed medication and dietary changes.'),
    (3, '2023-09-12', 'Flu', 'Recommended rest and hydration.'),
    (4, '2023-06-18', 'Stomach ache', 'Prescribed antacids and dietary changes.'),
    (4, '2023-10-02', 'Sinus infection', 'Prescribed antibiotics and nasal spray.'),
    (5, '2023-05-07', 'Back pain', 'Prescribed pain relievers and physical therapy.'),
    (5, '2023-08-31', 'Common cold', 'Recommended rest and hydration.');
