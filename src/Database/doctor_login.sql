
CREATE TABLE doctor_login (
  doctor_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (doctor_id)
);

--
@block 

SELECT * FROM doctor_login;

SELECT * FROM doctor_login WHERE username = 'DrSmith' ;


--
@block
drop table doctor_login