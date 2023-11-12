-- Create the PatientTable
CREATE TABLE Patient (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Mobile VARCHAR(15) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Age INT,
    Gender VARCHAR(10),
    BloodGroup VARCHAR(10),
    DoctorID INT,
    FOREIGN KEY (DoctorID) REFERENCES DoctorLogin(DoctorID)
);
--
@block 
select * from patient

--
@block 
SELECT PatientID FROM Patient WHERE FirstName = "John" AND LastName = "Doe"

--
@block



