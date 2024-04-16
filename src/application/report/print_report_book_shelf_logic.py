from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from src.data_access.daos.shelfDAO import ShelfDAO

class PrintReportBookShelfLogic:

    def __init__(self, database):
        self.database = database
        self.history = []

    def create_report(self):
        filename = f"books_shelf_summary.pdf"
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()
        title_style = styles['Title']
        body_style = styles['BodyText']
        elements = []

        elements.append(Paragraph("Books on shelf summary", title_style))
        elements.append(Spacer(1, 12))

        self.get_data()
        elements.extend(self.convert_data(body_style))

        doc.build(elements)

    def get_data(self):
        try:
            shelf_dao = ShelfDAO(self.database)
            self.history = shelf_dao.read()
        except Exception as e:
            self.history = []

    def convert_data(self, body_style):
        data_paragraphs = []
        for record in self.history:
            rec = f"ID: {record[0]} | book: {record[1]} | shelf number: {record[2]} floor number: {record[3]}"
            data_paragraphs.append(Paragraph(rec, body_style))
            data_paragraphs.append(Spacer(1, 12))
        return data_paragraphs