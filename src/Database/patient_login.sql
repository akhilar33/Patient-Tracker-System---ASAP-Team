CREATE TABLE patient_login (
    PatientID INT,
    username VARCHAR(255) NOT NULL ,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (PatientID),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
);



--
@block
select * from patient_login



--
@block
drop table patient_login
=======
--
@block
DELETE FROM patient_login WHERE username = 'arijain';

