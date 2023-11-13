import mysql.connector

class Patient:
    def __init__(self):
        self.connection = mysql.connector.connect(
             host = "localhost",
            user= "root",
            password= "password",
            database = 'Patient',
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()

    def insert_patient_details(self, first_name, last_name, email, mobile, dob, blood_group, gender, doctor):
        insert_query = """
        INSERT INTO patient (FIRST_Name, Last_Name, Email, Mobile, DOB, Blood_group, Gender, doctor)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        patient_data = (first_name, last_name, email, mobile, dob, blood_group, gender, doctor)

        self.cursor.execute(insert_query, patient_data)
        self.connection.commit()
        print("Patient details inserted successfully.")

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":

    # Example patient details (replace with actual data from UI)
    first_name = "John"
    last_name = "Doe"
    email = "johndoe@example.com"
    mobile = "1234567890"
    dob = "1990-01-15"
    blood_group = "A+"
    gender = "Male"
    doctor = "Dr. Smith"

    patient_manager = Patient()
    patient_manager.insert_patient_details(first_name, last_name, email, mobile, dob, blood_group, gender, doctor)
    patient_manager.close_connection()
