import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import uuid
import random

class insertDoctorLogin:
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
    
    
    
    def insert_doctor_data(self, data):
        try:

            # Insert the data into the MySQL database table
            data['doctor_id'] = [random.randint(100,999) for _ in range(len(data))]
            data.to_sql(name='doctor_login', con=self.engine, if_exists='append', index=False)
            #data is insert
            #possible update could be show a pop up saying that paitent data is sucessfully added. 

            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    # Data for the new patient
    data = {
    'username': ['DocJohn21', 'DrSarahMD', 'HealingDocMike', 'DrEmilyD', 'RoboDoc'],
    'password': ['password1', 'password2', 'password3', 'password4', 'password5']
    }
    data = pd.DataFrame(data)
    
    inserter = insertDoctorLogin()
    inserter.insert_doctor_data(data)
