import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class CreateBookCopyScene:

    def __init__(self, logic):
        self.logic = logic
        self.root = ctk.CTk()

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add book copy")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        self.components()

    def components(self):
        self.add_book_copy_lb = ctk.CTkLabel(self.root, text="Add book copy", font=('Open Sans', 25, 'bold'))
        self.add_book_copy_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.publisher_label = ctk.CTkLabel(self.root, text="Enter publisher name")
        self.publisher_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
        self.publisher_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Name...")
        self.publisher_input.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))

        self.title_label = ctk.CTkLabel(self.root, text="Enter book title")
        self.title_label.grid(row=2, column=0, padx=(10, 5), pady=(5, 5))
        self.title_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Book title...")
        self.title_input.grid(row=2, column=1, padx=(5, 10), pady=(5, 5))

        self.add_bkc = ctk.CTkButton(self.root, text="Add book copy", command=self.add_book_copy)
        self.add_bkc.grid(row=5, column=0, columnspan=2, pady=50)

    def check_for_input(self):
        if self.publisher_input.get() == "" or self.title_input.get() == "":
            return False
        return True

    def add_book_copy(self):
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the fields")

            # add book logic

            CTkMessagebox(title="Success", message=f"Book copy {self.title_input.get()} published by {self.publisher_input.get()} added successfully!", icon="check")
            self.publisher_input.delete(0, "end")
            self.title_input.delete(0, "end")

        except Exception as e:
            CTkMessagebox(title="Error", message=f"{e}", icon="cancel")

    def mainloop(self):
        self.root.mainloop()