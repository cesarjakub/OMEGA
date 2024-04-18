import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import re
from src.application.event_logger.EventLogger import EventLogger
from src.data_access.daos.genreDAO import GenreDAO
from src.data_access.tables.genre import Genre

class AddGenreScene:

    def __init__(self, logic, database):
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()
        self.el = EventLogger("./logs/log.txt")

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add genre")
        self.root.geometry("350x200")
        self.root.resizable(False, False)
        self.components()

    def components(self):
        self.add_genre_lb = ctk.CTkLabel(self.root, text="Add genre", font=('Open Sans', 25, 'bold'))
        self.add_genre_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.genre_label = ctk.CTkLabel(self.root, text="Enter name")
        self.genre_label.grid(row=1, column=0, padx=(10, 5), pady=(25, 5))
        self.genre_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Name of genre...")
        self.genre_input.grid(row=1, column=1, padx=(5, 10), pady=(25, 5))

        self.add_gen = ctk.CTkButton(self.root, text="Add genre", command=self.add_genre)
        self.add_gen.grid(row=5, column=0, columnspan=2, pady=40)

    def check_for_input(self):
        if self.genre_input.get() == "":
            return False
        return True

    def add_genre(self):
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the field")

            # genre logic
            name = self.genre_input.get().lower()

            if not re.match(r'^[a-zA-Z\s]+$', name):
                raise Exception("Name can only contain letters")

            if not 2 < len(name) < 50:
                raise Exception("Genre is incorrect")

            genre = Genre(
                id=0,
                name=name
            )
            genredao = GenreDAO(self.database)
            genredao.create(genre)

            CTkMessagebox(
                title="Success",
                message=f"Genre {self.genre_input.get()} added successfully!",
                icon="check"
            )
            self.genre_input.delete(0, "end")
            self.el.log_event("Genre added", "Success")
        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"{e}",
                icon="cancel"
            )
            self.el.log_event("Error -> Genre added", "Error")

    def mainloop(self):
        self.root.mainloop()