import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

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
        path = f"my_qrcode_{self.borrowing_table.id}.png"
        img.save(path)
        return path

    def create_pdf(self):
        filename = f"report{self.borrowing_table.id}.pdf"

        qr_code_path = self.create_qr_code()

        doc = SimpleDocTemplate(filename, pagesize=letter)

        styles = getSampleStyleSheet()
        title_style = styles['Title']
        body_style = styles['BodyText']

        elements = []

        elements.append(Paragraph("Borrowing Report", title_style))
        elements.append(Spacer(1, 12))

        elements.append(Paragraph(f"User: {self.users_table.first_name} {self.users_table.last_name}", body_style))
        elements.append(Paragraph(f"Book Title: {self.book_table.title}", body_style))
        elements.append(Paragraph(f"Date Borrowed: {self.borrowing_table.date_borrowed}", body_style))
        elements.append(Paragraph(f"Due Date: {self.borrowing_table.due_date}", body_style))
        elements.append(Spacer(1, 12))

        qr_code = Image(qr_code_path, width=200, height=200)
        elements.append(qr_code)

        doc.build(elements)

