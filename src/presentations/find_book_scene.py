import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.data_access.daos.bookDAO import BookDAO
from src.data_access.tables.book import Book

class FindBookScene:

    def __init__(self, logic, database):
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()
        self.book_values = []

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add book")
        self.root.geometry("360x200")
        self.root.resizable(False, False)
        self.create_values()
        self.components()

    def components(self):
        self.add_book_lb = ctk.CTkLabel(self.root, text="Find book", font=('Open Sans', 25, 'bold'))
        self.add_book_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.title_label = ctk.CTkLabel(self.root, text="Enter title")
        self.title_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
        self.title_input = ctk.CTkComboBox(self.root, width=250, values=self.book_values)
        self.title_input.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))
        self.title_input.set("choose one")

        self.find_bk = ctk.CTkButton(self.root, text="Find book", command=self.find_book)
        self.find_bk.grid(row=4, column=0, columnspan=2, pady=50)

    def create_values(self):
        bkdao = BookDAO(self.database)
        his_bk = bkdao.read()
        self.book_values = [item[0] for item in his_bk]

    def check_for_input(self):
        if self.title_input.get() == "":
            return False
        return True


    def find_book(self):
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the fields")

            # add find book logic
            title = self.title_input.get()

            book = Book(
                id=0,
                genre_id=0,
                author_id=0,
                title=title
            )

            bookdao = BookDAO(self.database)
            books_info = bookdao.read_record(book)
            message = ""
            for record in books_info:
                book_title, first_name, last_name, shelf_no, floor = record
                message += \
                    f"Book {book_title}; Author: {first_name} {last_name}; shelf number: {shelf_no}, floor: {floor}\n"
            CTkMessagebox(
                title="Info",
                message=f"{message}",
                width=500)
            self.title_input.set("choose one")

        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"{e}",
                icon="cancel"
            )

    def mainloop(self):
        self.root.mainloop()
