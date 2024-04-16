import unittest
from src.settings.config_reader import ConfigSettings

class TestConfigSettings(unittest.TestCase):

    def test_get_database_data(self):
        server, database_name, UID, PWD = ConfigSettings.get_database_data()

        expected_server = 'DESKTOP-2QAB4PC\\SQLEXPRESS'
        expected_database_name = 'Library_management'
        expected_UID = 'test'
        expected_PWD = '1234'

        self.assertEqual(server, expected_server)
        self.assertEqual(database_name, expected_database_name)
        self.assertEqual(UID, expected_UID)
        self.assertEqual(PWD, expected_PWD)

    def test_get_database_data_invalid_config_file(self):
        ConfigSettings.FILE_NAME = "invalid_config.ini"

        with self.assertRaises(ValueError):
            ConfigSettings.get_database_data()

    def test_get_database_data_missing_param(self):
        ConfigSettings.FILE_NAME = "missing_param_config.ini"

        with self.assertRaises(ValueError):
            ConfigSettings.get_database_data()

    def test_get_database_data_empty_config(self):
        ConfigSettings.FILE_NAME = "empty_config.ini"

        with self.assertRaises(ValueError):
            ConfigSettings.get_database_data()


if __name__ == '__main__':
    unittest.main()