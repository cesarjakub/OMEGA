import configparser
import json

class ConfigSettings:

    INI_FILE_NAME = "./config/config.ini"
    JSON_FILE_NAME = "./config/config_main.json"
    @staticmethod
    def get_database_data(file_name):
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
