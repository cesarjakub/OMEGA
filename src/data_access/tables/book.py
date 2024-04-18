
class Book:
    """Class representing a book."""

    def __init__(self, id: int, genre_id: int, author_id: int, title: str):
        """
        Initializes a Book instance.

        Parameters:
            id (int): The unique identifier for the book.
            genre_id (int): The unique identifier for the genre of the book.
            author_id (int): The unique identifier for the author of the book.
            title (str): The title of the book.

        Raises:
            ValueError: If id, genre_id, or author_id is negative.
        """
        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        if genre_id < 0:
            raise ValueError("Genre id must be a non-negative integer.")

        if author_id < 0:
            raise ValueError("Author id must be a non-negative integer.")

        self.id = id
        self.genre_id = genre_id
        self.author_id = author_id
        self.title = title

    def __str__(self):
        """Return a string representation of the Book instance."""
        message = f"id: {self.id}, genre id: {self.genre_id}, authro id: {self.author_id}, title: {self.title}"
        return message