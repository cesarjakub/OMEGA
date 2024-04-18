from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.users import Users

class UsersDAO(IDao):
    """Data Access Object for interacting with user data in the database."""

    def __init__(self, database: DatabaseConnection):
        """
        Initializes a UsersDAO instance.

        Parameters:
            database (DatabaseConnection): The database connection object.
        """
        super().__init__(database)

    def create(self, record: Users):
        """
        Creates a new user record in the database.

        Parameters:
            record (Users): The Users object containing the data to be inserted.

        Raises:
            Exception: If an error occurs while creating the user record.
        """
        try:
            msg = "Error with creating user."
            query = """
                    EXEC Add_user ?,?,?,?,?,?
                    """
            params = (record.first_name, record.last_name, record.date_of_birth, record.email, record.phone, record.address, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        """
        Reads user records from the database.

        Returns:
            list: A list of user records.

        Raises:
            Exception: If an error occurs while reading the user records.
        """
        msg = "No records."
        try:
            query = """
                    SELECT * FROM User_info
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg

    def update(self, record: Users):
        """
        Updates an existing user record in the database.

        Parameters:
            record (Users): The Users object containing the updated data.

        Raises:
            Exception: If an error occurs while updating the user record.
        """
        try:
            msg = "Error with updating user."
            query = """
                    UPDATE users
                    SET First_name = ?, Last_name = ?, Date_of_birth = ?, Email = ?, Phone = ?, Address = ?
                    WHERE ID = ?;
                    """
            params = (record.first_name, record.last_name, record.date_of_birth, record.email, record.phone, record.address, record.id)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Users):
        """
        Deletes a user record from the database.

        Parameters:
            record (Users): The Users object to be deleted.

        Raises:
            Exception: If an error occurs while deleting the user record.
        """
        try:
            msg = "Error with deleting user."
            query = """
                    DELETE FROM users WHERE Email = ?;
                    """
            params = (record.email, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read_first(self):
        """
        Reads first names of users from the database.

        Returns:
            list: A list of first names of users.

        Raises:
            Exception: If an error occurs while reading user first names.
        """
        msg = "No records."
        try:
            query = """
                    SELECT First_name FROM users
                    """
            first = self.database.select(query, msg)
            return first
        except Exception as e:
            return msg

    def read_last(self):
        """
        Reads last names of users from the database.

        Returns:
            list: A list of last names of users.

        Raises:
            Exception: If an error occurs while reading user last names.
        """
        msg = "No records."
        try:
            query = """
                    SELECT Last_name FROM users
                    """
            last = self.database.select(query, msg)
            return last
        except Exception as e:
            return msg

    def read_record(self):
        """
        Reads email addresses of users from the database.

        Returns:
            list: A list of email addresses of users.

        Raises:
            Exception: If an error occurs while reading user email addresses.
        """
        msg = "No records."
        try:
            query = """
                    SELECT Email FROM users
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg
