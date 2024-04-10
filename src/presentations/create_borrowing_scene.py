import datetime

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.data_access.daos.borrowingDAO import BorrowingDAO
from src.data_access.tables.borrowing import Borrowing
from src.data_access.tables.book import Book
from src.data_access.tables.users import Users


class CreateBorrowingScene:

    def __init__(self, logic, database):
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Create borrowing")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.components()

    def components(self):
        self.add_borrowing_lb = ctk.CTkLabel(self.root, text="Create borrowing", font=('Open Sans', 25, 'bold'))
        self.add_borrowing_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.title_label = ctk.CTkLabel(self.root, text="Enter title")
        self.title_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
        self.title_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Title...")
        self.title_input.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))

        self.first_label = ctk.CTkLabel(self.root, text="User first name")
        self.first_label.grid(row=2, column=0, padx=(10, 5), pady=(5, 5))
        self.first_input = ctk.CTkEntry(self.root, width=250, placeholder_text="First name...")
        self.first_input.grid(row=2, column=1, padx=(5, 10), pady=(5, 5))

        self.last_label = ctk.CTkLabel(self.root, text="User last name")
        self.last_label.grid(row=3, column=0, padx=(10, 5), pady=(5, 5))
        self.last_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Last name...")
        self.last_input.grid(row=3, column=1, padx=(5, 10), pady=(5, 5))

        self.borrowed_label = ctk.CTkLabel(self.root, text="Date of borrowing")
        self.borrowed_label.grid(row=4, column=0, padx=(10, 5), pady=(5, 5))
        self.borrowed_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Date...")
        self.borrowed_input.grid(row=4, column=1, padx=(5, 10), pady=(5, 5))

        self.due_label = ctk.CTkLabel(self.root, text="Due date")
        self.due_label.grid(row=5, column=0, padx=(10, 5), pady=(5, 10))
        self.due_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Date...")
        self.due_input.grid(row=5, column=1, padx=(5, 10), pady=(5, 10))

        self.add_borr = ctk.CTkButton(self.root, text="Create borrowing", command=self.create_borrowing)
        self.add_borr.grid(row=6, column=0, columnspan=2, pady=50)

    def check_for_input(self):
        if (self.title_input.get() == "" or self.first_input.get() == "" or self.last_input.get() == ""
                or self.borrowed_input.get() == "" or self.due_input.get() == ""):
            return False
        return True

    def create_borrowing(self):
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the fields")

            # create borrowing logic
            title = self.title_input.get()
            first_name = self.first_input.get()
            last_name = self.last_input.get()
            borrowed = self.borrowed_input.get()
            due = self.due_input.get()

            book = Book(
                id=0,
                genre_id=0,
                author_id=0,
                title=title
            )

            users = Users(
                id=0,
                first_name=first_name,
                last_name=last_name,
                date_of_birth=datetime.datetime.now().date(),
                email="",
                phone="",
                address=""
            )

            borrowing = Borrowing(
                id=0,
                book_id=0,
                users_id=0,
                date_borrowed=borrowed,
                due_date=due
            )
            borroweddao = BorrowingDAO(self.database)
            borroweddao.insert_record(borrowing, book, users)

            CTkMessagebox(title="Success", message=f"Borrowing {self.title_input.get()} for {self.first_input.get()} {self.last_input.get()} created successfully!",
                          icon="check")
            self.borrowed_input.delete(0, "end")
            self.due_input.delete(0, "end")
            self.first_input.delete(0, "end")
            self.last_input.delete(0, "end")
            self.title_input.delete(0, "end")

        except Exception as e:
            CTkMessagebox(title="Error", message=f"{e}", icon="cancel")

    def mainloop(self):
        self.root.mainloop()
