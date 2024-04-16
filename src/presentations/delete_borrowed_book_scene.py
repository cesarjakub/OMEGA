import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.data_access.daos.borrowingDAO import BorrowingDAO
from src.data_access.tables.borrowing import Borrowing
from datetime import datetime

class DeleteBorrowingBook:

    def __init__(self, logic, database):
        self.logic = logic
        self.database = database
        self.root = ctk.CTk()

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Dark")
        self.root.title("Add book")
        self.root.geometry("360x200")
        self.root.resizable(False, False)
        self.components()

    def components(self):
        self.del_book_lb = ctk.CTkLabel(self.root, text="Delete book", font=('Open Sans', 25, 'bold'))
        self.del_book_lb.grid(row=0, column=0, columnspan=2, pady=10)

        self.id_label = ctk.CTkLabel(self.root, text="Enter ID")
        self.id_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
        self.id_input = ctk.CTkEntry(self.root, width=250, placeholder_text="Enter id...")
        self.id_input.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))

        self.find_bk = ctk.CTkButton(self.root, text="DELETE", command=self.delete_borrowing)
        self.find_bk.grid(row=4, column=0, columnspan=2, pady=50)

    def check_for_input(self):
        if self.id_input.get() == "":
            return False
        return True

    def check_for_number(self):
        id_value = self.id_input.get()
        if id_value.isdigit() and int(id_value) > 0:
            return True
        else:
            return False

    def delete_borrowing(self):
        try:
            if not self.check_for_input():
                raise Exception("Please fill in the fields")

            if not self.check_for_number():
                raise Exception("Please enter a positive number for ID.")

            try:
                id = int(self.id_input.get())
            except ValueError:
                raise Exception("Please enter numbers")


            borrowing = Borrowing(
                id=id,
                book_id=0,
                users_id=0,
                date_borrowed=datetime.now().date(),
                due_date=datetime.now().date()
            )

            borrowingdao = BorrowingDAO(self.database)
            borrowingdao.delete(borrowing)

            CTkMessagebox(
                title="Info",
                message=f"Record with id {self.id_input.get()} has been deleted",
                width=500)
        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"{e}",
                icon="cancel"
            )

    def mainloop(self):
        self.root.mainloop()
