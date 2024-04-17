import unittest
from src.settings.config_reader import ConfigSettings

class TestConfigSettings(unittest.TestCase):

    def test_get_database_data(self):
        server, database_name, UID, PWD = ConfigSettings.get_database_data("../config/config.ini")

        expected_server = 'DESKTOP-2QAB4PC\\SQLEXPRESS'
        expected_database_name = 'Library_management'
        expected_UID = 'test'
        expected_PWD = '1234'

        self.assertEqual(server, expected_server)
        self.assertEqual(database_name, expected_database_name)
        self.assertEqual(UID, expected_UID)
        self.assertEqual(PWD, expected_PWD)

    def test_get_database_data_invalid_config_file(self):
        ConfigSettings.INI_FILE_NAME = "invalid_config.ini"

        with self.assertRaises(Exception):
            ConfigSettings.get_database_data("invalid_config.ini")

    def test_get_database_config(self):
        server, database_name, UID, PWD = ConfigSettings.get_database_config("../config/config_main.json")

        expected_server = 'DESKTOP-2QAB4PC\\SQLEXPRESS'
        expected_database_name = 'Library_management'
        expected_UID = 'test'
        expected_PWD = '1234'

        self.assertEqual(server, expected_server)
        self.assertEqual(database_name, expected_database_name)
        self.assertEqual(UID, expected_UID)
        self.assertEqual(PWD, expected_PWD)

    def test_get_database_config_invalid_config_file(self):
        ConfigSettings.JSON_FILE_NAME = "invalid_config.json"

        with self.assertRaises(FileNotFoundError):
            ConfigSettings.get_database_config("invalid_config.json")


if __name__ == '__main__':
    unittest.main()
