import PyPDF2
from fpdf import FPDF
import webbrowser
import os

# Define the path for the image and output PDF
image_path =r"/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/image.png" #r"F:\\panag\\Documents\\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\\image.png"
pdf_path = r"/run/media/panos/SAMSUNG T7/panag/Documents/hello.pdf"

# Create a new PDF document
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font and size
pdf.set_font("Arial", size=15)

# Create a cell with text
pdf.cell(200, 10, txt="Hello, World!", ln=True, align='C')

# Add an image
pdf.image(image_path, x=10, y=50, w=100)

# Add a table
pdf.set_font("Arial", size=12)
pdf.cell(30, 10, txt="Column 1", border=1, align='C')
pdf.cell(30, 10, txt="Column 2", border=1, align='C')
pdf.ln(10)
pdf.cell(30, 10, txt="Row 1", border=1, align='C')
pdf.cell(30, 10, txt="Row 2", border=1, align='C')

# Add a link
pdf.link(10, 120, 50, 25, "https://www.example.com")

# Save the PDF file
pdf.output(pdf_path)

# Read the PDF to extract information
with open(pdf_path, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Get number of pages
    num_pages = len(pdf_reader.pages)
    print("Number of pages:", num_pages)

    # Extract text from the first page
    page_number = 0  # Replace with the desired page number
    page = pdf_reader.pages[page_number]
    text = page.extract_text()
    print(text)

    # Extract metadata
    metadata = pdf_reader.metadata
    print("Title:", metadata.get("/Title"))
    print("Author:", metadata.get("/Author"))

# Open the PDF file in the default web browser
webbrowser.open('file://' + os.path.abspath(pdf_path))
