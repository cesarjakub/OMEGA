from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection

class ImportDAO(IDao):

    def __int__(self, database: DatabaseConnection):
        super().__init__(database)

    def import_data(self, Book_title, Author_first_name, Author_last_name, Genre_name, Publisher_name,
                    shelf_nu, floor_nu):
        try:
            msg = "Error while importing data."
            query = """
                    EXEC Import_data ?,?,?,?,?,?,?;
                    """
            params = (Book_title, Author_first_name, Author_last_name, Genre_name, Publisher_name, shelf_nu, floor_nu, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def create(self, record):
        pass

    def read(self):
        pass

    def update(self, record):
        pass

    def delete(self, record):
        pass