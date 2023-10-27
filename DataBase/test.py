import sys
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password= "password",
    database = 'Patient',auth_plugin='mysql_native_password'
   
    
)
cursor = db.cursor()
patient_data = {
    "FIRST_Name": "cute ",
    "Last_Name": "tttgfgf",
    "Email": "johndoe@example.com",
    "Mobile": "1234567890",
    "DOB": "1990-01-15",
    "Blood_group": "A+",
    "Gender": "Male",
    "doctor": "Dr. Smith"
}

# SQL query to insert data into the "patient" table
insert_query = """
INSERT INTO patient (FIRST_Name, Last_Name, Email, Mobile, DOB, Blood_group, Gender, doctor)
VALUES (%(FIRST_Name)s, %(Last_Name)s, %(Email)s, %(Mobile)s, %(DOB)s, %(Blood_group)s, %(Gender)s, %(doctor)s)
"""
cursor.execute(insert_query , patient_data) 
db.commit()

