import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.application.event_logger.EventLogger import EventLogger
from src.data_access.daos.borrowingDAO import BorrowingDAO
from src.data_access.tables.borrowing import Borrowing
from datetime import datetime

class DeleteBorrowingBook:
    """A scene for deleting a borrowing record."""

    def __init__(self, logic, database):
        """
        Initializes the DeleteBorrowingBook scene.

        Parameters:
            logic (Logic): An instance of the application's logic class.
            database: An instance of the application's database.
        """
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()
        self.el = EventLogger("./logs/log.txt")
        self.id_values = []

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add book")
        self.root.geometry("360x200")
        self.root.resizable(False, False)
        self.create_values()
        self.components()

    def components(self):
        """Creates and places GUI components for deleting a borrowing record."""
        self.del_book_lb = ctk.CTkLabel(self.root, text="Delete book", font=('Open Sans', 25, 'bold'))
        self.del_book_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.id_label = ctk.CTkLabel(self.root, text="Enter ID")
        self.id_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
        self.id_input = ctk.CTkComboBox(self.root, width=250, values=self.id_values)
        self.id_input.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))
        self.id_input.set("choose one")

        self.find_bk = ctk.CTkButton(self.root, text="DELETE", command=self.delete_borrowing)
        self.find_bk.grid(row=4, column=0, columnspan=2, pady=50)

    def check_for_input(self):
        """Checks if the user has entered an ID."""
        if self.id_input.get() == "":
            return False
        return True

    def check_for_number(self):
        """Checks if the entered ID is a positive number."""
        id_value = self.id_input.get()
        if id_value.isdigit() and int(id_value) > 0 and id_value in self.id_values:
            return True
        else:
            return False

    def create_values(self):
        """Retrieves borrowing record IDs from the database."""
        bordao = BorrowingDAO(self.database)
        his_bor = bordao.read_record()
        ids = [item[0] for item in his_bor]
        self.id_values = [str(i) for i in ids]

    def delete_borrowing(self):
        """Handles the process of deleting a borrowing record."""
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the fields")

            if not self.check_for_number():
                raise Exception("Please enter a positive number for ID or ID in range.")

            try:
                id = int(self.id_input.get())
            except ValueError:
                raise Exception("Please enter numbers")


            borrowing = Borrowing(
                id=id,
                book_id=0,
                users_id=0,
                date_borrowed=datetime.now().date(),
                due_date=datetime.now().date()
            )

            borrowingdao = BorrowingDAO(self.database)
            borrowingdao.delete(borrowing)

            CTkMessagebox(
                title="Info",
                message=f"Record with id {self.id_input.get()} has been deleted",
                width=500,
                icon="check"
            )
            self.id_input.set("choose one")
            self.el.log_event("Borrowing record deleted", "Success")
        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"{e}",
                icon="cancel"
            )
            self.el.log_event("Error -> Borrowing record deleted", "Error")

    def mainloop(self):
        """Starts the main event loop for the DeleteBorrowingBook scene."""
        self.root.mainloop()
