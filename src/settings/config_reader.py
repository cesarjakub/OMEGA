import configparser
import json

class ConfigSettings:

    FILE_NAME = "../config/config_v.json"
    @staticmethod
    def get_database_data():
        params = ["server", "database_name", "UID", "PWD"]

        conf = configparser.ConfigParser()
        conf.read(ConfigSettings.FILE_NAME)

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
    def get_database_config():
        with open(ConfigSettings.FILE_NAME, 'r') as reader:
            db_conn_data = json.load(reader)

        server_name = db_conn_data["database"]["server"]
        server_database = db_conn_data["database"]["DATABASE"]
        server_uid = db_conn_data["database"]["UID"]
        server_pwd = db_conn_data["database"]["PWD"]

        return server_name, server_database, server_uid, server_pwd
