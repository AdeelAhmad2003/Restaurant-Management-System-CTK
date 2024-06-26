from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import customtkinter as ctk
from tkinter import ttk
import pyodbc
from menu import MenuFile
from employee import employeeFile
from inventory import inventoryFile
from sales import salesFile

def setup_ui(app, connection):
    main_frame = CTkFrame(master=app, fg_color="#2A8C55", width=1200, height=670, corner_radius=0)
    main_frame.pack_propagate(0)
    main_frame.pack(fill="y", anchor="w", side="left")

    logo_img_data = Image.open("logo.png")
    logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))

    label1 = CTkLabel(master=main_frame, text="Welcome!!!", text_color="#eee", fg_color="transparent", font=("Arial Bold", 25), anchor="w")
    label1.pack(pady=(38, 10), anchor="n")

    # Create a frame to hold the buttons and ensure they are aligned properly
    button_frame = CTkFrame(master=main_frame, fg_color="transparent")
    button_frame.pack(pady=(50, 10), anchor="center")  # Increased top padding

    menu_img_data = Image.open("menu.png")
    menu_img = CTkImage(dark_image=menu_img_data, light_image=menu_img_data, size=(100, 100))

    menu = CTkButton(master=button_frame, image=menu_img, text="Menu Management", fg_color="transparent", font=("Arial Bold", 25), hover_color="#207244", anchor="center", command=lambda: open_menu(app, connection))
    menu.pack(side='left', padx=10)

    employee_img_data = Image.open("employees.png")
    employee_img = CTkImage(dark_image=employee_img_data, light_image=employee_img_data, size=(100, 100))

    employee = CTkButton(master=button_frame, image=employee_img, text="Employee Management", fg_color="transparent", font=("Arial Bold", 25), hover_color="#207244", anchor="center", command=lambda: open_employee(app, connection))
    employee.pack(side='left', padx=10)

    inventory_img_data = Image.open("inventory_1.png")
    inventory_img = CTkImage(dark_image=inventory_img_data, light_image=inventory_img_data, size=(100, 100))

    inventory = CTkButton(master=button_frame, image=inventory_img, text="Inventory Management", fg_color="transparent", font=("Arial Bold", 25), hover_color="#207244", anchor="center", command=lambda: open_inventory(app, connection))
    inventory.pack(side='left', padx=10)

    # Create a new frame for the "Sales and Reports" button to place it on the next line
    sales_button_frame = CTkFrame(master=main_frame, fg_color="transparent")
    sales_button_frame.pack(pady=(20, 10), anchor="center")  # Adjusted padding for spacing

    sales_img_data = Image.open("sales.png")
    sales_img = CTkImage(dark_image=sales_img_data, light_image=sales_img_data, size=(100, 100))

    sales = CTkButton(master=sales_button_frame, image=sales_img, text="Sales and Reports", fg_color="transparent", font=("Arial Bold", 25), hover_color="#207244", anchor="center", command=lambda: open_sales(app, connection))
    sales.pack()

def open_menu(app, connection):
    app.destroy()  # Destroy the current window
    MenuFile()  # Call the menu function
    exit(0)

def open_employee(app, connection):
    app.destroy()
    employeeFile()
    exit(0)

def open_inventory(app, connection):
    app.destroy()
    inventoryFile()
    exit(0)

def open_sales(app, connection):
    app.destroy()
    salesFile()
    exit(0)

def connect_to_database(server, database):
    try:
        connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        print("Database connection established successfully!")
        return connection
    except pyodbc.Error as ex:
        print(f"Error connecting to the database: {ex}")
        return None

def admin_file():
    server = 'DESKTOP-DTNJB1H\\SQLEXPRESS'
    database = 'tastytrack'

    # Establish the database connection
    connection = connect_to_database(server, database)

    if connection is not None:
        app = CTk()
        app.geometry("1200x670")
        app.resizable(0, 0)
        set_appearance_mode("light")
        setup_ui(app, connection)
        app.mainloop()
        connection.close()
    else:
        print("Failed to establish a database connection.")

if __name__ == "__main__":
    admin_file()
