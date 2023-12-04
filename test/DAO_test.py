import unittest
from unittest.mock import Mock
from unittest.mock import patch
import pandas as pd
import sys
sys.path.insert(0, "../")
from  src.Backend.Buisness_Logic.DoctorLoginDAO import DoctorLoginDAO 



class TestDoctorLoginDAO(unittest.TestCase):

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

    def test_insert_doctor_data(self):
        # Mocking the DataFrame to be inserted
        data = pd.DataFrame({'doctor_id': [1], 'username': ['DrSmith'], 'password': ['DrSmithPass1']})

        # Mocking the to_sql method to avoid actual database interaction
        with patch('pandas.DataFrame.to_sql') as mock_to_sql:
            dao = DoctorLoginDAO()
            dao.insert_doctor_data(data)

            # Ensure that to_sql method is called with the correct arguments
            mock_to_sql.assert_called_once_with(name='DoctorLogin', con=dao.engine, if_exists='append', index=False)

    def test_doctor_validation_valid(self):
        dao = DoctorLoginDAO()
        # Assuming you have a valid doctor in your database
        self.assertTrue(dao.doctorValidation('DrSmith', 'DrSmithPass1'))

    def test_doctor_validation_invalid(self):
        dao = DoctorLoginDAO()
        # Assuming you don't have a doctor with these credentials in your database
        self.assertFalse(dao.doctorValidation('NonExistentDoctor', 'InvalidPassword'))

    def test_get_doctor_id(self):
        # Assuming the doctor 'DrSmith' does not exist in the database
        dao = DoctorLoginDAO()
        doctor_id = dao.getDoctorID('DrSmi')
        self.assertIsNone(doctor_id)

if __name__ == '__main__':
    unittest.main()
