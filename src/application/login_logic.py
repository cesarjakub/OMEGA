from src.data_access.daos.adminDAO import AdminDAO

class LoginLogic:
    """A class for handling login logic."""

    def __init__(self, database):
        """
        Initializes a LoginLogic instance.

        Parameters:
            database: The database object to perform login operations.
        """
        self.database = database

    def login(self, email, password):
        """
        Performs a login operation.

        Parameters:
            email (str): The email of the user trying to log in.
            password (str): The password of the user trying to log in.

        Raises:
            Exception: If an error occurs during the login process.
        """
        try:
            admin = AdminDAO(self.database)
            admin.read_with_params(email, password)
        except Exception as e:
            raise Exception(e)