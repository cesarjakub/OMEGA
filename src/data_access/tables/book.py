
class Book:

    def __init__(self, id: int, genre_id: int, author_id: int, title: str):

        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        if genre_id < 0:
            raise ValueError("Id must be a non-negative integer.")

        if author_id < 0:
            raise ValueError("Id must be a non-negative integer.")

        self.id = id
        self.genre_id = genre_id
        self.author_id = author_id
        self.title = title