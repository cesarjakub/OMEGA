import configparser
import json

class ConfigSettings:
    """Class to handle configuration settings."""

    INI_FILE_NAME = "./config/config.ini"
    JSON_FILE_NAME = "./config/config_main.json"
    @staticmethod
    def get_database_data(file_name):
        """
        Get database connection data from an INI file.

        Parameters:
            file_name (str): The path to the INI file.

        Returns:
            tuple: A tuple containing server name, database name, UID, and PWD.

        Raises:
            ValueError: If the config file is empty, invalid, or if any parameter is missing.
        """
        params = ["server", "database_name", "UID", "PWD"]

        conf = configparser.ConfigParser()
        conf.read(file_name)

        if not conf.sections():
            raise ValueError("Config file is empty or invalid.")

        for param in params:
            if conf.get("DATABASE", param) is None:
                raise ValueError(f"Parameter: {param} is missing!")

        server = conf.get("DATABASE", params[0])
        database_name = conf.get("DATABASE", params[1])
        UID = conf.get("DATABASE", params[2])
        PWD = conf.get("DATABASE", params[3])

        return server, database_name, UID, PWD

    @staticmethod
    def get_database_config(file_name):
        """
        Get database connection configuration from a JSON file.

        Parameters:
            file_name (str): The path to the JSON file.

        Returns:
            tuple: A tuple containing server name, database name, UID, and PWD.

        Raises:
            FileNotFoundError: If the config file is not found.
            ValueError: If the JSON format is invalid or if any key is missing.
        """
        try:
            with open(file_name, 'r') as reader:
                db_conn_data = json.load(reader)

            server_name = db_conn_data["database"]["server"]
            server_database = db_conn_data["database"]["DATABASE"]
            server_uid = db_conn_data["database"]["UID"]
            server_pwd = db_conn_data["database"]["PWD"]

            return server_name, server_database, server_uid, server_pwd
        except FileNotFoundError:
            raise FileNotFoundError("Config file not found!")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in config file!")
        except KeyError as e:
            raise KeyError(f"Missing key: {e}")
