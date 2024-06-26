import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import re
from src.application.event_logger.EventLogger import EventLogger
from src.data_access.daos.usersDAO import UsersDAO
from src.data_access.tables.users import Users
from datetime import datetime

class DeleteUser:
    """A scene for deleting a user."""

    def __init__(self, logic, database):
        """
        Initializes the DeleteUser scene.

        Parameters:
            logic (Logic): An instance of the application's logic class.
            database: An instance of the application's database.
        """
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()
        self.el = EventLogger("./logs/log.txt")
        self.email_values = []

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add book")
        self.root.geometry("360x200")
        self.root.resizable(False, False)
        self.create_values()
        self.components()

    def components(self):
        """Creates and places GUI components for deleting a user."""
        self.del_book_lb = ctk.CTkLabel(self.root, text="Delete book", font=('Open Sans', 25, 'bold'))
        self.del_book_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.id_label = ctk.CTkLabel(self.root, text="Enter ID")
        self.id_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
        self.email_input = ctk.CTkComboBox(self.root, width=250, values=self.email_values)
        self.email_input.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))
        self.email_input.set("choose one")

        self.find_bk = ctk.CTkButton(self.root, text="DELETE", command=self.delete_borrowing)
        self.find_bk.grid(row=4, column=0, columnspan=2, pady=50)

    def check_for_input(self):
        """Checks if the user has entered an email."""
        if self.email_input.get() == "":
            return False
        return True

    def check_email(self, email):
        """Checks if the entered email has a valid format."""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return True
        else:
            return False

    def create_values(self):
        """Retrieves user emails from the database."""
        usrdao = UsersDAO(self.database)
        his_usr = usrdao.read_record()
        emails = [item[0] for item in his_usr]
        self.email_values = [str(i) for i in emails]

    def delete_borrowing(self):
        """Handles the process of deleting a user."""
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the fields")

            try:
                email = str(self.email_input.get())
            except ValueError:
                raise Exception("Please enter string")

            if not self.check_email(email):
                raise Exception("Please enter correct email format")

            user = Users(
                id=0,
                first_name="",
                last_name="",
                date_of_birth=datetime.now().date(),
                email=email,
                phone="",
                address=""
            )

            userdao = UsersDAO(self.database)
            userdao.delete(user)

            CTkMessagebox(
                title="Info",
                message=f"Record with id {self.email_input.get()} has been deleted",
                width=500,
                icon="check"
            )
            self.email_input.set("choose one")
            self.el.log_event("User deleted", "Success")
        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"{e}",
                icon="cancel"
            )
            self.el.log_event("Error -> User deleted", "Error")

    def mainloop(self):
        """Starts the main event loop for the DeleteUser scene."""
        self.root.mainloop()
