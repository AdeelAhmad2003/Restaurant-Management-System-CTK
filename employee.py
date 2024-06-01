from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import customtkinter as ctk
from tkinter import ttk
import pyodbc

app = CTk()
app.geometry("1200x740")
app.resizable(0,0)

set_appearance_mode("light")

sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55",  width=180, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("employees.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))

label1=CTkLabel(master=sidebar_frame, text="", image=logo_img)
label1.pack(pady=(38, 10), anchor="center")

add_img_data = Image.open("add.png")
add_img = CTkImage(dark_image=add_img_data, light_image=add_img_data)

add=CTkButton(master=sidebar_frame, image=add_img, text="Add Employee",fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda:add_employee(app))
add.pack(anchor="center", ipady=10, pady=(16, 0))

update_img_data = Image.open("update.png")
update_img = CTkImage(dark_image=update_img_data, light_image=update_img_data)
update=CTkButton(master=sidebar_frame, image=update_img, text="Update Employee", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda:update_employee(app))
update.pack(anchor="center", ipady=10, pady=(16, 0))

delete_img_data = Image.open("delete.png")
delete_img = CTkImage(dark_image=delete_img_data, light_image=delete_img_data)
delete=CTkButton(master=sidebar_frame, image=delete_img, text="Delete Employee", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda:delete_employee(app))
delete.pack(anchor="center", ipady=10, pady=(16, 0))

#==============================Item Frame=======================================
item_frame = CTkFrame(master=app, fg_color="#eee",  width=335, height=670, corner_radius=0)
item_frame.pack_propagate(0)
item_frame.pack(fill="y", anchor="w", side="left")
main_label=CTkLabel(master=item_frame, text="Employee Management", font=("Arial Black", 25), text_color="#2A8C55")
main_label.grid(row=0,column=0,columnspan=4)
employee_id=CTkLabel(master=item_frame, text="Employee ID:", font=("Arial Bold", 20), text_color="#2A8C55")
employee_id.grid(row=1,column=0,padx=10, pady=10,sticky='w')
employee_id_entry=CTkEntry(master=item_frame, width=305, placeholder_text="Enter Id", border_color="#2A8C55", border_width=2)
employee_id_entry.grid(row=2,column=0,columnspan=2,padx=10, pady=10)

employee_name=CTkLabel(master=item_frame, text="Employee Name:", font=("Arial Bold", 20), text_color="#2A8C55")
employee_name.grid(row=3,column=0,padx=10, pady=10,sticky='w')
employee_name_entry=CTkEntry(master=item_frame, width=305, placeholder_text="Enter Name", border_color="#2A8C55", border_width=2)   
employee_name_entry.grid(row=4,column=0,columnspan=2,padx=10, pady=10)

#dish_category=employee_name=CTkLabel(master=item_frame, text="Dish Category:", font=("Arial Bold", 20), text_color="#2A8C55")
#dish_category.grid(row=5,column=0,padx=10, pady=10,sticky='w')
#dish_category_value=CTkComboBox(master=item_frame, width=305, values=["FastFood", "Desi", "Chinese", "Turkish", "Drinks", "Deserts"], button_color="#2A8C55", border_color="#2A8C55", border_width=2,
#     button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
#dish_category_value.grid(row=6,column=0,columnspan=2,padx=10, pady=10)

employee_contact=CTkLabel(master=item_frame, text="Employee Contact:", font=("Arial Bold", 20), text_color="#2A8C55")
employee_contact.grid(row=5,column=0,padx=10, pady=10,sticky='w')
employee_contact_entry=CTkEntry(master=item_frame, width=305, placeholder_text="Enter Contact.no", border_color="#2A8C55", border_width=2)
employee_contact_entry.grid(row=6,column=0,columnspan=2,padx=10, pady=10)

