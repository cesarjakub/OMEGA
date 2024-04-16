import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.data_access.daos.countDAO import CountDAO

class NumbersScene:

    def __init__(self, logic, database):
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()
        self.book_count = 0
        self.users_count = 0
        self.borrowing_count = 0

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add book")
        self.root.geometry("360x200")
        self.root.resizable(False, False)
        self.get_data()
        self.components()

    def components(self):
        self.add_book_lb = ctk.CTkLabel(self.root, text="Total numbers", font=('Open Sans', 25, 'bold'))
        self.add_book_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.total_books_label = ctk.CTkLabel(self.root, text=f"Number of books: {self.book_count}")
        self.total_books_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))

        self.total_users_label = ctk.CTkLabel(self.root, text=f"Number of users: {self.users_count}")
        self.total_users_label.grid(row=2, column=0, padx=(10, 5), pady=(10, 5))

        self.total_borrowed_books_label = ctk.CTkLabel(self.root, text=f"number of borrowed books: {self.borrowing_count}")
        self.total_borrowed_books_label.grid(row=3, column=0, padx=(10, 5), pady=(10, 5))

    def get_data(self):
        countdao = CountDAO(self.database)
        bk = countdao.count_book()
        self.book_count = str(bk)

        usr = countdao.count_users()
        self.users_count = str(usr)

        bor = countdao.count_borrowing()
        self.borrowing_count = str(bor)

    def mainloop(self):
        self.root.mainloop()
