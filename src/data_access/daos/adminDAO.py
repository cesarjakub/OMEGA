from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.admin import Admin

class AdminDAO(IDao):

    def __init__(self, database: DatabaseConnection):
        super().__init__(database)

    def create(self, record: Admin):
        pass

    def read(self):
        pass

    def update(self, record: Admin):
        pass

    def delete(self, record: Admin):
        pass

    def read_with_params(self, email, password):
        try:
            query = """
                    SELECT Email, Password FROM users INNER JOIN admin ON users.ID = admin.Users_ID 
                    WHERE users.Email = ? AND admin.Password = ?
                    """
            params = (email, password, )
            self.database.select_with_params(query, params)
        except Exception as e:
            raise Exception(e)