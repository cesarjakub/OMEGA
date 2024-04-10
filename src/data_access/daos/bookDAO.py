from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.book import Book
from src.data_access.tables.genre import Genre
from src.data_access.tables.author import Author

class BookDAO(IDao):

    def __init__(self, database: DatabaseConnection):
        super().__init__(database)

    def create(self, record: Book):
        try:
            msg = "Error with creating book."
            query = """
                    INSERT INTO book(Genre_ID, Author_ID, Title) VALUES(?,?,?)
                    """
            params = (record.genre_id, record.author_id, record.title, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        try:
            msg = "No records."
            query = """
                    SELECT * FROM book
                    """
            self.database.select(query, msg)
        except Exception as e:
            raise Exception(e)

    def update(self, record: Book):
        try:
            msg = "Error with updating book."
            query = """
                    UPDATE book SET Genre_ID = ?, Author_ID = ?, Title = ? WHERE ID = ?
                    """
            params = (record.genre_id, record.author_id, record.title, record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Book):
        try:
            msg = "Error with deleting book."
            query = """
                    DELETE FROM book WHERE ID = ?
                    """
            params = (record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def insert_record(self, book: Book, genre: Genre, author: Author):
        try:
            msg = "Error with creating book."
            query = """
                    EXEC Add_book ?,?,?,?;
                    """
            params = (genre.name, author.first_name, author.last_name, book.title, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read_record(self, book: Book):
        try:
            msg = "Error with reading book."
            query = """
                    EXEC Find_book ?;
                    """
            params = (book.title, )
            books_info = self.database.select_with_params(query, params, msg)
            return books_info
        except Exception as e:
            raise Exception(e)