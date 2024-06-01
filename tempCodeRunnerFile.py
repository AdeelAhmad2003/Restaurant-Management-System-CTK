def create_bill_pdf(file_name, app):
    import tkinter.messagebox
    try:
        from reportlab.pdfgen import canvas
    except ImportError:
        tkinter.messagebox.showerror("Error", "Reportlab library is required for PDF generation.")
        return

    c = canvas.Canvas(file_name, pagesize=reportlab.lib.pagesizes.letter)

    # Set the font for the entire document
    c.setFont("Helvetica", 12)

    # Write customer details to PDF
    cust_name = cust_name_entry.get()
    cust_address = cust_add_entry.get()
    cust_phone = cust_ph_entry.get()
    payment_method=payment_method_value.get()

    c.drawString(50, 770, "Customer Details:")
    c.drawString(100, 750, f"Customer Name: {cust_name}")
    c.drawString(100, 730, f"Customer Address: {cust_address}")
    c.drawString(100, 710, f"Customer Phone: {cust_phone}")
    c.drawString(100, 690, f"Date: {current_date}")
    c.drawString(100, 670, f"Time: {current_time}")

    # Write TreeView data from app.tree to PDF
    y = 650
    c.drawString(50, y, "Ordered Items:")
    for item in app.tree.get_children():
        data = app.tree.item(item, 'values')
        if data:
            c.drawString(70, y - 30, f"Item ID: {data[0]}")
            c.drawString(150, y - 30, f"Name: {data[1]}")
            c.drawString(250, y - 30, f"Price: {data[3]}")
            y -= 20

    # Write TreeView data from app.tree2 to PDF
    y -= 20
    c.drawString(50, y, "Order Details:")
    items = app.tree2.get_children()

    # Print Order ID, Customer ID, and Table Number only once
    data = app.tree2.item(items[0], 'values')
    c.drawString(100, y - 30, f"Order ID: {data[0]}")
    c.drawString(100, y - 50, f"Customer ID: {data[1]}")
    c.drawString(100, y - 70, f"Table No: {data[4]}")
    y -= 100  # Adjust y-coordinate for the next item

    # Print details for each item
    for item in items:
        data = app.tree2.item(item, 'values')
        if data:
            # Write each detail on a separate line
            c.drawString(70, y, f"Item ID: {data[2]}")
            c.drawString(150, y, f"Price: {data[6]}")
            y -= 20  # Adjust y-coordinate for the next item

    # Write payment details to PDF
    y -= 40  # Adjust y-coordinate for the payment details
    total_price = total_price_entry.get()
    tax = tax_entry.get()
    total_amount = total_amount_entry.get()
    c.drawString(50, y, "Payment Details:")
    c.drawString(100, y - 30, f"Total Price: {total_price}")
    c.drawString(100, y - 50, f"Tax: {tax}%")
    c.drawString(100, y - 70, f"Total Amount: {total_amount}")
    c.drawString(100, y - 90, f"Payment Method: {payment_method}")

    c.showPage()
    c.save()
def print_bill(app):
    # Create a PDF file
    pdf_file = "bill.pdf"
    create_bill_pdf(pdf_file, app)

    # Open the PDF file with the default application
    open_pdf_with_default_app(pdf_file)

def open_pdf_with_default_app(file_name):
    import os
    os.system(file_name)