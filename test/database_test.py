import unittest
from unittest.mock import patch, MagicMock
from src.settings.config_reader import ConfigSettings
from src.data_access.database_connection import DatabaseConnection

class TestDatabaseConnection(unittest.TestCase):

    @patch('pyodbc.connect')
    def test_connect_success(self, mock_connect):
        with patch.object(ConfigSettings, 'get_database_config',
                          return_value=('server', 'database', 'user', 'password')):
            db = DatabaseConnection()
            db.connect()
            self.assertTrue(mock_connect.called)

    @patch('pyodbc.connect')
    def test_connect_missing_config(self, mock_connect):
        with patch.object(ConfigSettings, 'get_database_config', side_effect=ValueError):
            db = DatabaseConnection()
            with self.assertRaises(ValueError):
                db.connect()
            self.assertFalse(mock_connect.called)

    @patch('pyodbc.connect')
    def test_connect_other_errors(self, mock_connect):
        with patch.object(ConfigSettings, 'get_database_config', side_effect=Exception):
            db = DatabaseConnection()
            with self.assertRaises(ConnectionError):
                db.connect()
            self.assertFalse(mock_connect.called)


if __name__ == '__main__':
    unittest.main()
