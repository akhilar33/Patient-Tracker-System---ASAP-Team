import json
import logging
from flask import Flask, request, jsonify ,render_template
from Buisness_Logic.paitentlogindao2 import PatientLoginDAO
from Buisness_Logic.DoctorLoginDAO import DoctorLoginDAO



app = Flask(__name__,
    static_url_path="",
    static_folder="../View",
    template_folder="../View/templates",)


# ... (rest of your code)
@app.route("/")
def index():
    """
    This is the starting point of the application.
    """
    logging.info('Server message: Loading the view/home page for the application')
    return render_template("index.html")
@app.route('/patient')
def patient():
    return render_template('patient.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/validate-patient-login', methods=['POST'])
def validate_patient_login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    patient_dao = PatientLoginDAO()
    result = patient_dao.paitentValidation(username, password)

    if result:
        return jsonify({'success': 'Login successful'})
    else:
        return jsonify({'error': 'Login failed'}), 401

@app.route('/validate_doctor_login', methods=['POST'])
def validate_doctor_login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    doctor  = DoctorLoginDAO()
    result = doctor.doctorValidation(username, password)

    if result:
        return jsonify({'success': 'Login successful'})
    else:
        return jsonify({'error': 'Login failed'}), 401



if __name__ == '__main__':
    app.run(debug=True , port=8000)
