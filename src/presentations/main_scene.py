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
        self.root.geometry("875x550")
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
        self.buttons_frame.grid_rowconfigure(10, weight=1)

        self.import_data = ctk.CTkButton(self.buttons_frame, text="Import json data", command=self.logic.import_file)
        self.import_data.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="ew")

        self.create_borrowings = ctk.CTkButton(self.buttons_frame, text="Create borrowing", command=self.logic.create_borrowing)
        self.create_borrowings.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.add_book = ctk.CTkButton(self.buttons_frame, text="Add book", command=self.logic.add_book)
        self.add_book.grid(row=3, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.add_book_shelf = ctk.CTkButton(self.buttons_frame, text="Add book to shelf", command=self.logic.add_book_shelf)
        self.add_book_shelf.grid(row=4, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.create_book_copy = ctk.CTkButton(self.buttons_frame, text="Create book copy", command=self.logic.create_book_copy)
        self.create_book_copy.grid(row=5, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.add_author = ctk.CTkButton(self.buttons_frame, text="Add author", command=self.logic.add_author)
        self.add_author.grid(row=6, column=0, padx=20, pady=(30, 10), sticky="ew")

        self.add_user = ctk.CTkButton(self.buttons_frame, text="Add User", command=self.logic.add_user)
        self.add_user.grid(row=7, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.add_genre = ctk.CTkButton(self.buttons_frame, text="Add genre", command=self.logic.add_genre)
        self.add_genre.grid(row=8, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.add_publisher = ctk.CTkButton(self.buttons_frame, text="Add publisher", command=self.logic.add_publisher)
        self.add_publisher.grid(row=9, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.log_out = ctk.CTkButton(self.buttons_frame, text="Log Out", command=self.logic.log_out)
        self.log_out.grid(row=11, column=0, padx=20, pady=(10, 10), sticky="ew")

        #main scene
        self.scene_frame = ctk.CTkScrollableFrame(self.root, width=700, label_text="All records", corner_radius=15)
        self.scene_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.tabview = ctk.CTkTabview(self.scene_frame)
        self.tabview.pack(fill="both", expand=1)
        self.tabview.add("Borrowed books")
        self.tabview.add("Books with author")
        self.tabview.add("Books with publisher")
        self.tabview.add("Books on shelves")
        self.tabview.add("User info")

        self.load_first_tab()
        self.load_second_tab()
        self.load_third_tab()
        self.load_fourth_tab()
        self.load_fifth_tab()

    def load_first_tab(self):
        first_tab = self.tabview.tab("Borrowed books")

        reload = ctk.CTkButton(first_tab, text="Reload history", command=self.load_first_tab)
        reload.grid(row=0, column=0, pady=(10, 10), sticky="w")

        history = self.logic.load_borrowed_books_data()
        for i, record in enumerate(history):
            label = f"{i+1} | ID:{record[0]}, {record[1]} {record[2]}, phone: {record[3]} | book: {record[4]}, borrowed/due: {record[5]}/{record[6]}"

            rec = ctk.CTkLabel(first_tab, text=label, font=('Arial', 13), fg_color="gray20", corner_radius=10)
            rec.grid(row=i+1, column=0, pady=(0, 15), sticky="nsew")
            rec.configure(anchor="w")

    def load_second_tab(self):
        second_tab = self.tabview.tab("Books with author")

        reload = ctk.CTkButton(second_tab, text="Reload history", command=self.load_second_tab)
        reload.grid(row=0, column=0, pady=(10, 10), sticky="w")

        history = self.logic.load_books_with_author_data()
        for i, record in enumerate(history):
            label = f"{i+1} | book: {record[0]} | author: {record[1]} {record[2]} | genre: {record[3]}"

            rec = ctk.CTkLabel(second_tab, text=label, font=('Arial', 14), fg_color="gray20", corner_radius=10)
            rec.grid(row=i+1, column=0, pady=(0, 15), sticky="nsew")
            rec.configure(anchor="w")

    def load_third_tab(self):
        third_tab = self.tabview.tab("Books with publisher")

        reload = ctk.CTkButton(third_tab, text="Reload history", command=self.load_third_tab)
        reload.grid(row=0, column=0, pady=(10, 10), sticky="w")

        history = self.logic.load_books_with_publisher_data()
        for i, record in enumerate(history):
            label = f"{i+1} | book: {record[0]} | date of publication: {record[1]} | publisher: {record[2]}"

            rec = ctk.CTkLabel(third_tab, text=label, font=('Arial', 14), fg_color="gray20", corner_radius=10)
            rec.grid(row=i+1, column=0, pady=(0, 15), sticky="nsew")
            rec.configure(anchor="w")

    def load_fourth_tab(self):
        fourth_tab = self.tabview.tab("Books on shelves")

        reload = ctk.CTkButton(fourth_tab, text="Reload history", command=self.load_fourth_tab)
        reload.grid(row=0, column=0, pady=(10, 10), sticky="w")

        find_book = ctk.CTkButton(fourth_tab, text="Find book", command=self.logic.find_book)
        find_book.grid(row=0, column=1, padx=(160, 0), pady=(10, 10), sticky="w")

        history = self.logic.load_books_on_shelves_data()
        for i, record in enumerate(history):
            label = f"{i+1} | book: {record[1]} | shelf number: {record[2]} floor number: {record[3]}"

            rec = ctk.CTkLabel(fourth_tab, text=label, font=('Arial', 14), fg_color="gray20", corner_radius=10)
            rec.grid(row=i+1, column=0, pady=(0, 15), sticky="nsew")
            rec.configure(anchor="w")

    def load_fifth_tab(self):
        fifth_tab = self.tabview.tab("User info")

        reload = ctk.CTkButton(fifth_tab, text="Reload history", command=self.load_fifth_tab)
        reload.grid(row=0, column=0, pady=(10, 10), sticky="w")

        history = self.logic.load_user_info_data()
        for i, record in enumerate(history):
            label = f"{i+1} | {record[0]} {record[1]} | contact: {record[2]}, {record[3]}, {record[4]}"

            rec = ctk.CTkLabel(fifth_tab, text=label, font=('Arial', 13), fg_color="gray20", corner_radius=10)
            rec.grid(row=i+1, column=0, pady=(0, 15), sticky="nsew")
            rec.configure(anchor="w")

    def mainloop(self):
        self.root.mainloop()

    def destroy(self):
        self.root.destroy()
