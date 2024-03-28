from src.data_access.daos.idao import IDao
from src.data_access.tables.users import Users

class UsersDAO(IDao):

    def __init__(self):
        super().__init__()

    def create(self, record):
        pass

    def read(self):
        pass

    def update(self, record):
        pass

    def delete(self, record):
        pass