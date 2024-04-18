import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import re
from src.application.event_logger.EventLogger import EventLogger
from src.data_access.daos.authorDAO import AuthorDAO
from src.data_access.tables.author import Author


class AddAuthorScene:
    """
    Represents a scene for adding an author in the application.

    Attributes:
        logic (Logic): The logic layer of the application.
        database (DatabaseConnection): The database connection object.
        root (ctk.CTk): The root window of the scene.
        el (EventLogger): The event logger for logging events.
        add_author_lb (ctk.CTkLabel): The label for the title of the scene.
        first_label (ctk.CTkLabel): The label for the first name input field.
        first_input (ctk.CTkEntry): The entry field for entering the first name.
        last_label (ctk.CTkLabel): The label for the last name input field.
        last_input (ctk.CTkEntry): The entry field for entering the last name.
        add_auth (ctk.CTkButton): The button for adding the author.

    Methods:
        __init__(self, logic, database): Initializes the AddAuthorScene object.
        components(self): Sets up the GUI components for the scene.
        check_for_input(self): Checks if the input fields are empty.
        add_author(self): Adds the author to the database and handles input validation.
        mainloop(self): Starts the event loop to display the GUI.
    """

    def __init__(self, logic, database):
        """
        Initializes the AddAuthorScene object.

        Args:
            logic (Logic): The logic layer of the application.
            database (DatabaseConnection): The database connection object.
        """
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()
        self.el = EventLogger("./logs/log.txt")

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add author")
        self.root.geometry("375x250")
        self.root.resizable(False, False)
        self.components()

    def components(self):
        """
        Sets up the GUI components for the scene.
        """
        self.add_author_lb = ctk.CTkLabel(self.root, text="Add author", font=('Open Sans', 25, 'bold'))
        self.add_author_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.first_label = ctk.CTkLabel(self.root, text="Author first name")
        self.first_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
        self.first_input = ctk.CTkEntry(self.root, width=250, placeholder_text="First name...")
        self.first_input.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))

        self.last_label = ctk.CTkLabel(self.root, text="Author last name")
        self.last_label.grid(row=2, column=0, padx=(10, 5), pady=(5, 10))
        self.last_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Last name...")
        self.last_input.grid(row=2, column=1, padx=(5, 10), pady=(5, 10))

        self.add_auth = ctk.CTkButton(self.root, text="Add author", command=self.add_author)
        self.add_auth.grid(row=5, column=0, columnspan=2, pady=50)

    def check_for_input(self):
        """
        Checks if the input fields are empty.

        Returns:
            bool: True if the input fields are not empty, False otherwise.
        """
        if self.first_input.get() == "" or self.last_input.get() == "":
            return False
        return True

    def add_author(self):
        """
        Adds the author to the database and handles input validation.
        """
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the fields")

            # add author logic
            first_name = self.first_input.get()
            last_name = self.last_input.get()

            if not re.match(r'^[a-zA-Z.]+$', first_name):
                raise Exception("First name can only contain letters")

            if not re.match(r'^[a-zA-Z.]+$', last_name):
                raise Exception("Last name can only contain letters")

            if not 2 < len(first_name) < 20:
                raise Exception("Name is incorrect")

            if not 2 < len(last_name) < 20:
                raise Exception("Name is incorrect")

            author = Author(
                id=0,
                first_name=first_name,
                last_name=last_name
            )
            authordao = AuthorDAO(self.database)
            authordao.create(author)

            CTkMessagebox(
                title="Success",
                message=f"Author {self.first_input.get()} {self.last_input.get()} added successfully!",
                icon="check"
            )
            self.first_input.delete(0, "end")
            self.last_input.delete(0, "end")
            self.el.log_event("Author added", "Success")
        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"{e}",
                icon="cancel"
            )
            self.el.log_event("Error -> Author added", "Error")

    def mainloop(self):
        """
        Starts the event loop to display the GUI.
        """
        self.root.mainloop()