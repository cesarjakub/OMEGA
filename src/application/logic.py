from src.presentations.login_scene import LoginScene
from src.application.login_logic import LoginLogic
from src.presentations.main_scene import MainScene
from src.presentations.add_book_scene import AddBookScene
from src.presentations.add_user_scene import AddUserScene
from src.presentations.add_publisher_scene import AddPublisherScene
from src.presentations.add_genre_scene import AddGenreScene
from src.presentations.add_author_scene import AddAuthorScene
from src.presentations.create_book_copy_scene import CreateBookCopyScene
from src.presentations.create_borrowing_scene import CreateBorrowingScene
from src.presentations.add_book_shelf_scene import AddBookShelfScene
from src.presentations.find_book_scene import FindBookScene

from src.data_access.daos.borrowingDAO import BorrowingDAO
from src.data_access.daos.authorDAO import AuthorDAO
from src.data_access.daos.publisherDAO import PublisherDAO
from src.data_access.daos.shelfDAO import ShelfDAO
from src.data_access.daos.usersDAO import UsersDAO

class Logic:

    def __init__(self, database):
        self.database = database
        self.main_sc = None
        #self.start()

    # login logic
    def start(self):
        login = LoginScene(logic=self)
        login.mainloop()

    def login(self, email, password):
        try:
            login_logic = LoginLogic(self.database)
            login_logic.login(email, password)
        except Exception as e:
            raise Exception(e)

    #main logic
    def main_scene(self):
        self.main_sc = MainScene(self)
        self.main_sc.mainloop()

    def find_book(self):
        find_book_sc = FindBookScene(self, self.database)
        find_book_sc.mainloop()

    def create_borrowing(self):
        create_borrowing_sc = CreateBorrowingScene(self, self.database)
        create_borrowing_sc.mainloop()

    def add_user(self):
        add_user_sc = AddUserScene(self, self.database)
        add_user_sc.mainloop()

    def add_book(self):
        add_book_sc = AddBookScene(self, self.database)
        add_book_sc.mainloop()

    def add_book_shelf(self):
        add_book_shelf_sc = AddBookShelfScene(self, self.database)
        add_book_shelf_sc.mainloop()

    def create_book_copy(self):
        create_book_copy_sc = CreateBookCopyScene(self, self.database)
        create_book_copy_sc.mainloop()

    def add_author(self):
        add_author_sc = AddAuthorScene(self, self.database)
        add_author_sc.mainloop()

    def add_genre(self):
        add_genre_sc = AddGenreScene(self, self.database)
        add_genre_sc.mainloop()

    def add_publisher(self):
        add_publisher_sc = AddPublisherScene(self, self.database)
        add_publisher_sc.mainloop()

    def log_out(self):
        self.main_sc.destroy()
        self.start()

    def load_borrowed_books_data(self):
        load_borrowed_books = BorrowingDAO(self.database)
        history = load_borrowed_books.read()
        return history

    def load_books_with_author_data(self):
        load_books_with_author = AuthorDAO(self.database)
        history = load_books_with_author.read()
        return history

    def load_books_with_publisher_data(self):
        load_books_with_publisher = PublisherDAO(self.database)
        history = load_books_with_publisher.read()
        return history

    def load_books_on_shelves_data(self):
        load_books_on_shelves = ShelfDAO(self.database)
        history = load_books_on_shelves.read()
        return history

    def load_user_info_data(self):
        load_user_info = UsersDAO(self.database)
        history = load_user_info.read()
        return history