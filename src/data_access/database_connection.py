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

    def disconnect(self):
        self.connection.close()

    # selects
    def select_with_params(self, query, params, msg):
        try:
            if not params:
                raise Exception("Please fill in field")
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            records = cursor.fetchall()
            cursor.close()
            if not records:
                return msg
            return records
        except Exception as e:
            raise Exception(e)
        finally:
            self.disconnect()

    def select(self, query, msg):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()
            if not records:
                return msg
            return records
        except Exception as e:
            raise Exception(e)
        finally:
            self.disconnect()

    # executables
    def exec(self, query, params, msg):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            cursor.commit()
            cursor.close()
        except Exception as e:
            raise Exception(msg)
        finally:
            self.disconnect()