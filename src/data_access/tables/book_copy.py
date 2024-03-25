from datetime import date
class BookCopy:

    def __init__(self, id: int, book_id: int, publisher_id: int, date_of_publication: date):

        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        if book_id < 0:
            raise ValueError("Id must be a non-negative integer.")

        if publisher_id < 0:
            raise ValueError("Id must be a non-negative integer.")

        self.id = id
        self.book_id = book_id
        self.publisher_id = publisher_id
        self.date_of_publication = date_of_publication