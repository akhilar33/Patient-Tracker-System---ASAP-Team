import unittest
import pytest
from unittest.mock import MagicMock
import pandas as pd

import sys
sys.path.insert(0, "../")
from  src.Backend.Buisness_Logic.DoctorLoginDAO import DoctorLoginDAO 


@pytest.fixture
def mock_mysql_connector(mocker):
    return mocker.patch("mysql.connector.connect")

@pytest.fixture
def mock_sqlalchemy_create_engine(mocker):
    return mocker.patch("sqlalchemy.create_engine")

@pytest.fixture
def doctor_login_dao(mock_mysql_connector, mock_sqlalchemy_create_engine):
    return DoctorLoginDAO()

def test_insert_doctor_data(doctor_login_dao, mocker):
    mocker.patch("pandas.DataFrame.to_sql")
    mocker.patch("builtins.print")

    mock_data = pd.DataFrame(
        {"doctor_id": [1], "username": ["DrSmith"], "password": ["DrSmithPass1"]})
    doctor_login_dao.insert_doctor_data(mock_data)

    pd.DataFrame.to_sql.assert_called_once_with(
        name='DoctorLogin', con=doctor_login_dao.engine, if_exists='append', index=False)
    print.assert_called_once_with("Data inserted successfully.")



def test_doctorValidation(doctor_login_dao, mocker):
    mocker.patch.object(doctor_login_dao.cursor, "execute")
    mocker.patch.object(doctor_login_dao.cursor, "fetchone",
                        return_value=(1, 'DrSmith', 'DrSmithPass1'))

    result = doctor_login_dao.doctorValidation('DrSmith', 'DrSmithPass1')

    doctor_login_dao.cursor.execute.assert_called_once_with(
        "SELECT * FROM DoctorLogin WHERE username = %s AND password = %s", ('DrSmith', 'DrSmithPass1'))
    assert result is True

def test_getDoctorID(doctor_login_dao, mocker):
    mocker.patch.object(doctor_login_dao.cursor, "execute")
    mocker.patch.object(doctor_login_dao.cursor, "fetchone", return_value=(1,))

    result = doctor_login_dao.getDoctorID('DrSmith')

    doctor_login_dao.cursor.execute.assert_called_once_with(
        "SELECT DoctorID FROM DoctorLogin WHERE username = %s", ('DrSmith',))
    assert result == (1,)

def test_getDoctorID2(doctor_login_dao, mocker):
    mocker.patch.object(doctor_login_dao.cursor, "execute")
    mocker.patch.object(doctor_login_dao.cursor, "fetchone", return_value= None)

    result = doctor_login_dao.getDoctorID('DrSm')

    doctor_login_dao.cursor.execute.assert_called_once_with(
        "SELECT DoctorID FROM DoctorLogin WHERE username = %s", ('DrSm',))
    assert result is None
