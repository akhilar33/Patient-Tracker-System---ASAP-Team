import json
import logging
from flask import Flask, render_template, redirect, url_for, request, flash
from flask import jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from Buisness_Logic.paitentlogindao2 import PatientLoginDAO
from Buisness_Logic.DoctorLoginDAO import DoctorLoginDAO
from Buisness_Logic.medicalHistoryDAO import medicalHistoryDAO

from flask_session import Session


app = Flask(__name__,
    static_url_path="",
    static_folder="../View",
    template_folder="../View/templates",)

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



@app.route('/login', methods=[ 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check patient credentials using the PatientLoginDAO
        patient_dao = PatientLoginDAO()
        if patient_dao.paitentValidation(username, password):
            # Load the user and log them in
            id = patient_dao.getPaitentID(username)
            user_obj = User(id)
            login_user(user_obj)
            return redirect(url_for('dashboard'))
        else:
            return jsonify({'status': 'error', 'message': 'Invalid username or password'})

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard/medical_records' , methods=['GET'])
@login_required
def medical_records():
    patient_id = current_user.id
    medicalHistory = medicalHistoryDAO()
    #print(int(patient_id[1]))
    medical_data = medicalHistory.getMedicalData(int(patient_id[1]))
    return render_template('medical_records.html', medical_data=medical_data)



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
    app.run(debug=True , port=8000)
