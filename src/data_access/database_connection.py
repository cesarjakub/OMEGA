import pyodbc
from src.settings.config_reader import ConfigSettings

class DatabaseConnection:

    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            server_name, server_database, server_uid, server_pwd = ConfigSettings.get_database_data()

            self.connection = pyodbc.connect(
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={server_name};"
                f"DATABASE={server_database};"
                f"UID={server_uid};"
                f"PWD={server_pwd}"
            )

        except ValueError as e:
            raise ValueError(e)
        except Exception:
            raise ConnectionError("Failed to connect to the database")
        finally:
            self.disconnect()

    def disconnect(self):
        self.connection.close()
