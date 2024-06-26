import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import re
from src.application.event_logger.EventLogger import EventLogger
from src.data_access.daos.shelfDAO import ShelfDAO
from src.data_access.daos.bookDAO import BookDAO
from src.data_access.tables.shelf import Shelf
from src.data_access.tables.book import Book

class AddBookShelfScene:
    """A scene for adding a book to a shelf in the system."""

    def __init__(self, logic, database):
        """
        Initializes the AddBookShelfScene.

        Parameters:
            logic (Logic): An instance of the application's logic class.
            database (DatabaseConnection): An instance of the database connection class.
        """
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()
        self.el = EventLogger("./logs/log.txt")
        self.book_values = []

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add book")
        self.root.geometry("400x275")
        self.root.resizable(False, False)
        self.create_values()
        self.components()

    def components(self):
        """Creates and places GUI components for the AddBookShelfScene."""
        self.add_book_lb = ctk.CTkLabel(self.root, text="Add book to shelf", font=('Open Sans', 25, 'bold'))
        self.add_book_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.title_label = ctk.CTkLabel(self.root, text="Enter title")
        self.title_label.grid(row=1, column=0, padx=(10, 5), pady=(5, 5))
        self.title_input = ctk.CTkComboBox(self.root, width=250, values=self.book_values)
        self.title_input.grid(row=1, column=1, padx=(5, 10), pady=(5, 5))
        self.title_input.set("choose one")

        self.shelf_no_label = ctk.CTkLabel(self.root, text="Shelf number")
        self.shelf_no_label.grid(row=2, column=0, padx=(10, 5), pady=(5, 5))
        self.shelf_no_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Shelf number...")
        self.shelf_no_input.grid(row=2, column=1, padx=(5, 10), pady=(5, 5))

        self.floor_label = ctk.CTkLabel(self.root, text="Floor number")
        self.floor_label.grid(row=3, column=0, padx=(10, 5), pady=(5, 5))
        self.floor_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Floor number...")
        self.floor_input.grid(row=3, column=1, padx=(5, 10), pady=(5, 5))

        self.add_bk = ctk.CTkButton(self.root, text="Add book to shelf", command=self.add_book_shelf)
        self.add_bk.grid(row=4, column=0, columnspan=2, pady=50)

    def create_values(self):
        """Creates initial values for book selection."""
        bkdao = BookDAO(self.database)
        his_bk = bkdao.read()
        self.book_values = [item[0] for item in his_bk]

    def check_for_input(self):
        """Checks if all required input fields are filled."""
        if self.title_input.get() == "" or self.shelf_no_input.get() == "" or self.floor_input.get() == "":
            return False
        return True

    def validate_positive_integer(self, value):
        """
        Validates if a given value is a positive integer.

        Parameters:
            value (str): The value to be validated.

        Returns:
            bool: True if the value is a positive integer, False otherwise.
        """
        return value.isdigit() and int(value) > 0

    def check_for_number(self):
        """
        Checks if the shelf and floor numbers are positive integers.

        Returns:
            bool: True if both shelf and floor numbers are positive integers, False otherwise.
        """
        shelf_no_value = self.shelf_no_input.get()
        if not self.validate_positive_integer(shelf_no_value):
            return False

        floor_value = self.floor_input.get()
        if not self.validate_positive_integer(floor_value):
            return False

        return True

    def add_book_shelf(self):
        """Adds a new book to a shelf."""
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the fields")

            if not self.check_for_number():
                raise Exception("Please enter a positive integer.")

            # add book to shelf logic
            title = self.title_input.get()
            try:
                floor_no = int(self.floor_input.get())
                shelf_no = int(self.shelf_no_input.get())
            except ValueError:
                raise Exception("Please enter numbers")

            if not re.match(r'^[a-zA-Z\s]+$', title):
                raise Exception("Title can only contain letters")

            if not 1 < len(title) < 100:
                raise Exception("Title is incorrect")

            book = Book(
                id=0,
                author_id=0,
                genre_id=0,
                title=title
            )

            shelf = Shelf(
                id=0,
                book_id=0,
                shelf_no=shelf_no,
                floor=floor_no
            )

            shelfdao = ShelfDAO(self.database)
            shelfdao.insert_record(shelf, book)

            CTkMessagebox(
                title="Success",
                message=f"Book {self.title_input.get()} added successfully!",
                icon="check"
            )
            self.title_input.set("choose one")
            self.shelf_no_input.delete(0, "end")
            self.floor_input.delete(0, "end")
            self.el.log_event("Book on shelf added", "Success")
        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"{e}",
                icon="cancel"
            )
            self.el.log_event("Error -> Book on shelf added", "Error")

    def mainloop(self):
        """Starts the main event loop for the AddBookShelfScene."""
        self.root.mainloop()