import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class AddBookScene:

    def __init__(self, logic):
        self.logic = logic
        self.root = ctk.CTk()

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add book")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.components()

    def components(self):
        self.add_book_lb = ctk.CTkLabel(self.root, text="Add book", font=('Open Sans', 25, 'bold'))
        self.add_book_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.genre_label = ctk.CTkLabel(self.root, text="Enter genre")
        self.genre_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
        self.genre_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Genre...")
        self.genre_input.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))

        self.first_label = ctk.CTkLabel(self.root, text="Author first name")
        self.first_label.grid(row=2, column=0, padx=(10, 5), pady=(5, 5))
        self.first_input = ctk.CTkEntry(self.root, width=250, placeholder_text="First name...")
        self.first_input.grid(row=2, column=1, padx=(5, 10), pady=(5, 5))

        self.last_label = ctk.CTkLabel(self.root, text="Author last name")
        self.last_label.grid(row=3, column=0, padx=(10, 5), pady=(5, 5))
        self.last_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Last name...")
        self.last_input.grid(row=3, column=1, padx=(5, 10), pady=(5, 5))

        self.title_label = ctk.CTkLabel(self.root, text="Enter title")
        self.title_label.grid(row=4, column=0, padx=(10, 5), pady=(5, 10))
        self.title_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Title...")
        self.title_input.grid(row=4, column=1, padx=(5, 10), pady=(5, 10))

        self.add_bk = ctk.CTkButton(self.root, text="Add book", command=self.add_book)
        self.add_bk.grid(row=5, column=0, columnspan=2, pady=50)

    def check_for_input(self):
        if self.genre_input.get() == "" or self.first_input.get() == "" or self.last_input.get() == "" or self.title_input.get() == "":
            return False
        return True

    def add_book(self):
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the fields")

            # add book logic

            CTkMessagebox(title="Success", message=f"Book {self.title_input.get()} added successfully!", icon="info")
            self.genre_input.delete(0, "end")
            self.first_input.delete(0, "end")
            self.last_input.delete(0, "end")
            self.title_input.delete(0, "end")
        except Exception as e:
            CTkMessagebox(title="Error", message=f"{e}", icon="cancel")

    def mainloop(self):
        self.root.mainloop()