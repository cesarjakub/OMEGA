import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.data_access.daos.countDAO import CountDAO

class NumbersScene:
    """A scene to display total numbers of books, users, and borrowed books."""

    def __init__(self, logic, database):
        """
        Initializes the NumbersScene.

        Parameters:
            logic (Logic): An instance of the application's logic class.
            database (DatabaseConnection): An instance of the database connection class.
        """
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
        """Creates and places GUI components for the NumbersScene."""
        self.add_book_lb = ctk.CTkLabel(self.root, text="Total numbers", font=('Open Sans', 25, 'bold'))
        self.add_book_lb.grid(row=0, column=0, columnspan=2, padx=(70,0), pady=10)

        self.total_books_label = ctk.CTkLabel(self.root, fg_color="gray20", corner_radius=8, text=f"Number of books:")
        self.total_books_label.grid(row=1, column=0, padx=(70, 5), pady=(10, 5))

        self.total_books_cn = ctk.CTkLabel(self.root, text=f"{self.book_count}")
        self.total_books_cn.grid(row=1, column=1, padx=(10, 5), pady=(10, 5))

        self.total_users_label = ctk.CTkLabel(self.root, fg_color="gray20", corner_radius=8, text=f"Number of users:")
        self.total_users_label.grid(row=2, column=0, padx=(70, 5), pady=(10, 5))

        self.total_users_cn = ctk.CTkLabel(self.root, text=f"{self.users_count}")
        self.total_users_cn.grid(row=2, column=1, padx=(10, 5), pady=(10, 5))

        self.total_borrowed_books_label = ctk.CTkLabel(self.root, fg_color="gray20", corner_radius=8, text=f"number of borrowed books:")
        self.total_borrowed_books_label.grid(row=3, column=0, padx=(70, 5), pady=(10, 5))

        self.total_borrowed_books_cn = ctk.CTkLabel(self.root, text=f"{self.borrowing_count}")
        self.total_borrowed_books_cn.grid(row=3, column=1, padx=(10, 5), pady=(10, 5))


    def get_data(self):
        """Retrieves data from the database."""
        countdao = CountDAO(self.database)
        bk = countdao.count_book()
        bkc = [item[0] for item in bk]
        self.book_count = str(bkc)

        usr = countdao.count_users()
        usrc = [item[0] for item in usr]
        self.users_count = str(usrc)

        bor = countdao.count_borrowing()
        borc = [item[0] for item in bor]
        self.borrowing_count = borc

    def mainloop(self):
        """Starts the main event loop for the NumbersScene."""
        self.root.mainloop()