employee_email=CTkLabel(master=item_frame, text="Employee E-mail:", font=("Arial Bold", 20), text_color="#2A8C55")
employee_email.grid(row=7,column=0,padx=10, pady=10,sticky='w')
employee_email_entry=CTkEntry(master=item_frame, width=305, placeholder_text="Enter E-mail Address", border_color="#2A8C55", border_width=2)
employee_email_entry.grid(row=8,column=0,columnspan=2,padx=10, pady=10)



employee_username=CTkLabel(master=item_frame, text="Employee Username:", font=("Arial Bold", 20), text_color="#2A8C55")
employee_username.grid(row=9,column=0,padx=10, pady=10,sticky='w')
employee_username_entry=CTkEntry(master=item_frame, width=305, placeholder_text="Enter Username", border_color="#2A8C55", border_width=2)
employee_username_entry.grid(row=10,column=0,columnspan=2,padx=10, pady=10)

employee_password=CTkLabel(master=item_frame, text="Employee Password:", font=("Arial Bold", 20), text_color="#2A8C55")
employee_password.grid(row=11,column=0,padx=10, pady=10,sticky='w')
employee_password_entry=CTkEntry(master=item_frame, width=305, placeholder_text="Enter Password",show='*', border_color="#2A8C55", border_width=2)
employee_password_entry.grid(row=12,column=0,columnspan=2,padx=10, pady=10)

employee_duty=CTkLabel(master=item_frame, text="Employee Duty:", font=("Arial Bold", 20), text_color="#2A8C55")
employee_duty.grid(row=13,column=0,padx=10, pady=10,sticky='w')
employee_duty_entry=CTkEntry(master=item_frame, width=305, placeholder_text="Enter Task", border_color="#2A8C55", border_width=2)
employee_duty_entry.grid(row=14,column=0,columnspan=2,padx=10, pady=10)



#=================================Print Frame==========================

main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=670, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")
search_entry=None

message_label = CTkLabel(master=main_view, text="Message Will Appear Here!",width=100)
message_label.pack(anchor="center", ipady=5, pady=(10, 0))
search_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
search_container.pack(fill="x", pady=(10, 0), padx=27)
radio_var = ctk.IntVar(value=0)

search_entry=CTkEntry(master=search_container, width=200, placeholder_text="Search Item", border_color="#2A8C55", border_width=2)
search_entry.pack(side="left", padx=(13, 0), pady=15)
search_button = CTkButton(master=search_container, text="Search",fg_color="#2A8C55", font=("Arial Bold", 14), hover_color="#207244", command=lambda:search_employee(app))
search_button.pack(side="left", padx=(13, 0), pady=15)
radiobutton_1 = CTkRadioButton(master=search_container, text="By ID",variable= radio_var, value=1,border_color="#2A8C55",hover_color="#2A8C55")
radiobutton_1.pack(side="left", padx=(13, 0), pady=15)
radiobutton_2 = CTkRadioButton(master=search_container, text="By Name",variable= radio_var, value=2,border_color="#2A8C55",hover_color="#2A8C55")
radiobutton_2.pack(side="left", padx=(13, 0), pady=15)


app.tree = ttk.Treeview(main_view, columns=("ID", "Name", "Contact","E-Mail", "Username","Password","Duty"), show="headings", style="Treeview")
app.tree.pack(fill="both", expand=True,pady=5)  # Use pack() for the Treeview

# Set up vertical scrollbar
app.tree_scroll_y = ttk.Scrollbar(main_view, orient="vertical", command=app.tree.yview)
app.tree_scroll_y.pack(side="right", fill="y",padx=1)  # Use pack() for the scrollbar

# Set up horizontal scrollbar
app.tree_scroll_x = ttk.Scrollbar(main_view, orient="horizontal", command=app.tree.xview)
app.tree_scroll_x.pack(fill="x")  # Use pack() for the scrollbar

