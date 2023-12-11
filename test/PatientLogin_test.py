import unittest
from unittest.mock import patch
import pandas as pd
import sys
from src.Backend.Buisness_Logic.paitentlogindao2 import PatientLoginDAO

sys.path.insert(0, "../")


class TestPatientLoginDAO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up any common resources needed for the tests
        pass

    @classmethod
    def tearDownClass(cls):
        # Clean up any common resources used by the tests
        pass

    def setUp(self):
        # Set up resources specific to each test case
        pass

    def tearDown(self):
        # Clean up resources after each test case
        pass

    @patch('pandas.DataFrame.to_sql')
    def test_insert_patient_login_data(self, mock_to_sql):
        # Mocking the DataFrame to be inserted
        data = pd.DataFrame({
            'FirstName': ['ARIHANT'],
            'LastName': ['JAIN'],
            'Username': ['arijain'],
            'Password': ['arijain']
        })

        # Mocking the to_sql method to avoid actual database interaction
        dao = PatientLoginDAO()
        dao.insert_patient_data(data)

        # Ensure that to_sql method is called with the correct arguments
        mock_to_sql.assert_called_once_with(
            name='patient_login', con=dao.engine, if_exists='append', index=False)

    def test_get_patient_login_data(self):
        dao = PatientLoginDAO()
        username = 'arijain'
        login_data = dao.getquery('Username', username)

        # Ensure that the returned DataFrame is not empty
        self.assertFalse(login_data.empty)

    def test_update_patient_login_data(self):
        dao = PatientLoginDAO()
        username = 'arijain'
        field_to_update = 'Password'
        new_value = 'NewPassword123'

        # Update the patient login record
        dao.updated(username, field_to_update, new_value)

        # Fetch the updated record to verify the update
        updated_data = dao.getquery('Username', username)

        # Ensure that the updated data has the new value
        self.assertEqual(updated_data['Password'].iloc[0], new_value)

    def test_delete_patient_login_data(self):
        dao = PatientLoginDAO()
        username = 'arijain'

        # Delete the patient login record
        dao.delete(username)

        # Try fetching the deleted record to ensure it doesn't exist
        deleted_data = dao.getquery('Username', username)

        # Ensure that the deleted data is empty
        self.assertTrue(deleted_data.empty)

    def test_patient_login_validation(self):
        dao = PatientLoginDAO()
        username = 'arijain'
        password = 'arijain'

        # Validate patient login credentials
        result = dao.paitentValidation(username, password)

        # Ensure that the validation is successful
        self.assertTrue(result)

    def test_get_patient_id(self):
        dao = PatientLoginDAO()
        username = 'arijain'

        # Get patient ID based on the username
        patient_id = dao.getPaitentID(username)

        # Ensure that the patient ID is not None
        self.assertIsNotNone(patient_id)


if __name__ == '__main__':
    unittest.main()
