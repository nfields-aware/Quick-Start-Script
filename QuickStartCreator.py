#Install PyMuPDF: pip3 install PyMuPDF

import fitz  # PyMuPDF

# Path to template pdf. Just keep the template in the same folder as this script.
pdf_file_path = "AwareID-QuickStartGuide-Template.pdf"

# Customer Name for Final File
customer_name = input("Enter Customer Name: ")

# Open the PDF 
pdf_document = fitz.open(pdf_file_path)

# Page Select 
page = pdf_document[0]

# User Inputs
admin_portal_url = input("Admin Portal URL= ")
password = input("Password= ")
qr_url = input("QR-URL= ")

# Admin Portal Coordinates
admin_x, admin_y, admin_width, admin_height = (52, 294, 400, 20)

# Password Coordinates
password_x, password_y, password_width, password_height = (77, 320, 400, 20) 

# QR Coordinates
qr_x, qr_y, qr_width, qr_height = (69, 600, 400, 20)

# Insert the Admin Portal URL 
page.insert_textbox(
    fitz.Rect(admin_x, admin_y, admin_x + admin_width, admin_y + admin_height),
    admin_portal_url,
    fontsize=10,
    fontname="Helvetica",
    color=(0, 0, 0),  # Text color (black)
    align=0  # Text alignment (left)
)

# Insert the Password
page.insert_textbox(
    fitz.Rect(password_x, password_y, password_x + password_width, password_y + password_height),
    password,
    fontsize=10,
    fontname="Helvetica",
    color=(0, 0, 0),  # Text color (black)
    align=0  # Text alignment (left)
)

# Insert the QR-URL
page.insert_textbox(
    fitz.Rect(qr_x, qr_y, qr_x + qr_width, qr_y + qr_height),
    qr_url,
    fontsize=10,
    fontname="Helvetica",
    color=(0, 0, 0),  # Text color (black)
    align=0  # Text alignment (left)
)

# Save the modified PDF with the customer name appended to the filename
output_pdf_path = f"{customer_name}_AwareID-QuickStartGuide.pdf"
pdf_document.save(output_pdf_path)

# Close the PDF
pdf_document.close()

print(f"PDF with Customer Name appended and input prompts saved as {output_pdf_path}")
