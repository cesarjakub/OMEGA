
class Publisher:

    def __init__(self, id: int, name: str):

        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        self.id = id
        self.name = name

    def __str__(self):
        message = f"id: {self.id}, name of publisher: {self.name}"
        return message