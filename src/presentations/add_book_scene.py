import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import re
from src.application.event_logger.EventLogger import EventLogger
from src.data_access.daos.bookDAO import BookDAO
from src.data_access.daos.genreDAO import GenreDAO
from src.data_access.daos.authorDAO import AuthorDAO
from src.data_access.tables.book import Book
from src.data_access.tables.author import Author
from src.data_access.tables.genre import Genre

class AddBookScene:

    def __init__(self, logic, database):
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()
        self.el = EventLogger("./logs/log.txt")
        self.genre_values = []
        self.author_last = []
        self.author_first = []
        self.book_values = []

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add book")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.create_values()
        self.components()

    def components(self):
        self.add_book_lb = ctk.CTkLabel(self.root, text="Add book", font=('Open Sans', 25, 'bold'))
        self.add_book_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.genre_label = ctk.CTkLabel(self.root, text="Enter genre")
        self.genre_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
        self.genre_input = ctk.CTkComboBox(self.root, width=250, values=self.genre_values)
        self.genre_input.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))
        self.genre_input.set("choose one")

        self.first_label = ctk.CTkLabel(self.root, text="Author first name")
        self.first_label.grid(row=2, column=0, padx=(10, 5), pady=(5, 5))
        self.first_input = ctk.CTkComboBox(self.root, width=250, values=self.author_first)
        self.first_input.grid(row=2, column=1, padx=(5, 10), pady=(5, 5))
        self.first_input.set("choose one")

        self.last_label = ctk.CTkLabel(self.root, text="Author last name")
        self.last_label.grid(row=3, column=0, padx=(10, 5), pady=(5, 5))
        self.last_input = ctk.CTkComboBox(self.root, width=250, values=self.author_last)
        self.last_input.grid(row=3, column=1, padx=(5, 10), pady=(5, 5))
        self.last_input.set("choose one")

        self.title_label = ctk.CTkLabel(self.root, text="Enter title")
        self.title_label.grid(row=4, column=0, padx=(10, 5), pady=(5, 10))
        self.title_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Title...")
        self.title_input.grid(row=4, column=1, padx=(5, 10), pady=(5, 10))

        self.add_bk = ctk.CTkButton(self.root, text="Add book", command=self.add_book)
        self.add_bk.grid(row=5, column=0, columnspan=2, pady=50)

    def create_values(self):
        gendao = GenreDAO(self.database)
        his_gen = gendao.read()
        self.genre_values = [item[0] for item in his_gen]

        authdao = AuthorDAO(self.database)
        his_ath = authdao.read_records()
        author_first_names = [item[0] for item in his_ath]
        self.author_first = list(set(author_first_names))

        authdao_two = AuthorDAO(self.database)
        his_ath_two = authdao_two.read_records_two()
        author_last_names = [item[0] for item in his_ath_two]
        self.author_last = list(set(author_last_names))

    def check_for_input(self):
        if (self.genre_input.get() == "" or self.first_input.get() == "" or self.last_input.get() == "" or
                self.title_input.get() == ""):
            return False
        return True

    def add_book(self):
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the fields")

            # add book logic
            name = self.genre_input.get().lower()
            first_name = self.first_input.get()
            last_name = self.last_input.get()
            title = self.title_input.get()

            if not re.match(r'^[a-zA-Z]+$', name):
                raise Exception("Genre name can only contain letters")

            if not re.match(r'^[a-zA-Z]+$', first_name):
                raise Exception("First name can only contain letters")

            if not re.match(r'^[a-zA-Z]+$', last_name):
                raise Exception("Last name can only contain letters")

            if not re.match(r'^[a-zA-Z\s]+$', title):
                raise Exception("Title can only contain letters")

            if not 2 < len(name) < 50:
                raise Exception("Genre is incorrect")

            if not 2 < len(first_name) < 20:
                raise Exception("Name is incorrect")

            if not 2 < len(last_name) < 20:
                raise Exception("Name is incorrect")

            if not 1 < len(name) < 100:
                raise Exception("Title is incorrect")

            genre = Genre(
                id=0,
                name=name
            )
            author = Author(
                id=0,
                first_name=first_name,
                last_name=last_name
            )
            book = Book(
                id=0,
                genre_id=genre.id,
                author_id=author.id,
                title=title
            )

            bookdao = BookDAO(self.database)
            bookdao.insert_record(book, genre, author)

            CTkMessagebox(
                title="Success",
                message=f"Book {self.title_input.get()} added successfully!",
                icon="check"
            )
            self.genre_input.set("choose one")
            self.first_input.set("choose one")
            self.last_input.set("choose one")
            self.title_input.delete(0, "end")
            self.el.log_event("Book added", "Success")
        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"{e}",
                icon="cancel"
            )
            self.el.log_event("Error -> Author added", "Error")

    def mainloop(self):
        self.root.mainloop()