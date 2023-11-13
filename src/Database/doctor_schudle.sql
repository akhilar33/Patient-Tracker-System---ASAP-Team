CREATE TABLE DoctorLogin (
    DoctorID INT NOT NULL AUTO_INCREMENT,
    Username VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    PRIMARY KEY (DoctorID)
);

--
@block 
Select * from PatientLogin