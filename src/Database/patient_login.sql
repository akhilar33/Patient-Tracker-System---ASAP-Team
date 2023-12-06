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

<<<<<<< HEAD


--
@block
drop table patient_login
=======
--
@block
DELETE FROM patient_login WHERE username = 'arijain';

=======
--
@block
DELETE FROM patient_login WHERE username = 'arijain';
>>>>>>> 0a1ec2099db0ac425d625f9b070cf3fd4157ff4d
