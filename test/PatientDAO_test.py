import unittest
from unittest.mock import patch
import pandas as pd
import sys
from src.Backend.Buisness_Logic.PaitentDAO import PaitentDAO

sys.path.insert(0, "../")


class TestPaitentDAO(unittest.TestCase):

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
    def test_insert_patient_data(self, mock_to_sql):
        # Mocking the DataFrame to be inserted
        data = pd.DataFrame({
            'FirstName': ['John'],
            'LastName': ['Doe'],
            'Mobile': ['1234567890'],
            'Email': ['john@example.com'],
            'Age': [30],
            'Gender': ['Male'],
            'BloodGroup': ['A+'],
            'DoctorID': [1]
        })

        # Mocking the to_sql method to avoid actual database interaction
        dao = PaitentDAO()
        dao.insert_patient_data(data)

        # Ensure that to_sql method is called with the correct arguments
        mock_to_sql.assert_called_once_with(
            name='patient', con=dao.engine, if_exists='append', index=False)

    def test_get_paitent_id(self):
        dao = PaitentDAO()
        patient_id = dao.getPaitentID('Dodda', 'Reddy', '+918886242222')

        # Ensure that the returned patient ID is not None
        self.assertIsNotNone(patient_id)

    def test_update_patient_data(self):
        dao = PaitentDAO()
        first_name = 'John'
        field_to_update = 'Age'
        new_value = 31

        # Update the patient record
        dao.updated(first_name, field_to_update, new_value)

        # Fetch the updated record to verify the update
        updated_data = dao.getquery('FirstName', first_name)

        # Ensure that the updated data has the new value
        self.assertEqual(updated_data['Age'].iloc[0], new_value)


if __name__ == '__main__':
    unittest.main()
