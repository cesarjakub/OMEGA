from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.admin import Admin


class AdminDAO(IDao):
    """A class for handling CRUD operations related to the Admin table in the database."""

    def __init__(self, database: DatabaseConnection):
        """
        Initializes an AdminDAO instance.

        Parameters:
            database (DatabaseConnection): The database connection object.
        """
        super().__init__(database)

    def create(self, record: Admin):
        """
        Creates a new admin record in the database.

        Parameters:
            record (Admin): The admin record to be created.

        Raises:
            Exception: If an error occurs during the creation process.
        """
        try:
            msg = "Error with creating admin."
            query = """
                    INSERT INTO admin(Users_ID, Role, Password) VALUES(?, ?, ?)
                    """
            params = (record.users_id, record.role, record.password, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        """
        Retrieves all admin records from the database.

        Raises:
            Exception: If no records are found or an error occurs during the retrieval process.
        """
        try:
            msg = "No records."
            query = """
                    SELECT * FROM admin
                    """
            self.database.select(query, msg)
        except Exception as e:
            raise Exception(e)

    def update(self, record: Admin):
        """
        Updates an existing admin record in the database.

        Parameters:
            record (Admin): The admin record to be updated.

        Raises:
            Exception: If an error occurs during the update process.
        """
        try:
            msg = "Error with updating admin."
            query = """
                    UPDATE admin SET Users_ID = ?, Role = ?, Password = ? WHERE ID = ?
                    """
            params = (record.users_id, record.role, record.password, record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Admin):
        """
        Deletes an admin record from the database.

        Parameters:
            record (Admin): The admin record to be deleted.

        Raises:
            Exception: If an error occurs during the deletion process.
        """
        try:
            msg = "Error with deleting admin."
            query = """
                    DELETE FROM admin WHERE Password = ?
                    """
            params = (record.password,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read_with_params(self, email, password):
        """
        Retrieves an admin record based on the provided email and password.

        Parameters:
            email (str): The email of the admin.
            password (str): The password of the admin.

        Raises:
            Exception: If the provided email or password is incorrect or an error occurs during the retrieval process.
        """
        try:
            msg = "Email or password is wrong! Please try again."
            query = """
                    SELECT Email, Password FROM users INNER JOIN admin ON users.ID = admin.Users_ID 
                    WHERE users.Email = ? AND admin.Password = ?
                    """
            params = (email, password,)
            _ = self.database.select_with_params(query, params, msg)
        except Exception as e:
            raise Exception(e)
