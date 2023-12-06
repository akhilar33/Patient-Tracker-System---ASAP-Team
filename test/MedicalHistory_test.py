from src.Backend.Buisness_Logic.medicalHistoryDAO import medicalHistoryDAO
import unittest
from unittest.mock import patch
import pandas as pd
import sys
sys.path.insert(0, "../")


class TestMedicalHistoryDAO(unittest.TestCase):

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
    def test_insert_medical_data(self, mock_to_sql):
        # Mocking the DataFrame to be inserted
        data = pd.DataFrame({
            'Patient_ID': [1],
            'Date_of_Visit': ['2023-10-01'],
            'Medical_Condition': ['Fever'],
            'Medication_Prescribed': ['Paracetamol']
        })

        # Mocking the to_sql method to avoid actual database interaction
        dao = medicalHistoryDAO()
        dao.insert_medical_data(data)

        # Ensure that to_sql method is called with the correct arguments
        mock_to_sql.assert_called_once_with(
            name='medical_history', con=dao.engine, if_exists='append', index=False)

    def test_get_medical_data(self):
        # Assuming there is a patient with ID 1 in the medical history table
        dao = medicalHistoryDAO()
        patient_id = 1
        medical_data = dao.getMedicalData(patient_id)

        # Ensure that the returned DataFrame is not empty
        self.assertFalse(medical_data.empty)


if __name__ == '__main__':
    unittest.main()
