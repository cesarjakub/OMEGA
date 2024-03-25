
class Shelf:

    def __init__(self, id: int, book_id: int, shelf_no: int, floor: int):

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