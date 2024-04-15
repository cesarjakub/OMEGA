
class Author:

    def __init__(self, id: int, first_name: str, last_name: str):

        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        message = f"id: {self.id}, full name: {self.first_name} {self.last_name}"
        return message

