import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.lib.units import inch

from src.data_access.tables.book import Book
from src.data_access.tables.users import Users
from src.data_access.tables.borrowing import Borrowing

class PrintReportLogic:

    def __init__(self, book_table: Book, users_table: Users, borrowing_table: Borrowing, database):
        self.book_table = book_table
        self.users_table = users_table
        self.borrowing_table = borrowing_table
        self.database = database

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

    def create_pdf(self):
        filename = f"report{self.borrowing_table.id}.pdf"
        folder_path = "/OMEGA/reports"

        doc = SimpleDocTemplate(f"{folder_path}/{filename}", pagesize=letter)

        book_info = [
            ["Book Information"],
            ["Title:", self.book_table.title],
        ]
        user_info = [
            ["User Information"],
            ["First Name:", self.users_table.first_name],
            ["Last Name:", self.users_table.last_name],
            ["Phone:", self.users_table.phone]
        ]
        borrowing_info = [
            ["Borrowing Information"],
            ["Date Borrowed:", str(self.borrowing_table.date_borrowed)],
            ["Due Date:", str(self.borrowing_table.due_date)]
        ]

        book_table = Table(book_info)
        user_table = Table(user_info)
        borrowing_table = Table(borrowing_info)

        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        book_table.setStyle(style)
        user_table.setStyle(style)
        borrowing_table.setStyle(style)

        content = [book_table, user_table, borrowing_table]

        doc.build(content)
