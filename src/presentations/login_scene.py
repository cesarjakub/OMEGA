import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class LoginScene:

    def __init__(self, logic):
        self.logic = logic

        self.root = ctk.CTk()
        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Login")
        self.root.geometry("400x340")
        self.root.resizable(False, False)
        self.entry()
        self.root.mainloop()

    def entry(self):
        self.name_label = ctk.CTkLabel(self.root, text="Library Management", font=('Open Sans', 25, 'bold'))
        self.name_label.pack(pady=10)

        self.email_label = ctk.CTkLabel(self.root, text="Email")
        self.email_label.pack()

        self.email_entry = ctk.CTkEntry(self.root, width=300, placeholder_text="Email...")
        self.email_entry.pack(pady=5)

        self.password_label = ctk.CTkLabel(self.root, text="Password")
        self.password_label.pack()

        self.password_entry = ctk.CTkEntry(self.root, width=300, show="*", placeholder_text="Password...")
        self.password_entry.pack(pady=5)

        self.button()

    def button(self):
        self.submit = ctk.CTkButton(self.root, text="Submit", command=self.login_btn)
        self.submit.pack(pady=30)

    def login_btn(self):
        try:
            self.logic.login(self.email_entry.get(), self.password_entry.get(), "Email or password is wrong! Please try again.")
        except Exception as e:
            CTkMessagebox(title="Error", message=f"{e}", icon="cancel",)

