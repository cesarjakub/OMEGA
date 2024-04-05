import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class AddPublisherScene:

    def __init__(self, logic):
        self.logic = logic
        self.root = ctk.CTk()

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add publisher")
        self.root.geometry("350x200")
        self.root.resizable(False, False)
        self.components()

    def components(self):
        self.add_publisher_lb = ctk.CTkLabel(self.root, text="Add publisher", font=('Open Sans', 25, 'bold'))
        self.add_publisher_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.publisher_label = ctk.CTkLabel(self.root, text="Enter name")
        self.publisher_label.grid(row=1, column=0, padx=(10, 5), pady=(25, 5))
        self.publisher_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Name of publisher...")
        self.publisher_input.grid(row=1, column=1, padx=(5, 10), pady=(25, 5))

        self.add_pub = ctk.CTkButton(self.root, text="Add publisher", command=self.add_publisher)
        self.add_pub.grid(row=5, column=0, columnspan=2, pady=40)

    def check_for_input(self):
        if self.publisher_input.get() == "":
            return False
        return True

    def add_publisher(self):
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the field")

            # add publisher logic

            CTkMessagebox(title="Success", message=f"Publisher {self.publisher_input.get()} added successfully!", icon="check")
            self.publisher_input.delete(0, "end")

        except Exception as e:
            CTkMessagebox(title="Error", message=f"{e}", icon="cancel")

    def mainloop(self):
        self.root.mainloop()