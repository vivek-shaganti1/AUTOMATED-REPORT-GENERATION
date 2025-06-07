from fpdf import FPDF
import csv
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 102, 204)  # Blue color
        self.cell(0, 10, 'Sample Data Report', align='C', ln=True)
        self.ln(10)
    def table_header(self):
        self.set_fill_color(0, 102, 204)  # Blue background
        self.set_text_color(255, 255, 255)  # White text
        self.set_font('Arial', 'B', 12)
        self.cell(60, 10, 'Name', border=1, fill=True)
        self.cell(30, 10, 'Age', border=1, fill=True)
        self.cell(60, 10, 'City', border=1, fill=True)
        self.ln()
    def table_row(self, name, age, city, fill):
        self.set_fill_color(224, 235, 255)  # Light blue fill
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 12)
        self.cell(60, 10, name, border=1, fill=fill)
        self.cell(30, 10, age, border=1, fill=fill)
        self.cell(60, 10, city, border=1, fill=fill)
        self.ln()
def generate_pdf_report(csv_file, output_pdf):
    pdf = PDFReport()
    pdf.add_page()

    # Add table header
    pdf.table_header()

    # Read CSV data and add rows
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        fill = False
        for row in reader:
            pdf.table_row(row['Name'], row['Age'], row['City'], fill)
            fill = not fill

    pdf.output(output_pdf)
    print(f"PDF generated successfully: {output_pdf}")

if __name__ == "__main__":
    generate_pdf_report('sample_data.csv', 'report_fpdf.pdf')
