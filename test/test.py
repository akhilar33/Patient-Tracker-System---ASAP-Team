import unittest
from unittest.mock import Mock
from unittest.mock import patch
import pandas as pd
from io import StringIO
import sys
sys.path.insert(0, "../")
from src.Backend.Buisness_Logic.PaitentDAO import PaitentDAO
from src.Backend.Buisness_Logic.paitentlogindao2 import PatientLoginDAO 

class TestPaitentDAO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the PaitentDAO instance for testing
        cls.patient_dao = PaitentDAO()

    def setUp(self):
        # Reset the state before each test
        self.patient_dao.connection.rollback()
    def test_insert_patient_data(self):
        # Mock data for testing
        mock_data = pd.DataFrame({
            'FirstName': ['John'],
            'LastName': ['Doe'],
            'Mobile': ['1234567890']
        })

        # Mock the 'to_sql' method to avoid actual database insertion
        with patch('pandas.DataFrame.to_sql') as mock_to_sql:
            self.patient_dao.insert_patient_data(mock_data)

            # Check if the 'to_sql' method was called with the expected arguments
            mock_to_sql.assert_called_once_with(
                name='patient', con=self.patient_dao.engine, if_exists='append', index=False
            )

    def test_insert_patient_data_exception_handling(self):
        # Mock data for testing
        mock_data = pd.DataFrame({
            'FirstName': ['John'],
            'LastName': ['Doe'],
            'Mobile': ['1234567890']
        })

        # Mock the 'to_sql' method to raise an exception
        with patch('pandas.DataFrame.to_sql', side_effect=Exception("Mocked exception during to_sql")), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.patient_dao.insert_patient_data(mock_data)

        # Check the error message or perform additional assertions if needed
        self.assertIn("Error: Mocked exception during to_sql", mock_stdout.getvalue())



            
    def test_getquery(self):
        # Mock data for testing
        feild = 'FirstName'
        patientdata = 'John'

        # Mock the 'execute' method to avoid actual database query
        with patch.object(self.patient_dao.cursor, 'fetchall') as mock_fetchall:
            result = self.patient_dao.getquery(feild, patientdata)

            # Check if the 'execute' method was called with the expected arguments
            mock_fetchall.assert_called_once()

            # Check the type of the result (assuming it's a DataFrame)
            self.assertIsNone(result)

    def test_updated(self):
        # Mock data for testing
        first_name = 'John'
        field_to_update = 'LastName'
        new_value = 'Doe'

        # Mock the 'execute' and 'commit' methods to avoid actual database update
        with patch.object(self.patient_dao.connection, 'commit'), \
             patch.object(self.patient_dao.cursor, 'execute') as mock_execute:
            self.assertIsNone(self.patient_dao.updated(first_name, field_to_update, new_value))

            # Check if the 'execute' method was called with the expected arguments
            mock_execute.assert_called_once()

    def test_delete(self):
        # Mock data for testing
        first_name = 'John'

        # Mock the 'execute', 'commit', 'close' methods to avoid actual database deletion
        with patch.object(self.patient_dao.connection, 'commit'), \
             patch.object(self.patient_dao.cursor, 'execute'), \
             patch.object(self.patient_dao.cursor, 'close'), \
             patch.object(self.patient_dao.connection, 'close'):
            self.assertIsNone(self.patient_dao.delete(first_name))

    def test_getPaitentID(self):
        # Mock data for testing
        first_name = 'John'
        last_name = 'Doe'
        mobile = '1234567890'

        # Mock the 'execute' and 'fetchone' methods to avoid actual database query
        with patch.object(self.patient_dao.cursor, 'fetchone', return_value=(1,)):
            result = self.patient_dao.getPaitentID(first_name, last_name, mobile)

            # Check if the 'execute' method was called with the expected arguments
            self.assertEqual(result, (1,))



class TestPatientLoginDAO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the PatientLoginDAO instance for testing
        cls.patient_login_dao = PatientLoginDAO()

    def setUp(self):
        # Reset the state before each test
        self.patient_login_dao.connection.rollback()

    @patch('pandas.DataFrame.to_sql')
    def test_insert_patient_data_success(self, mock_to_sql):
        # Mock data for testing
        mock_data = pd.DataFrame({
            'FirstName': ['John'],
            'LastName': ['Doe'],
            'Username': ['john_doe'],
            'Password': ['password123']
        })

        # Mock the 'execute' method to return a PatientID
        with patch.object(self.patient_login_dao.connection, 'cursor') as mock_cursor:
            mock_cursor.fetchone.return_value = (1,)

            # Run the method under test
            self.patient_login_dao.insert_patient_data(mock_data)

        # Check if 'to_sql' method was called with the expected arguments
        mock_to_sql.assert_called_once_with(
            name='patient_login', con=self.patient_login_dao.engine, if_exists='append', index=False
        )

        
    @patch('pandas.DataFrame.to_sql')
    def test_insert_patient_data_no_patient_id(self, mock_to_sql):
        # Mock data for testing
        mock_data = pd.DataFrame({
            'FirstName': ['John'],
            'LastName': ['Doe'],
            'Username': ['john_doe'],
            'Password': ['password123']
        })
        with patch('pandas.DataFrame.to_sql', side_effect=Exception("Mocked exception during to_sql")), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.patient_login_dao.insert_patient_data(mock_data)
        self.assertIn("Error: Mocked exception during to_sql", mock_stdout.getvalue())

    def test_paitentValidation_valid_credentials(self):
        # Mock the 'execute' method to return a result for valid credentials
        with patch.object(self.patient_login_dao.connection, 'cursor') as mock_cursor:
            mock_cursor.fetchone.return_value = (1, 'john_doe', 'password123')

            # Run the method under test
            result = self.patient_login_dao.paitentValidation('arijain', 'arijain')

            # Check the result
            self.assertTrue(result)

    def test_paitentValidation_invalid_credentials(self):
        # Mock the 'execute' method to return None for invalid credentials
        with patch.object(self.patient_login_dao.connection, 'cursor') as mock_cursor:
            mock_cursor.fetchone.return_value = None

            # Run the method under test
            result = self.patient_login_dao.paitentValidation('john_doe', 'invalid_password')

            # Check the result
            self.assertFalse(result)
    
    def test_getPaitentID(self):
        # Mock data for testing
        username = 'arijain'


        # Mock the 'execute' and 'fetchone' methods to avoid actual database query
        with patch.object(self.patient_login_dao.cursor, 'fetchone', return_value=(16,)):
            result = self.patient_login_dao.getPaitentID( username)

            # Check if the 'execute' method was called with the expected arguments
            self.assertEqual(result, (16,))
    
    def test_getquery(self):
        # Mock data for testing
        feild = 'username'
        patientdata = 'arij'

        # Mock the 'execute' method to avoid actual database query
        with patch.object(self.patient_login_dao.cursor, 'fetchall') as mock_fetchall:
            result = self.patient_login_dao.getquery(feild, patientdata)

            # Check if the 'execute' method was called with the expected arguments
            mock_fetchall.assert_called_once()

            # Check the type of the result (assuming it's a DataFrame)
            self.assertIsNone(result)  


if __name__ == '__main__':
    unittest.main()
