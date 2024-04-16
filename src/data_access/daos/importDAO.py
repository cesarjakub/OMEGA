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
        try:
            msg = "Error with creating book."
            query = """
                    INSERT INTO book(Genre_ID, Author_ID, Title) VALUES(?,?,?)
                    """
            params = (record.genre_id, record.author_id, record.title,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        msg = "No records."
        try:
            query = """
                            SELECT Title from book
                            """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg

    def update(self, record):
        try:
            msg = "Error with updating book."
            query = """
                    UPDATE book SET Genre_ID = ?, Author_ID = ?, Title = ? WHERE ID = ?
                    """
            params = (record.genre_id, record.author_id, record.title, record.id,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record):
        try:
            msg = "Error with deleting book."
            query = """
                    DELETE FROM book WHERE ID = ?
                    """
            params = (record.id,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)