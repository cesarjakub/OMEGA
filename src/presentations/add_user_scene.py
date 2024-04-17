import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from datetime import datetime
from src.application.event_loger.EventLoger import EventLoger
import re
from src.data_access.daos.usersDAO import UsersDAO
from src.data_access.tables.users import Users

class AddUserScene:

    def __init__(self, logic, database):
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()
        self.el = EventLoger("./logs/log.txt")

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add user")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.components()

    def components(self):
        self.add_user_lb = ctk.CTkLabel(self.root, text="Add user", font=('Open Sans', 25, 'bold'))
        self.add_user_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.first_label = ctk.CTkLabel(self.root, text="First name")
        self.first_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
        self.first_input = ctk.CTkEntry(self.root, width=250, placeholder_text="First name...")
        self.first_input.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))

        self.last_label = ctk.CTkLabel(self.root, text="Last name")
        self.last_label.grid(row=2, column=0, padx=(10, 5), pady=(5, 5))
        self.last_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Last name...")
        self.last_input.grid(row=2, column=1, padx=(5, 10), pady=(5, 5))

        self.birth_label = ctk.CTkLabel(self.root, text="Date of birth")
        self.birth_label.grid(row=3, column=0, padx=(10, 5), pady=(5, 5))
        self.birth_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Date of birth (YYYY-MM-DD)...")
        self.birth_input.grid(row=3, column=1, padx=(5, 10), pady=(5, 5))

        self.email_label = ctk.CTkLabel(self.root, text="Enter email")
        self.email_label.grid(row=4, column=0, padx=(10, 5), pady=(5, 5))
        self.email_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Email...")
        self.email_input.grid(row=4, column=1, padx=(5, 10), pady=(5, 5))

        self.phone_label = ctk.CTkLabel(self.root, text="Enter phone")
        self.phone_label.grid(row=5, column=0, padx=(10, 5), pady=(5, 5))
        self.phone_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Phone...")
        self.phone_input.grid(row=5, column=1, padx=(5, 10), pady=(5, 5))

        self.address_label = ctk.CTkLabel(self.root, text="Enter address")
        self.address_label.grid(row=6, column=0, padx=(10, 5), pady=(5, 10))
        self.address_input = ctk.CTkEntry(self.root, width=250, placeholder_text="address...")
        self.address_input.grid(row=6, column=1, padx=(5, 10), pady=(5, 10))

        self.add_usr = ctk.CTkButton(self.root, text="Add user", command=self.add_book)
        self.add_usr.grid(row=7, column=0, columnspan=2, pady=50)

    def check_for_input(self):
        if (self.first_input.get() == "" or self.last_input.get() == "" or self.birth_input.get() == ""
                or self.email_input.get() == "" or self.phone_input.get() == "" or self.address_input.get() == ""):
            return False

        return True

    def check_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return True
        else:
            return False

    def add_book(self):
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the fields")

            # add user logic
            first_name = self.first_input.get()
            last_name = self.last_input.get()
            try:
                date_of_birth = datetime.strptime(self.birth_input.get(), '%Y-%m-%d').date()
            except ValueError:
                raise ValueError("Incorrect date format, please enter date in YYYY-MM-DD format.")
            email = self.email_input.get()
            phone = self.phone_input.get()
            address = self.address_input.get()

            if not 2 < len(first_name) < 20:
                raise Exception("First name is incorrect")

            if not 2 < len(last_name) < 20:
                raise Exception("Last name is incorrect")

            if not 2 < len(email) < 50:
                raise Exception("Email is incorrect")

            if not 2 < len(phone) < 50:
                raise Exception("Phone is incorrect")

            if not 2 < len(address) < 100:
                raise Exception("Address is incorrect")

            if not self.check_email(email):
                raise Exception("Please enter correct email format")

            users = Users(
                id=0,
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                email=email,
                phone=phone,
                address=address
            )
            usersdao = UsersDAO(self.database)
            usersdao.create(users)

            CTkMessagebox(
                title="Success",
                message=f"User {self.first_input.get()} {self.last_input.get()} added successfully!",
                icon="check"
            )
            self.first_input.delete(0, "end")
            self.last_input.delete(0, "end")
            self.birth_input.delete(0, "end")
            self.email_input.delete(0, "end")
            self.phone_input.delete(0, "end")
            self.address_input.delete(0, "end")
            self.el.log_event("User added", "Success")
        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"{e}",
                icon="cancel"
            )
            self.el.log_event("Error -> User added", "Error")

    def mainloop(self):
        self.root.mainloop()