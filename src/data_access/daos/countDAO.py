from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection

class CountDAO(IDao):

    def __int__(self, database: DatabaseConnection):
        super().__init__(database)

    def count_book(self):
        msg = "0"
        try:
            query = """
                    SELECT COUNT(*) FROM book;
                    """
            book_count = self.database.select(query, msg)
            return book_count
        except Exception as e:
            return msg

    def count_users(self):
        msg = "0"
        try:
            query = """
                    SELECT COUNT(*) FROM users;
                    """
            users_count = self.database.select(query, msg)
            return users_count
        except Exception as e:
            return msg

    def count_borrowing(self):
        msg = "0"
        try:
            query = """
                    SELECT COUNT(*) FROM borrowing;
                    """
            borrowing_count = self.database.select(query, msg)
            return borrowing_count
        except Exception as e:
            return msg

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