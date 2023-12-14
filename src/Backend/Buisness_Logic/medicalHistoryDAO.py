import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import random

class  medicalHistoryDAO:
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

    def insert_medical_data(self, data):
        try:

            print(type(data))


            # Insert the data into the MySQL database table
            data.to_sql(name='medical_history', con=self.engine, if_exists='append', index=False)
            #data is insert
            #possible update could be show a pop up saying that paitent data is sucessfully added. 

            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error: {e}")


    def getMedicalData(self , paitentID):

        query = f"SELECT * FROM medical_history WHERE PatientID = %s "
        self.cursor.execute(query, (paitentID,))
        df = pd.DataFrame(self.cursor.fetchall(), columns=[desc[0] for desc in self.cursor.description])
        return df



        


# if __name__ == "__main__":
#     # Data for medical history
# #    #medical_data = {
# #         'Patient_ID': [1, 2, 3, 4, 5, 6, 7],  # Use the appropriate patient IDs
# #         'Date_of_Visit': ['2023-10-01', '2023-10-15', '2023-10-05', '2023-10-12', '2023-10-20', '2023-10-08', '2023-10-25'],
# #         'Medical_Condition': ['Fever', 'Headache', 'Injury', 'Cold', 'Flu', 'Allergy', 'Asthma'],
# #         'Medication_Prescribed': ['Paracetamol', 'Aspirin', 'Bandage', 'Cough Syrup', 'Antiviral', 'Antihistamine', 'Inhaler']
# #     }
# #     #medical_data = pd.DataFrame(medical_data)



#     # print(inserter.getMedicalData(6))

#     # print(inserter.getMedicalData(1))
#     obj = medicalHistoryDAO()

