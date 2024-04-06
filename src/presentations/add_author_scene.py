import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.data_access.daos.authorDAO import AuthorDAO
from src.data_access.tables.author import Author


class AddAuthorScene:

    def __init__(self, logic, database):
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add author")
        self.root.geometry("375x250")
        self.root.resizable(False, False)
        self.components()

    def components(self):
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
        if self.first_input.get() == "" or self.last_input.get() == "":
            return False
        return True

    def add_author(self):
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the fields")

            # add author logic
            first_name = self.first_input.get()
            last_name = self.last_input.get()

            author = Author(
                id=0,
                first_name=first_name,
                last_name=last_name
            )
            authordao = AuthorDAO(self.database)
            authordao.create(author)

            CTkMessagebox(title="Success", message=f"Author {self.first_input.get()} {self.last_input.get()} added successfully!", icon="check")
            self.first_input.delete(0, "end")
            self.last_input.delete(0, "end")

        except Exception as e:
            CTkMessagebox(title="Error", message=f"{e}", icon="cancel")

    def mainloop(self):
        self.root.mainloop()