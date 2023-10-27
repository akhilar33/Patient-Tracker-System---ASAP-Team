import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

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

            # Insert the data into the MySQL database table
            data.to_sql(name='patient', con=self.engine, if_exists='append', index=False)

            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    # Data for the new patient
    new_patient_data = {
        'FIRST_Name': ['Akhilas'],
        'Last_Name': ['Reddys'],
        'Email': ['newpatient@.com'],
        'Mobile': ['4139494787'],
        'DOB': ['2000-01-15'],
        'Blood_group': ['O+'],
        'Gender': ['Male'],
        'doctor': ['Dr. New']
    }
    df = pd.DataFrame(new_patient_data)
    inserter = PatientDataInserter()
    inserter.insert_patient_data(df)
