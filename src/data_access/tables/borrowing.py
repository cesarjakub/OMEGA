from datetime import date
class Borrowing:

    def __init__(self, id: int, book_id: int, users_id: int, date_borrowed: date, due_date: date):

        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        if book_id < 0:
            raise ValueError("Id must be a non-negative integer.")

        if users_id < 0:
            raise ValueError("Id must be a non-negative integer.")

        self.id = id
        self.book_id = book_id
        self.users_id = users_id
        self.date_borrowed = date_borrowed
        self.due_date = due_date