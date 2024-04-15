import qrcode

from src.data_access.tables.book import Book
from src.data_access.tables.users import Users
from src.data_access.tables.borrowing import Borrowing

class PrintReportLogic:

    def __init__(self, book_table: Book, users_table: Users, borrowing_table: Borrowing):
        self.book_table = book_table
        self.users_table = users_table
        self.borrowing_table = borrowing_table

    def create_qr_code(self):
        data = (f"{self.users_table.first_name} {self.users_table.last_name} phone: {self.users_table.phone}, "
                f"title: {self.book_table.title}, borrowed: {self.borrowing_table.date_borrowed} due date: {self.borrowing_table.due_date}")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("my_qrcode.png")