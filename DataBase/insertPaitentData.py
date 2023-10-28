import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import random

class PatientDataInserter:
    def __init__(self):
        self.connection = mysql.connector.connect(
             host = "localhost",
            user= "root",
            password= "password",
            database = 'Patient',
            auth_plugin='mysql_native_password'
        )
        print("Connection established")
        self.cursor = self.connection.cursor()
        hostname= "localhost"
        database= "Patient"
        username= "root"
        password= "password"

        self.engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=database, user=username, pw=password))
    

    
    
    def insert_patient_data(self, data):
        try:
            print(type(data))

            # Insert the data into the MySQL database table
            data['patient_id'] = [random.randint(1000,9999) for _ in range(len(data))]
            data.to_sql(name='patient', con=self.engine, if_exists='append', index=False)
            #data is insert
            #possible update could be show a pop up saying that paitent data is sucessfully added. 

            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    # Data for the new patient
    data = pd.DataFrame({
        'FIRST_Name': ["Akhila", "John", "Alice", "Sarah", "Michael", "Emily", "David", "Olivia", "William"],
        'Last_Name': ["Reddy", "Doe", "Smith", "Johnson", "Brown", "Davis", "Wilson", "Anderson", "Miller"],
        'Email': ["akhilareddyd@umass.edu", "johndoe@example.com", "alicesmith@example.com", "sarah@example.com", "michael@example.com", "emily@example.com", "david@example.com", "olivia@example.com", "william@example.com"],
        'Mobile': ["4139494787", "5551234567", "5559876543", "5551112222", "5553334444", "5555555555", "5556667777", "5557778888", "5558889999"],
        'DOB': ['2023-10-25', '2023-09-15', '2023-08-05', '2023-07-20', '2023-06-10', '2023-05-15', '2023-04-08', '2023-03-12', '2023-02-01'],
        'Blood_group': ["B+", "A-", "O+", "AB+", "A+", "O-", "B-", "AB-", "A+"],
        'Gender': ["Female", "Male", "Female", "Female", "Male", "Female", "Male", "Female", "Male"],
        'doctor': ["Dr. Smith", "Dr. Johnson", "Dr. Brown", "Dr. Davis", "Dr. Wilson", "Dr. Anderson", "Dr. Miller", "Dr. Harris", "Dr. Lee"]
    })

    inserter = PatientDataInserter()
    inserter.insert_patient_data(data)
