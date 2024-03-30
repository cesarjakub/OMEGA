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
        self.root.mainloop()

    def components(self):
        #sidebar
        self.buttons_frame = ctk.CTkFrame(self.root, width=175, corner_radius=15)
        self.buttons_frame.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nsew")

        #main scene
        self.scene_frame = ctk.CTkScrollableFrame(self.root, width=700, corner_radius=15)
        self.scene_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
