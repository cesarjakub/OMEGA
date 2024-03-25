
class Genre:

    def __init__(self, id: int, name: str):

        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        self.id = id
        self.name = name