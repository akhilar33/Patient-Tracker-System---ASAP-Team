import json
import logging
import pandas as pd
from flask import Flask, render_template, redirect, url_for, request, flash
from flask import jsonify,abort
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from Buisness_Logic.paitentlogindao2 import PatientLoginDAO
from Buisness_Logic.DoctorLoginDAO import DoctorLoginDAO
from Buisness_Logic.medicalHistoryDAO import medicalHistoryDAO
from Buisness_Logic.PaitentDAO import PaitentDAO

from flask_session import Session


app = Flask(__name__,
    static_url_path='/static',
    static_folder="../View/static",
    template_folder="../View/templates",
)


app.config['SECRET_KEY'] = 'your_secret_key'
app.config['DEBUG'] = False

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/patient')
def patient():
    return render_template('patient.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/paitent_login', methods=['POST'])
def paitent_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        patient_dao = PatientLoginDAO()
        # Check patient credentials using the PatientLoginDAO
        if patient_dao.paitentValidation(username, password):
            id = patient_dao.getPaitentID(username)
            user_obj = User(id)
            login_user(user_obj)
            return redirect(url_for('dashboard'))
        else:
            return jsonify({'status': 'error', 'message': 'Invalid username or password'})

 
@app.route('/doctor_login', methods=['POST'])
def doctor_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        doctor_dao = DoctorLoginDAO()
        # Check patient credentials using the PatientLoginDAO
        if doctor_dao.doctorValidation(username, password):
            id = doctor_dao.getDoctorID(username)
            user_obj = User(id)
            login_user(user_obj)
            return redirect(url_for('doctorDashboard'))
        else:
            return jsonify({'status': 'error', 'message': 'Invalid username or password'})


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/doctorDashboard')
@login_required
def doctorDashboard():
    return render_template('doctor_dashboard.html')

@app.route('/dashboard/medical_records' , methods=['GET'])
@login_required
def medical_records():
    patient_id = current_user.id
    medicalHistory = medicalHistoryDAO()
    #print(int(patient_id[1]))
    medical_data = medicalHistory.getMedicalData(int(patient_id[1]))
    return render_template('medical_records.html', medical_data=medical_data)

@app.route('/doctorDashboard/view_Paitent_Records' , methods=['POST' , 'GET'])
@login_required
def view_Paitent_Records():
    return render_template('getpaitentdetails.html')

@app.route('/doctorDashboard/view_Paitent_Records/getPaitentRecords' , methods=['POST' , 'GET'])
@login_required
def getPaitentRecords():
    if request.method == 'GET':
        first_name = request.args.get('firstName')
        last_name = request.args.get('lastName')
        mobile_number = request.args.get('mobileNumber')

        paitent = PaitentDAO()
        patient_id = paitent.getPaitentID(first_name,last_name,mobile_number)
        if not patient_id:
            abort(404)
        medicalHistory = medicalHistoryDAO()
        medical_data = medicalHistory.getMedicalData(patient_id[0])
        medical_data = medical_data.to_dict(orient='records')
        return medical_data
    

    
@app.route('/doctorDashboard/addPatient',methods=['POST' , 'GET'])
@login_required
def addPatient():
    if request.method == 'POST':
        # Retrieve form data from the request
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        blood_group = request.form.get('blood_group')
        mobile_number = request.form.get('mobile_number')
        email = request.form.get('email')
        doctor_id = request.form.get('doctor_id')

        # Perform validation on form data if needed
        data = {
        'FirstName': [first_name],
        'LastName': [last_name],
        'Mobile': [mobile_number],
        'Email': [email],
        'Age': [age],
        'Gender': [gender],
        'BloodGroup': [blood_group],
        'DoctorID': [doctor_id]}

        # Add the patient to the database
        patient = PaitentDAO()
        patient.insert_patient_data(pd.DataFrame(data))
        patient_id = patient.getPaitentID(first_name, last_name,mobile_number )
        patient_id = patient_id[0]
        # Redirect to the medical records page or any other desired page
        return render_template('add_medical_records.html', patient_id=patient_id)
    

    # Render the add_paitent.html page for GET requests
    return render_template('add_paitent.html')


@app.route('/doctorDashboard/view_Paitent_Records/viewRecords' , methods=['POST' , 'GET'])
@login_required
def viewRecords():
    patient_records = request.args.get('data')
    medical_data = json.loads(patient_records)
    df = pd.DataFrame(medical_data)
    print(df)
    return render_template('medical_records_doctor.html', medical_data=df)

@app.route('/doctorDashboard/addMedicalRecords', methods=['GET', 'POST'])
@login_required
def addMedicalRecords():
    patient_id = request.args.get('patient_id')
    return render_template('add_medical_records.html', patient_id=patient_id)

@app.route('/submitMedicalRecords', methods=['POST'])
@login_required
def submitMedicalRecords():
    # Retrieve form data from the request
    patient_id = int(request.form.get('patient_id'))
    date = request.form.get('date_of_visit')
    medical_condition = request.form.get('medical_condition')
    medication_prescribed = request.form.get('medication_prescribed')
    medical_data = {
        'PatientID': [patient_id],
        'Date_of_Visit': [date],
        'Medical_Condition': [medical_condition],
        'Medication_Prescribed': [medication_prescribed]}
    medical_history = medicalHistoryDAO()
    medical_history.insert_medical_data(pd.DataFrame(medical_data))
    data = medical_history.getMedicalData(patient_id)
    return render_template('medical_records_doctor.html', medical_data=data)



@app.route('/dashboard/appointment_request')
@login_required
def appointment_request():
    return render_template('appointment_request.html')



@app.route('/index')
@login_required
def index():
    return f'Hello, {current_user.id}! This is your dashboard.'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(debug=True, port=5001)
