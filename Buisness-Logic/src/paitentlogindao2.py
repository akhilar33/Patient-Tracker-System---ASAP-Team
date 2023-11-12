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
            first_name = data['FirstName']
            last_name = data['LastName']
            query = "SELECT PatientID FROM Patient WHERE FirstName = %s AND LastName = %s"
            self.cursor.execute(query, (first_name[0], last_name[0]))
            patient_id = self.cursor.fetchone()

            if patient_id:
                # Insert the data into the patient_login table
                new_df = pd.DataFrame({'PatientID': patient_id[0] , 'Username': data['Username'],'Password': data['Password'], })
                new_df.to_sql(name='patient_login', con=self.engine, if_exists='append', index=False)
                self.connection.commit()
                print("Data inserted successfully.")
            else:
                print("You need to be a paitent to login to the system")
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
   { 'FirstName' : 'David', 'LastName': 'Leez' ,'Username': 'PatientUser7', 'Password': 'P@ssw0rd7'}
    ]

# Create a DataFrame from the patient data
    patients_df = pd.DataFrame(patients_data)
    patient_dao = PatientLoginDAO()
    patient_dao.insert_patient_data(patients_df)




