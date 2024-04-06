from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.author import Author

class AuthorDAO(IDao):

    def __init__(self, database: DatabaseConnection):
        super().__init__(database)

    def create(self, record: Author):
        try:
            msg = "Error with creating admin."
            query = """
                    INSERT INTO author(First_name, Last_name) VALUES(?,?)
                    """
            params = (record.first_name, record.last_name, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        try:
            msg = "No records."
            query = """
                    SELECT * FROM author
                    """
            self.database.select(query, msg)
        except Exception as e:
            raise Exception(e)

    def update(self, record: Author):
        try:
            msg = "Error with updating admin."
            query = """
                    UPDATE author SET First_name = ?, Last_name = ? WHERE ID = ?
                    """
            params = (record.first_name, record.last_name, record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Author):
        try:
            msg = "Error with deleting admin."
            query = """
                    DELETE FROM author WHERE First_name = ? and Last_name = ?
                    """
            params = (record.first_name, record.last_name,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)