# Attach scrollbars to the Treeview
app.tree.configure(yscrollcommand=app.tree_scroll_y.set, xscrollcommand=app.tree_scroll_x.set)
bg_color = "#fff"
text_color = "#000000"
selected_color = "#2A8C55"


treestyle = ttk.Style()
treestyle.theme_use('default')
treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
treestyle.map('Treeview', background=[('selected', selected_color)], foreground=[('selected',text_color)])
main_view.bind("<<TreeviewSelect>>", lambda event: main_view.focus_set())

# Configure column headings
app.tree.heading("ID", text="ID")
app.tree.heading("Name", text="Name")
app.tree.heading("Contact", text="Contact")
app.tree.heading("E-Mail", text="E-Mail")
app.tree.heading("Username", text="Username")
app.tree.heading("Password", text="Password")
app.tree.heading("Duty", text="Duty")

# Configure column widths
column_widths = [50, 200, 100, 100]
for i, width in enumerate(column_widths):
    app.tree.column(i, width=width, anchor='center')

def load_employee_data(connection,app):
    if connection is not None:
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM Employee")
            employee_data = cur.fetchall()

            # Clear existing items in the Treeview
            for record in app.tree.get_children():
                app.tree.delete(record)

            # Insert data into the Treeview
            for item in employee_data:
                    # Format each column as needed to avoid overflow
                    formatted_columns = []
                    for column in item:
                        if column is not None:
                            formatted_columns.append("{:<20}".format(column))  # Format column if not None
                        else:
                            formatted_columns.append("")  # Add empty string if column is None

                    # Insert formatted data into Treeview
                    app.tree.insert("", ctk.END, values=formatted_columns)

            connection.commit()
            #app.message_label.config(text='Menu Loaded Successfully!',foreground='green')
        except pyodbc.Error as ex:
            print(f"Error fetching data from the database: {ex}")
            app.message_label.config(text='Failed to Load Employee!',foreground='red')
    else:
        print("Database connection is not established.")
def find_id():
        id_term = employee_id_entry.get()
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM Employee WHERE Employee_ID = ?", (id_term,))
            employee_data = cur.fetchall()
            if len(employee_data) == 0:
                return 0  # ID doesn't exist
            else:
                return 1  # ID exists
        except pyodbc.Error as ex:
            print(f"Error: {ex}")
            return -1  # Some error occurred
def search_employee(app):
        global search_entry
        global message_label
        search_term = search_entry.get().strip()
        if len(search_term)==0:
            message_label.configure(text="Please Enter Employee Name or ID to Search",text_color='#FF0000')

        elif connection is not None:
            try:
                    cur = connection.cursor()
                    if radio_var.get() == 1:  # Searching by ID
                        cur.execute("SELECT * FROM Employee  WHERE Employee_ID LIKE ?", ('%' + search_term + '%',))
                    elif radio_var.get() == 2:  # Searching by name
                        cur.execute("SELECT * FROM Employee WHERE Employee_Name LIKE ?", ('%' + search_term + '%',))
                    employee_data = cur.fetchall()
                    # Clear existing items in the Treeview
                    for record in app.tree.get_children():
                        app.tree.delete(record)

                    # Insert data into the Treeview
                    for item in employee_data:
                        app.tree.insert("", ctk.END, values=item)

                    connection.commit()
                    message_label.configure(text='Employee Found Successfully!',text_color="#2A8C55")
                    if(len(employee_data)==0):
                        message_label.configure(text="Employee not Found",text_color='#FF0000')
            except pyodbc.Error as ex:
                print(f"Error searching data from the database: {ex}")
        else:
            print("Database connection is not established.")
