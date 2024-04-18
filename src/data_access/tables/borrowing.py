from datetime import date
class Borrowing:
    """Class representing a borrowing record."""

    def __init__(self, id: int, book_id: int, users_id: int, date_borrowed: date, due_date: date):
        """
        Initializes a Borrowing instance.

        Parameters:
            id (int): The unique identifier for the borrowing record.
            book_id (int): The unique identifier for the borrowed book.
            users_id (int): The unique identifier for the user who borrowed the book.
            date_borrowed (date): The date when the book was borrowed.
            due_date (date): The due date for returning the borrowed book.

        Raises:
            ValueError: If id, book_id, or users_id is negative.
        """
        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        if book_id < 0:
            raise ValueError("Book id must be a non-negative integer.")

        if users_id < 0:
            raise ValueError("Users id must be a non-negative integer.")

        self.id = id
        self.book_id = book_id
        self.users_id = users_id
        self.date_borrowed = date_borrowed
        self.due_date = due_date

    def __str__(self):
        """Return a string representation of the Borrowing instance."""
        message = (f"id: {self.id}, book id: {self.book_id}, user id: {self.users_id}, "
                   f"date og borrowing: {self.date_borrowed}, due date: {self.due_date}")
        return message