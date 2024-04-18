
class Publisher:
    """Class representing a publisher."""

    def __init__(self, id: int, name: str):
        """
        Initializes a Publisher instance.

        Parameters:
            id (int): The unique identifier for the publisher.
            name (str): The name of the publisher.

        Raises:
            ValueError: If id is negative.
        """
        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        self.id = id
        self.name = name

    def __str__(self):
        """Return a string representation of the Publisher instance."""
        message = f"id: {self.id}, name of publisher: {self.name}"
        return message