def add_employee(app):
        employee_id = employee_id_entry.get().strip()  # Strip leading and trailing whitespace
        employee_name = employee_name_entry.get()
        employee_contact=employee_contact_entry.get()
        employee_email=employee_email_entry.get()
        employee_username = employee_username_entry.get()
        employee_password=employee_password_entry.get()
        employee_duty=employee_duty_entry.get()

        if not employee_id:  # Check if employee_id is empty
            message_label.configure(text="Employee ID is mandatory", text_color='#FF0000')
        elif find_id() == 1:
            message_label.configure(text="Employee already exists", text_color='#FF0000')
        else:
            try:
                cur = connection.cursor()
                cur.execute("INSERT INTO Employee (Employee_ID, Employee_Name,Employee_Contact,Employee_Email, Employee_Username,Employee_Password,Employee_Duty) VALUES (?, ?, ?, ?, ?, ?, ?)",(employee_id, employee_name,employee_contact,employee_email ,employee_username,employee_password,employee_duty))
                connection.commit()
                message_label.configure(text="Success: Employee Added!", text_color='#2A8C55')
                load_employee_data(connection,app)  # Reload data in Treeview after adding new item
            except pyodbc.Error as ex:
                print(f"Error inserting data into the database: {ex}")
                message_label.configure(text="Error: Failed to Add Employee!", text_color='#FF0000')

def delete_employee(app):
        employee_id = employee_id_entry.get().strip()  # Strip leading and trailing whitespace
        if not employee_id:  # Check if employee_id is empty
            message_label.configure(text="Employee ID is mandatory for deletion", text_color='#FF0000')
        elif find_id() == 0:
            message_label.configure(text="Employee does not exist",text_color='#FF0000')
        elif connection is not None:
            try:
                cur = connection.cursor()
                cur.execute("DELETE FROM Employee WHERE Employee_ID = ?", (employee_id,))
                connection.commit()
                message_label.configure(text='Employee Details Deleted Successfully!', text_color="#2A8C55")
                load_employee_data(connection,app)  # Reload data in Treeview after deleting item
            except pyodbc.Error as ex:
                print(f"Error deleting data from the database: {ex}")
                message_label.configure(text="Failed to Delete Employee Details!", text_color='#FF000')
        else:
            print("Database connection is not established.")


def update_employee(app):
        employee_id = employee_id_entry.get().strip()
        employee_name = employee_name_entry.get()
        employee_contact=employee_contact_entry.get()
        employee_email=employee_email_entry.get()
        employee_username = employee_username_entry.get()
        employee_password=employee_password_entry.get()
        employee_duty=employee_duty_entry.get()

        if not employee_id:
                message_label.configure(text="Employee Id is Mandatory for Updating",text_color='#FF0000')
        elif (find_id()==0):
            message_label.configure(text="Employee Does Not Exist ",text_color='#FF0000')

        elif connection is not None:
            try:
                cur = connection.cursor()
                cur.execute("UPDATE Employee SET Employee_Name=?, Employee_Contact=?, Employee_Email=?, Employee_Username=?, Employee_Password=?, Employee_Duty=?  WHERE employee_ID=?", (employee_name,employee_contact,employee_email, employee_username,employee_password,employee_duty,employee_id))
                connection.commit()
                message_label.configure(text="Employee Details Updated Successfully!",text_color="#2A8C55")
                load_employee_data(connection,app)  # Reload data in Treeview after updating item
            except pyodbc.Error as ex:
                print(f"Error updating data in the database: {ex}")
                message_label.configure(text="Failed to Update Emplopyee Details!",text_color='FF0000')
        else:
            print("Database connection is not established.")

def connect_to_database(server, database):
    try:
        connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        print("Database connection established successfully!")
        return connection
    except pyodbc.Error as ex:
        print(f"Error connecting to the database: {ex}")
        return None

if __name__ == "__main__":
    server = 'DESKTOP-8RO21S6\SQLEXPRESS'
    database = 'tastytrack'

    # Establish the database connection
    connection = connect_to_database(server, database)

    if connection is not None:
        try:
            load_employee_data(connection,app)
            app.mainloop()
        finally:
            # Close the database connection
            connection.close()
    else:
        print("Failed to establish a database connection.")
