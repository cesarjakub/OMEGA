import pyodbc
from src.settings.config_reader import ConfigSettings
from CTkMessagebox import CTkMessagebox

class DatabaseConnection:
    """Class to handle database connection and queries."""

    def __init__(self):
        """Initialize a DatabaseConnection instance."""
        self.connection = None

    def connect(self):
        """Connect to the database."""
        try:
            server_name, server_database, server_uid, server_pwd = ConfigSettings.get_database_config("./config/config_main.json")

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
        """Disconnect from the database."""
        self.connection.close()

    # selects
    def select_with_params(self, query, params, msg):
        """
        Execute a select query with parameters.

        Parameters:
            query (str): The SQL query to execute.
            params (tuple): The parameters for the query.
            msg (str): The message to return if no records are found.

        Returns:
            records (list): The result records of the query.
            msg (str): The message indicating no records found.

        Raises:
            Exception: If an error occurs during query execution.
        """
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
        """
        Execute a select query.

        Parameters:
            query (str): The SQL query to execute.
            msg (str): The message to return if no records are found.

        Returns:
            records (list): The result records of the query.
            msg (str): The message indicating no records found.

        Raises:
            Exception: If an error occurs during query execution.
        """
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
        """
        Execute a query without returning records.

        Parameters:
            query (str): The SQL query to execute.
            params (tuple): The parameters for the query.
            msg (str): The message to raise if an error occurs during query execution.

        Raises:
            Exception: If an error occurs during query execution.
        """
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