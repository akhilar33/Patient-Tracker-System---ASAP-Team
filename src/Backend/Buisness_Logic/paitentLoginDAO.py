import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import random

class  PatientLoginDAO:
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
            data.to_sql(name='PatientLogin', con=self.engine, if_exists='append', index=False)
            #data is insert
            #possible update could be show a pop up saying that paitent data is sucessfully added. 

            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error: {e}")


    def getquery(self , feild , patientdata):
        query = f"SELECT * FROM PatientLogin WHERE {feild} = %s"
        self.cursor.execute(query, (patientdata,))
        df = pd.DataFrame(self.cursor.fetchall(), columns=[desc[0] for desc in self.cursor.description])
        #return the df
        print(type(df))

    def updated(self, first_name, field_to_update, new_value):
        try: 
            update_query = f"UPDATE PatientLogin SET {field_to_update} = %s WHERE FIRST_Name = %s"
            self.cursor.execute(update_query, (new_value, first_name))
            self.connection.commit()
        except Exception as e:
            return f"Error: {e}"
    def delete(self, firstName):
        try: 
            delete_query = "DELETE FROM PatientLogin WHERE FIRST_Name = %s"
            self.cursor.execute(delete_query, (firstName,))
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        except Exception as e:
            return f"Error: {e}"

        


if __name__ == "__main__":
    # Data for the new patients
    patients_data = [
    { 'Username': 'PatientUser1', 'Password': 'P@ssw0rd1'},
    { 'Username': 'HealthySoul22', 'Password': 'Secure#2023'},
    { 'Username': 'HeartWarrior', 'Password': 'Strong&123'},
    { 'Username': 'SunflowerSmiles', 'Password': 'HappyDay$'},
    { 'Username': 'WellnessSeeker', 'Password': 'Peaceful*1'},
]

# Create a DataFrame from the patient data
    patients_df = pd.DataFrame(patients_data)

# Create a PatientLoginDAO object
    patient_login_dao = PatientLoginDAO()

# Insert the patient data into the database
    patient_login_dao.insert_patient_data(patients_df)


