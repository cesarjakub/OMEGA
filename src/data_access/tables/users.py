from datetime import date


class Users:
    """Class representing a user."""

    def __init__(self, id: int, first_name: str, last_name: str, date_of_birth: date, email: str, phone: str,
                 address: str):
        """
        Initializes a Users instance.

        Parameters:
            id (int): The unique identifier for the user.
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            date_of_birth (date): The date of birth of the user.
            email (str): The email address of the user.
            phone (str): The phone number of the user.
            address (str): The address of the user.

        Raises:
            ValueError: If id is negative.
        """
        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        """Return a string representation of the Users instance."""
        message = (f"id: {self.id}, name: {self.first_name} {self.last_name}, date of birth: {self.date_of_birth}, "
                   f"contact: {self.email} or {self.phone} or {self.address}")
        return message
