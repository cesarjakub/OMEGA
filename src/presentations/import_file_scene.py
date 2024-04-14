import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog

class ImportFileScene:

    def __init__(self, logic, database):
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add book")
        self.root.geometry("350x200")
        self.root.resizable(False, False)
        self.components()

    def components(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json")],
            title="Choose a JSON file"
        )
        if self.file_path:
            self.selected_file_label = ctk.CTkLabel(self.root, text=self.file_path, fg_color="gray20", corner_radius=10)
            self.selected_file_label.grid(row=0, column=0, padx=(50, 50), columnspan=2, pady=(20, 0))

            self.import_bt = ctk.CTkButton(self.root, text="Import", command=self.import_logic)
            self.import_bt.grid(row=1, column=0, columnspan=2, pady=50)
        else:
            CTkMessagebox(title="Error", message=f"Please select file")

    def import_logic(self):
        pass

    def mainloop(self):
        self.root.mainloop()