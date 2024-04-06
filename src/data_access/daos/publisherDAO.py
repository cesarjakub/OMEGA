from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.publisher import Publisher

class PublisherDAO(IDao):

    def __init__(self, database: DatabaseConnection):
        super().__init__(database)

    def create(self, record: Publisher):
        try:
            msg = "Error with creating publisher."
            query = """
                    INSERT INTO publisher(Name) VALUES(?)
                    """
            params = (record.name, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        pass

    def update(self, record: Publisher):
        pass

    def delete(self, record: Publisher):
        pass