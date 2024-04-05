import sys

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class MainScene:

    def __init__(self, logic):
        self.logic = logic

        self.root = ctk.CTk()
        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Library Management")
        self.root.geometry("875x500")
        self.root.resizable(False, False)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure((2, 3), weight=0)
        self.root.grid_rowconfigure(0, weight=1)
        self.components()

    def components(self):
        #sidebar
        self.buttons_frame = ctk.CTkFrame(self.root, width=175, corner_radius=15)
        self.buttons_frame.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nsew")
        self.buttons_frame.grid(row=0, column=0, sticky="nsew")
        self.buttons_frame.grid_rowconfigure(9, weight=1)

        self.borrowings = ctk.CTkButton(self.buttons_frame, text="Borrowings", command=None)
        self.borrowings.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="ew")

        self.create_borrowings = ctk.CTkButton(self.buttons_frame, text="Create borrowing", command=self.logic.create_borrowing)
        self.create_borrowings.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.add_user = ctk.CTkButton(self.buttons_frame, text="Add User", command=self.logic.add_user)
        self.add_user.grid(row=3, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.add_book = ctk.CTkButton(self.buttons_frame, text="Add book", command=self.logic.add_book)
        self.add_book.grid(row=4, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.create_book_copy = ctk.CTkButton(self.buttons_frame, text="Create book copy", command=self.logic.create_book_copy)
        self.create_book_copy.grid(row=5, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.add_author = ctk.CTkButton(self.buttons_frame, text="Add author", command=self.logic.add_author)
        self.add_author.grid(row=6, column=0, padx=20, pady=(30, 10), sticky="ew")

        self.add_genre = ctk.CTkButton(self.buttons_frame, text="Add genre", command=self.logic.add_genre)
        self.add_genre.grid(row=7, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.add_publisher = ctk.CTkButton(self.buttons_frame, text="Add publisher", command=self.logic.add_publisher)
        self.add_publisher.grid(row=8, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.log_out = ctk.CTkButton(self.buttons_frame, text="Log Out", command=self.logic.log_out)
        self.log_out.grid(row=10, column=0, padx=20, pady=(10, 10), sticky="ew")

        #main scene
        self.scene_frame = ctk.CTkScrollableFrame(self.root, width=700, corner_radius=15)
        self.scene_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    def mainloop(self):
        self.root.mainloop()

    def destroy(self):
        self.root.destroy()
