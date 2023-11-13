import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import uuid
import random

class DoctorLoginDAO:
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
            data.to_sql(name='DoctorLogin', con=self.engine, if_exists='append', index=False)
            #data is insert
            #possible update could be show a pop up saying that paitent data is sucessfully added. 

            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error: {e}")


    def getquery(self , username):
        query = f"SELECT * FROM DoctorLogin WHERE username = %s"
        self.cursor.execute(query, (username,))
        df = pd.DataFrame(self.cursor.fetchall(), columns=[desc[0] for desc in self.cursor.description])
        #return the df
        print(df)



if __name__ == "__main__":
    # Data for the new patient
    doctors_data = [
    {'DoctorID': 1, 'Username': 'DrSmith', 'Password': 'DrSmithPass1'},
    {'DoctorID': 2, 'Username': 'DrJohnson', 'Password': 'Doctor123#'},
    {'DoctorID': 3, 'Username': 'DrDavis', 'Password': 'SecureDoc$'},
]

# Create a DataFrame from the doctor data
    doctors_df = pd.DataFrame(doctors_data)

# Create a DoctorLoginDAO object
    doctor_login_dao = DoctorLoginDAO()

# Insert the doctor data into the database
    doctor_login_dao.insert_doctor_data(doctors_df) 