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

    def import_file(self):
        import_file_sc = ImportFileScene(self, self.database)
        import_file_sc.mainloop()

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

    def numbers(self):
        numbers_sc = NumbersScene(self, self.database)
        numbers_sc.mainloop()

    def log_out(self):
        self.main_sc.destroy()
        self.start()

    # load history
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

    # delete record
    def delete_borrowed_books_data(self):
        delete_borrowing_book_sc = DeleteBorrowingBook(self, self.database)
        delete_borrowing_book_sc.mainloop()

    def delete_book_from_shelf(self):
        delete_book_from_shelf_scene = DeleteBookFromShelf(self, self.database)
        delete_book_from_shelf_scene.mainloop()

    def delete_user(self):
        delete_user_Scene = DeleteUser(self, self.database)
        delete_user_Scene.mainloop()

    # create summary
    def create_report(self, book_table, users_table, borrowing_table):
        print_report = PrintReportLogic(book_table, users_table, borrowing_table, self.database)
        print_report.create_pdf()

    def create_report_books(self):
        print_report_book = PrintReportBookLogic(self.database)
        print_report_book.create_report()

    def create_report_users(self):
        print_report_users = PrintReportUsersLogic(self.database)
        print_report_users.create_report()

    def create_report_shelf(self):
        print_report_shelf = PrintReportBookShelfLogic(self.database)
        print_report_shelf.create_report()

    # name day
    def name_day(self):
        name_day_sc = NameDay(self, self.database)
        name = name_day_sc.get_name()
        return name