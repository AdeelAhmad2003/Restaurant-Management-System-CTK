import tkinter as tk
from tkinter import ttk
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class PrintTreeViewApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Print TreeView Data")
        
        # Create TreeView
        self.tree = ttk.Treeview(master)
        self.tree.pack(expand=True, fill=tk.BOTH)
        
        # Insert some sample data into the TreeView
        self.tree.insert("", "end", text="Parent", iid="parent")
        self.tree.insert("parent", "end", text="Child 1")
        self.tree.insert("parent", "end", text="Child 2")
        self.tree.insert("parent", "end", text="Child 3")
        
        # Button to print TreeView data
        self.print_button = tk.Button(master, text="Print", command=self.print_tree_data)
        self.print_button.pack()

    def print_tree_data(self):
        # Get TreeView data
        data_to_print = []
        for item in self.tree.get_children():
            data_to_print.append(self.tree.item(item)["text"])
        
        # Generate PDF
        pdf_file = "treeview_data.pdf"
        self.create_pdf(pdf_file, data_to_print)
        
        # Open PDF with default application (e.g., PDF viewer with printing capability)
        os.system(pdf_file)

    def create_pdf(self, file_name, data):
        c = canvas.Canvas(file_name, pagesize=letter)
        text = "\n".join(data)
        c.drawString(100, 750, text)
        c.save()

# Create the Tkinter application window
root = tk.Tk()
app = PrintTreeViewApp(root)
root.mainloop()
