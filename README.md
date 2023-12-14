 
# Patient Tracker Project

## Overview

Welcome to the Patient Tracker project! This healthcare management system is designed to streamline patient data management for medical professionals and staff. The project employs a Client-Server architecture, utilizing Python, Flask, MySQL, HTML, CSS, and JavaScript to deliver a comprehensive and user-friendly solution.

## Features

- **User Roles:**
  - Doctors
  - Hospital Management Staff
  - Patients
  - Nurses

- **Functionality:**
  - User authentication and role-based access control
  - Real-time schedule viewing for doctors
  - Patient data management (addition, retrieval)
  - Business logic for efficient data presentation
  - API development for secure data access
  - Structured and organized data storage in MySQL database

## Technologies Used

- **Programming Language:** Python
- **Web Framework:** Flask
- **Frontend Framework:** HTML, CSS, JavaScript
- **API Development:** Flask
- **Database Management System:** MySQL
- **Version Control:** Git (GitHub)

## Setup Instructions

1. Clone the repository.
2. Run ```pip3 install -r requirements.txt.``` This installs all the necessary libraries. 
2. Run ```./init.sh``` from the root folder of the project. This starts up the flask server and installs the necessary libraries.
3. Open `http://127.0.0.1:5000/` on any browser to view the UI.

## Testing & Analysis 
Testing is done using Pytest. It is advised to create a virtual enviroment (python venv, conda) to install the packages.
Preferred version of python - **python3.8**. 

**Statement Coverage**
1. Run the following script to generate line coverage report: ```./statement_coverage.sh```
3. The statement coverage is approximalty **92%** 

**Decision Coverage**

2. Run the following script to generate branch coverage report: ```./decision_coverage.sh```
3. The decision coverage is approximately **93%** 

## Contribution Guidelines
We welcome contributions to enhance the functionality and user experience. Please follow these guidelines:

1. Fork the repository and create a new branch for your changes.
2. Make sure to test your changes thoroughly before submitting a pull request.
3. Clearly describe the purpose and impact of your changes.

## Acknowledgments

We would like to express our gratitude to the open-source community for the tools and frameworks that made this project possible. We would also like to thank Prof. Conboy and her team for their constant guidance.

## Happy coding!


<<<<<<< HEAD
=======

# Comments 
- testing database 
- testing DAO 
- 
>>>>>>> 68ac0cd7238362eb51985062707ced39ae5ac620
