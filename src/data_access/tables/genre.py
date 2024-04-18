
class Genre:
    """Class representing a genre."""

    def __init__(self, id: int, name: str):
        """
        Initializes a Genre instance.

        Parameters:
            id (int): The unique identifier for the genre.
            name (str): The name of the genre.

        Raises:
            ValueError: If id is negative.
        """
        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        self.id = id
        self.name = name

    def __str__(self):
        """Return a string representation of the Genre instance."""
        message = f"id: {self.id}, name of genre: {self.name}"
        return message