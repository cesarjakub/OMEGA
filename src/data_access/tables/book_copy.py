from datetime import date
class BookCopy:
    """Class representing a copy of a book."""

    def __init__(self, id: int, book_id: int, publisher_id: int, date_of_publication: date):
        """
        Initializes a BookCopy instance.

        Parameters:
            id (int): The unique identifier for the book copy.
            book_id (int): The unique identifier for the book associated with this copy.
            publisher_id (int): The unique identifier for the publisher of the book copy.
            date_of_publication (date): The date of publication of the book copy.

        Raises:
            ValueError: If id, book_id, or publisher_id is negative.
        """
        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        if book_id < 0:
            raise ValueError("Book id must be a non-negative integer.")

        if publisher_id < 0:
            raise ValueError("Publisher id must be a non-negative integer.")

        self.id = id
        self.book_id = book_id
        self.publisher_id = publisher_id
        self.date_of_publication = date_of_publication

    def __str__(self):
        """Return a string representation of the BookCopy instance."""
        message = (f"id: {self.id}, book id: {self.book_id}, publisher id: {self.publisher_id}, "
                   f"date of publication: {self.date_of_publication}")
        return message