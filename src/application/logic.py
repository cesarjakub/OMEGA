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
from src.presentations.import_file_scene import ImportFileScene
from src.presentations.delete_borrowed_book_scene import DeleteBorrowingBook
from src.presentations.delete_book_shelf_scene import DeleteBookFromShelf
from src.presentations.delete_user_scene import DeleteUser
from src.presentations.numers_scene import NumbersScene

from src.application.name_day_logic import NameDay
from src.application.summary.print_summary_logic import PrintReportLogic
from src.application.summary.print_summary_book_logic import PrintReportBookLogic
from src.application.summary.print_summary_users_logic import PrintReportUsersLogic
from src.application.summary.print_summary_book_shelf_logic import PrintReportBookShelfLogic

from src.data_access.daos.borrowingDAO import BorrowingDAO
from src.data_access.daos.authorDAO import AuthorDAO
from src.data_access.daos.publisherDAO import PublisherDAO
from src.data_access.daos.shelfDAO import ShelfDAO
from src.data_access.daos.usersDAO import UsersDAO

class Logic:
    """A class representing the logic layer of the application."""

    def __init__(self, database):
        """
        Initializes a Logic instance.

        Parameters:
            database: The database object used throughout the application.
        """
        self.database = database
        self.main_sc = None
        self.start()

    # login logic
    def start(self):
        """Starts the application by initiating the login scene."""
        login = LoginScene(logic=self)
        login.mainloop()

    def login(self, email, password):
        """
        Logs in a user.

        Parameters:
            email (str): The user's email.
            password (str): The user's password.

        Raises:
            Exception: If an error occurs during the login process.
        """
        try:
            login_logic = LoginLogic(self.database)
            login_logic.login(email, password)
        except Exception as e:
            raise Exception(e)

    #main logic
    def main_scene(self):
        """Displays the main scene of the application."""
        self.main_sc = MainScene(self)
        self.main_sc.mainloop()

    def import_file(self):
        """Displays the file window."""
        import_file_sc = ImportFileScene(self, self.database)
        import_file_sc.mainloop()

    def find_book(self):
        """Displays the find book window."""
        find_book_sc = FindBookScene(self, self.database)
        find_book_sc.mainloop()

    def create_borrowing(self):
        """Displays window for creating borrowings."""
        create_borrowing_sc = CreateBorrowingScene(self, self.database)
        create_borrowing_sc.mainloop()

    def add_user(self):
        """Displays window for adding users."""
        add_user_sc = AddUserScene(self, self.database)
        add_user_sc.mainloop()

    def add_book(self):
        """Displays window for adding books."""
        add_book_sc = AddBookScene(self, self.database)
        add_book_sc.mainloop()

    def add_book_shelf(self):
        """Displays window for adding books into shelf."""
        add_book_shelf_sc = AddBookShelfScene(self, self.database)
        add_book_shelf_sc.mainloop()

    def create_book_copy(self):
        """Displays window for creating book copy."""
        create_book_copy_sc = CreateBookCopyScene(self, self.database)
        create_book_copy_sc.mainloop()

    def add_author(self):
        """Displays window for adding book author."""
        add_author_sc = AddAuthorScene(self, self.database)
        add_author_sc.mainloop()

    def add_genre(self):
        """Displays window for adding genre."""
        add_genre_sc = AddGenreScene(self, self.database)
        add_genre_sc.mainloop()

    def add_publisher(self):
        """Displays window for adding publisher."""
        add_publisher_sc = AddPublisherScene(self, self.database)
        add_publisher_sc.mainloop()

    def numbers(self):
        """Displays window showing numbers."""
        numbers_sc = NumbersScene(self, self.database)
        numbers_sc.mainloop()

    def log_out(self):
        """Function that will log you out from the app."""
        self.main_sc.destroy()
        self.start()

    # load history
    def load_borrowed_books_data(self):
        """Function for loading data (borrowings) from database."""
        load_borrowed_books = BorrowingDAO(self.database)
        history = load_borrowed_books.read()
        return history

    def load_books_with_author_data(self):
        """Function for loading data (books with authors) from database."""
        load_books_with_author = AuthorDAO(self.database)
        history = load_books_with_author.read()
        return history

    def load_books_with_publisher_data(self):
        """Function for loading data (books with publishers) from database."""
        load_books_with_publisher = PublisherDAO(self.database)
        history = load_books_with_publisher.read()
        return history

    def load_books_on_shelves_data(self):
        """Function for loading data (books on shelf) from database."""
        load_books_on_shelves = ShelfDAO(self.database)
        history = load_books_on_shelves.read()
        return history

    def load_user_info_data(self):
        """Function for loading data (users) from database."""
        load_user_info = UsersDAO(self.database)
        history = load_user_info.read()
        return history

    # delete record
    def delete_borrowed_books_data(self):
        """Function for deleting data (borrowed books) from database."""
        delete_borrowing_book_sc = DeleteBorrowingBook(self, self.database)
        delete_borrowing_book_sc.mainloop()

    def delete_book_from_shelf(self):
        """Function for deleting data (books from shelf) from database."""
        delete_book_from_shelf_scene = DeleteBookFromShelf(self, self.database)
        delete_book_from_shelf_scene.mainloop()

    def delete_user(self):
        """Function for deleting data (user) from database."""
        delete_user_Scene = DeleteUser(self, self.database)
        delete_user_Scene.mainloop()

    # create summary
    def create_report(self, book_table, users_table, borrowing_table):
        """Function for creating report (borrowing)."""
        print_report = PrintReportLogic(book_table, users_table, borrowing_table, self.database)
        print_report.create_pdf()

    def create_report_books(self):
        """Function for creating report books."""
        print_report_book = PrintReportBookLogic(self.database)
        print_report_book.create_report()

    def create_report_users(self):
        """Function for creating report (users)."""
        print_report_users = PrintReportUsersLogic(self.database)
        print_report_users.create_report()

    def create_report_shelf(self):
        """Function for creating report (books on shelf)."""
        print_report_shelf = PrintReportBookShelfLogic(self.database)
        print_report_shelf.create_report()

    # name day
    def name_day(self):
        """
        Retrieves today's name from an API.

        Returns:
            str: The name associated with today's date.
        """
        name_day_sc = NameDay(self, self.database)
        name = name_day_sc.get_name()
        return name