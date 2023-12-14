
CREATE TABLE DoctorLogin (
  doctor_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (doctor_id)
);

--
@block 
select * from DoctorLogin