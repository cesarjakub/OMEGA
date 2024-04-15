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
        msg = "No records."
        try:
            query = """
                    SELECT * FROM Books_author_genre
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg

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

    def read_records(self):
        msg = "No records."
        try:
            query = """
                    SELECT First_name FROM author;
                    """
            first_name_history = self.database.select(query, msg)
            return first_name_history
        except Exception as e:
            return msg

    def read_records_two(self):
        msg = "No records."
        try:
            query = """
                    SELECT Last_name FROM author;
                    """
            last_name_history = self.database.select(query, msg)
            return last_name_history
        except Exception as e:
            return msg