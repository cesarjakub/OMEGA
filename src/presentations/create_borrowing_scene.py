from datetime import datetime
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import re
from src.application.event_logger.EventLogger import EventLogger
from src.data_access.daos.borrowingDAO import BorrowingDAO
from src.data_access.daos.bookDAO import BookDAO
from src.data_access.daos.usersDAO import UsersDAO
from src.data_access.tables.borrowing import Borrowing
from src.data_access.tables.book import Book
from src.data_access.tables.users import Users


class CreateBorrowingScene:

    def __init__(self, logic, database):
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()
        self.el = EventLogger("./logs/log.txt")
        self.book_values = []
        self.first_name = []
        self.last_name = []

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Create borrowing")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.create_values()
        self.components()

    def components(self):
        self.add_borrowing_lb = ctk.CTkLabel(self.root, text="Create borrowing", font=('Open Sans', 25, 'bold'))
        self.add_borrowing_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.title_label = ctk.CTkLabel(self.root, text="Enter title")
        self.title_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
        self.title_input = ctk.CTkComboBox(self.root, width=250, values=self.book_values)
        self.title_input.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))
        self.title_input.set("choose one")

        self.first_label = ctk.CTkLabel(self.root, text="User first name")
        self.first_label.grid(row=2, column=0, padx=(10, 5), pady=(5, 5))
        self.first_input = ctk.CTkComboBox(self.root, width=250, values=self.first_name)
        self.first_input.grid(row=2, column=1, padx=(5, 10), pady=(5, 5))
        self.first_input.set("choose one")

        self.last_label = ctk.CTkLabel(self.root, text="User last name")
        self.last_label.grid(row=3, column=0, padx=(10, 5), pady=(5, 5))
        self.last_input = ctk.CTkComboBox(self.root, width=250, values=self.last_name)
        self.last_input.grid(row=3, column=1, padx=(5, 10), pady=(5, 5))
        self.last_input.set("choose one")

        self.borrowed_label = ctk.CTkLabel(self.root, text="Date of borrowing")
        self.borrowed_label.grid(row=4, column=0, padx=(10, 5), pady=(5, 5))
        self.borrowed_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Date (YYYY-MM-DD)...")
        self.borrowed_input.grid(row=4, column=1, padx=(5, 10), pady=(5, 5))

        self.due_label = ctk.CTkLabel(self.root, text="Due date")
        self.due_label.grid(row=5, column=0, padx=(10, 5), pady=(5, 10))
        self.due_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Date (YYYY-MM-DD)...")
        self.due_input.grid(row=5, column=1, padx=(5, 10), pady=(5, 10))

        self.add_borr = ctk.CTkButton(self.root, text="Create borrowing", command=self.create_borrowing)
        self.add_borr.grid(row=6, column=0, columnspan=2, pady=50)

    def create_values(self):
        bkdao = BookDAO(self.database)
        his_bk = bkdao.read()
        self.book_values = [item[0] for item in his_bk]

        first = UsersDAO(self.database)
        his_frs = first.read_first()
        self.first_name = [item[0] for item in his_frs]

        last = UsersDAO(self.database)
        his_lst = last.read_last()
        self.last_name = [item[0] for item in his_lst]



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
            try:
                borrowed = datetime.strptime(self.borrowed_input.get(), '%Y-%m-%d').date()
            except ValueError:
                raise ValueError("Incorrect date format, please enter date in YYYY-MM-DD format.")
            try:
                due = datetime.strptime(self.due_input.get(), '%Y-%m-%d').date()
            except ValueError:
                raise ValueError("Incorrect date format, please enter date in YYYY-MM-DD format.")

            if not re.match(r'^[a-zA-Z]+$', first_name):
                raise ValueError("First name can only contain letters")

            if not re.match(r'^[a-zA-Z]+$', last_name):
                raise ValueError("Last name can only contain letters")

            if not re.match(r'^[a-zA-Z\s]+$', title):
                raise ValueError("Title can only contain letters")

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
                date_of_birth=datetime.now().date(),
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

            CTkMessagebox(
                title="Success",
                message=f"Borrowing {self.title_input.get()} for {self.first_input.get()} {self.last_input.get()} "
                        f"created successfully!",
                icon="check")
            self.borrowed_input.delete(0, "end")
            self.due_input.delete(0, "end")
            self.first_input.set("choose one")
            self.last_input.set("choose one")
            self.title_input.set("choose one")
            self.el.log_event("Borrowing created", "Success")
        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"{e}",
                icon="cancel"
            )
            self.el.log_event("Error -> Borrowing created", "Error")


    def mainloop(self):
        self.root.mainloop()
