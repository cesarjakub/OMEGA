import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog
from src.data_access.daos.importDAO import ImportDAO
import json

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
            self.selected_file_label.configure(anchor="center")

            self.import_bt = ctk.CTkButton(self.root, text="Import", command=self.import_logic)
            self.import_bt.grid(row=1, column=0, columnspan=2, pady=50)
        else:
            CTkMessagebox(title="Error", message=f"Please select file")
            
    def import_logic(self):
        try:
            # import logic
            data = self.read_data()
            import_data = ImportDAO(self.database)

            for imp in data:
                import_data.import_data(imp['title'], imp['Author_first_name'], imp['Author_last_name'], imp['genre'], imp['publisher'], imp['shelf_number'], imp['floor_number'])

            self.file_path = None
            self.selected_file_label.configure(text="Please select file", padx=68)
            CTkMessagebox(title="Info", message=f"Data imported successfully", width=500)
        except Exception as e:
            CTkMessagebox(title="Error", message=f"{e}", icon="cancel")

    def read_data(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def mainloop(self):
        self.root.mainloop()