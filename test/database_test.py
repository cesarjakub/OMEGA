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

    @patch('pyodbc.connect')
    def test_select_with_params_success(self, mock_connect):
        db = DatabaseConnection()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('result',)]
        mock_connect.return_value.cursor.return_value = mock_cursor

        result = db.select_with_params("SELECT * FROM table WHERE column=?", ('value',), "No records found")

        self.assertEqual(result, [('result',)])
        mock_connect.assert_called_once()

    @patch('pyodbc.connect')
    def test_select_with_params_no_records_found(self, mock_connect):
        db = DatabaseConnection()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_connect.return_value.cursor.return_value = mock_cursor

        result = db.select_with_params("SELECT * FROM table WHERE column=?", ('value',), "No records found")

        self.assertEqual(result, "No records found")

    @patch('pyodbc.connect')
    def test_select_no_records_found(self, mock_connect):
        db = DatabaseConnection()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_connect.return_value.cursor.return_value = mock_cursor

        result = db.select("SELECT * FROM table WHERE column=?", "No records found")

        self.assertEqual(result, "No records found")


if __name__ == '__main__':
    unittest.main()
