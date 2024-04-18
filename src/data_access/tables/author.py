
class Author:
    """Class representing an author."""

    def __init__(self, id: int, first_name: str, last_name: str):
        """
        Initializes an Author instance.

        Parameters:
            id (int): The unique identifier for the author.
            first_name (str): The first name of the author.
            last_name (str): The last name of the author.

        Raises:
            ValueError: If id is negative.
        """
        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        """Return a string representation of the Author instance."""
        message = f"id: {self.id}, full name: {self.first_name} {self.last_name}"
        return message

