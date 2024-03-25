
class Admin:

    def __init__(self, id: int, users_id: int, role: str):

        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        if users_id < 0:
            raise ValueError("Users id must be a non-negative integer.")

        self.id = id
        self.users_id = users_id
        self.role = role