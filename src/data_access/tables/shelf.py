
class Shelf:
    """Class representing a shelf."""

    def __init__(self, id: int, book_id: int, shelf_no: int, floor: int):
        """
        Initializes a Shelf instance.

        Parameters:
            id (int): The unique identifier for the shelf.
            book_id (int): The id of the book placed on the shelf.
            shelf_no (int): The shelf number.
            floor (int): The floor number where the shelf is located.

        Raises:
            ValueError: If any of the parameters is negative.
        """
        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        if book_id < 0:
            raise ValueError("Book id must be a non-negative integer.")

        if shelf_no < 0:
            raise ValueError("Shelf number must be a non-negative integer.")

        if floor < 0:
            raise ValueError("Floor number must be a non-negative integer.")

        self.id = id
        self.book_id = book_id
        self.shelf_no = shelf_no
        self.floor = floor

    def __str__(self):
        """Return a string representation of the Shelf instance."""
        message = f"id: {self.id}, book id: {self.book_id}, shelf number: {self.shelf_no}, floor: {self.floor}"
        return message