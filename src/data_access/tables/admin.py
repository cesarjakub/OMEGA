
class Admin:
    """Class representing an admin user."""

    def __init__(self, id: int, users_id: int, role: str, password: str):
        """
        Initializes an Admin instance.

        Parameters:
            id (int): The unique identifier for the admin.
            users_id (int): The ID of the associated user.
            role (str): The role of the admin.
            password (str): The password of the admin.

        Raises:
            ValueError: If id or users_id is negative.
        """

        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        if users_id < 0:
            raise ValueError("Users id must be a non-negative integer.")

        self.id = id
        self.users_id = users_id
        self.role = role
        self.password = password