from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.genre import Genre

class GenreDAO(IDao):

    def __init__(self, database: DatabaseConnection):
        super().__init__(database)

    def create(self, record: Genre):
        try:
            msg = "Error with creating genre."
            query = """
                    INSERT INTO genre(Name) VALUES(?)
                    """
            params = (record.name, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        msg = "No records."
        try:
            query = """
                    SELECT Name FROM genre
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg

    def update(self, record: Genre):
        try:
            msg = "Error with updating genre."
            query = """
                    UPDATE genre SET Name = ? WHERE ID = ?
                    """
            params = (record.name, record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Genre):
        try:
            msg = "Error with deleting genre."
            query = """
                    DELETE FROM genre WHERE Name = ?
                    """
            params = (record.name,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)