from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.book_copy import BookCopy
from src.data_access.tables.publisher import Publisher
from src.data_access.tables.book import Book


class BookCopyDAO(IDao):

    def __init__(self, database: DatabaseConnection):
        super().__init__(database)

    def create(self, record: BookCopy):
        try:
            msg = "Error with creating book copy."
            query = """
                    INSERT INTO book_copy(Book_ID, Publisher_ID, Date_of_publication) 
                    VALUES (?, ?, GETDATE())
                    """
            params = (record.book_id, record.publisher_id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        try:
            msg = "No records."
            query = """
                    SELECT * FROM book_copy
                    """
            self.database.select(query, msg)
        except Exception as e:
            raise Exception(e)

    def update(self, record: BookCopy):
        try:
            msg = "Error with updating book copy."
            query = """
                    UPDATE book_copy SET Book_ID = ?, Publisher_ID = ? WHERE ID = ?
                    """
            params = (record.book_id, record.publisher_id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: BookCopy):
        try:
            msg = "Error with deleting book copy."
            query = """
                    DELETE FROM book_copy WHERE ID = ?
                    """
            params = (record.id,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def insert_record(self, book: Book, publisher: Publisher):
        try:
            msg = "Error with creating book copy."
            query = """
                    EXEC Create_book_copy ?,?;
                    """
            params = (book.title, publisher.name,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)
