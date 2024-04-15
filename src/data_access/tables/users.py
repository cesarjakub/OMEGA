from datetime import date


class Users:

    def __init__(self, id: int, first_name: str, last_name: str, date_of_birth: date, email: str, phone: str,
                 address: str):
        if id < 0:
            raise ValueError("Id must be a non-negative integer.")

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        message = (f"id: {self.id}, name: {self.first_name} {self.last_name}, date of birth: {self.date_of_birth}, "
                   f"contact: {self.email} or {self.phone} or {self.address}")
        return message
