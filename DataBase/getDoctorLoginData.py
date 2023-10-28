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


       
    
    def getquery(self , username):
        query = f"SELECT * FROM doctor_login WHERE username = %s"
        self.cursor.execute(query, (username,))
        df = pd.DataFrame(self.cursor.fetchall(), columns=[desc[0] for desc in self.cursor.description])
        #return the df
        print(df)




if __name__ == "__main__":
    # Data for the new patient
    query = GetPaitentData()
    query.getquery('RoboDoc')
 