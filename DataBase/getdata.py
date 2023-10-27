import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

class GetPaitentData:
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
    
    def getquery(self , feild , patientdata):
        query = f"SELECT * FROM patient WHERE {feild} = %s"
        self.cursor.execute(query, (patientdata,))
        df = pd.DataFrame(self.cursor.fetchall(), columns=[desc[0] for desc in self.cursor.description])
        print(df)



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
    query = GetPaitentData()
    query.getquery('Last_Name', 'Reddy')
 