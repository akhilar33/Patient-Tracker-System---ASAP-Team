import mysql.connector 
import pandas as pd
from sqlalchemy import create_engine


data = {
    'FIRST_Name': ['NewPatient'],
    'Last_Name': ['LastName'],
    'Email': ['newpatient@example.com'],
    'Mobile': ['1234567890'],
    'DOB': ['2000-01-15'],
    'Blood_group': ['O+'],
    'Gender': ['Male'],
    'doctor': ['Dr. New']
}

new_patient_df = pd.DataFrame(data)
print(new_patient_df)

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database = 'Patient'
    )
    print("Connection established")
    cursor = mydb.cursor()

except mysql.connector.Error as err:
    print("An error occurred:", err)

hostname= "localhost"
database= "Patient"
username= "root"
password= "password"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=database, user=username, pw=password))

new_patient_df.to_sql(name='patient', con=engine, if_exists='append', index=False)
