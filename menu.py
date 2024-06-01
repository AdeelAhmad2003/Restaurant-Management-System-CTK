from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import customtkinter as ctk
from tkinter import ttk
import pyodbc

app = CTk()
app.geometry("1200x670")
app.resizable(0,0)

set_appearance_mode("light")

sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55",  width=180, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))

label1=CTkLabel(master=sidebar_frame, text="", image=logo_img)
label1.pack(pady=(38, 10), anchor="center")

add_img_data = Image.open("add.png")
add_img = CTkImage(dark_image=add_img_data, light_image=add_img_data)

add=CTkButton(master=sidebar_frame, image=add_img, text="Add Item",fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda:add_menu_item(app))
add.pack(anchor="center", ipady=10, pady=(16, 0))

update_img_data = Image.open("update.png")
update_img = CTkImage(dark_image=update_img_data, light_image=update_img_data)
update=CTkButton(master=sidebar_frame, image=update_img, text="Update Item", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda:update_menu_item(app))
update.pack(anchor="center", ipady=10, pady=(16, 0))

delete_img_data = Image.open("delete.png")
delete_img = CTkImage(dark_image=delete_img_data, light_image=delete_img_data)
delete=CTkButton(master=sidebar_frame, image=delete_img, text="Delete Item", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda:delete_menu_item(app))
delete.pack(anchor="center", ipady=10, pady=(16, 0))

reload_img_data = Image.open("reload.png")
reload_img = CTkImage(dark_image=reload_img_data, light_image=reload_img_data)
reload=CTkButton(master=sidebar_frame, image=reload_img, text="Reload Menu", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda:load_menu_data(connection,app))
reload.pack(anchor="center", ipady=10, pady=(16, 0))

sort_value=CTkComboBox(master=sidebar_frame, width=175, values=["Sort By ...", "Sort By Name", "Sort By Category", "Sort By Price(Lowest)","Sort By Price(Highest)"], button_color="#454545", border_color="#454545", border_width=2,
     button_hover_color="#FFF",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff",command=lambda value:sort_menu_from_database(app))
sort_value.pack(anchor="center", ipady=1, pady=(16, 0))




#==============================Item Frame=======================================
item_frame = CTkFrame(master=app, fg_color="#eee",  width=335, height=670, corner_radius=0)
item_frame.pack_propagate(0)
item_frame.pack(fill="y", anchor="w", side="left")
main_label=CTkLabel(master=item_frame, text="Menu Management", font=("Arial Black", 25), text_color="#2A8C55")
main_label.grid(row=0,column=0,columnspan=4)
dish_id=CTkLabel(master=item_frame, text="Dish ID:", font=("Arial Bold", 20), text_color="#2A8C55")
dish_id.grid(row=1,column=0,padx=10, pady=10,sticky='w')
dish_id_entry=CTkEntry(master=item_frame, width=305, placeholder_text="Enter Id", border_color="#2A8C55", border_width=2)
dish_id_entry.grid(row=2,column=0,columnspan=2,padx=10, pady=10)

dish_name=CTkLabel(master=item_frame, text="Dish Name:", font=("Arial Bold", 20), text_color="#2A8C55")
dish_name.grid(row=3,column=0,padx=10, pady=10,sticky='w')
dish_name_entry=CTkEntry(master=item_frame, width=305, placeholder_text="Enter Name", border_color="#2A8C55", border_width=2)   
dish_name_entry.grid(row=4,column=0,columnspan=2,padx=10, pady=10)

dish_category=dish_name=CTkLabel(master=item_frame, text="Dish Category:", font=("Arial Bold", 20), text_color="#2A8C55")
dish_category.grid(row=5,column=0,padx=10, pady=10,sticky='w')
dish_category_value=CTkComboBox(master=item_frame, width=305, values=["Appetizer", "Soup", "Salad", "Rice", "Mutton Handian", "Chicken Handian","Beef Handian","Traditional Food","Seafood","Burger","Pizza","Tandoor","SoftDrink","HotDrink","Shake","Ice-Cream","Dessert"], button_color="#2A8C55", border_color="#2A8C55", border_width=2,
     button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
dish_category_value.grid(row=6,column=0,columnspan=2,padx=10, pady=10)


dish_price=CTkLabel(master=item_frame, text="Dish Price:", font=("Arial Bold", 20), text_color="#2A8C55")
dish_price.grid(row=7,column=0,padx=10, pady=10,sticky='w')
dish_price_entry=CTkEntry(master=item_frame, width=305, placeholder_text="Enter Price", border_color="#2A8C55", border_width=2)
dish_price_entry.grid(row=8,column=0,columnspan=2,padx=10, pady=10)


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
search_button = CTkButton(master=search_container, text="Search",fg_color="#2A8C55", font=("Arial Bold", 14), hover_color="#207244", command=lambda:search_menu_item(app))
search_button.pack(side="left", padx=(13, 0), pady=15)
radiobutton_1 = CTkRadioButton(master=search_container, text="By ID",variable= radio_var, value=1,border_color="#2A8C55",hover_color="#2A8C55")
radiobutton_1.pack(side="left", padx=(13, 0), pady=15)
radiobutton_2 = CTkRadioButton(master=search_container, text="By Name",variable= radio_var, value=2,border_color="#2A8C55",hover_color="#2A8C55")
radiobutton_2.pack(side="left", padx=(13, 0), pady=15)


app.tree = ttk.Treeview(main_view, columns=("ID", "Name", "Category", "Price"), show="headings", style="Treeview")
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
app.tree.heading("Category", text="Category")
app.tree.heading("Price", text="Price")

# Configure column widths
column_widths = [50, 200, 100, 100]
for i, width in enumerate(column_widths):
    app.tree.column(i, width=width, anchor='center')

def load_menu_data(connection,app):
    if connection is not None:
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM Menu")
            menu_data = cur.fetchall()

            # Clear existing items in the Treeview
            for record in app.tree.get_children():
                app.tree.delete(record)

            # Insert data into the Treeview
            for item in menu_data:
                # Format category to ensure it doesn't overflow
                formatted_category = "{:<20}".format(item[2])  # Adjust width as needed

                # Insert formatted data into Treeview
                app.tree.insert("", ctk.END, values=(item[0], item[1], formatted_category, item[3]))

            connection.commit()
            #app.message_label.config(text='Menu Loaded Successfully!',foreground='green')
        except pyodbc.Error as ex:
            print(f"Error fetching data from the database: {ex}")
            app.message_label.config(text='Failed to Load Menu!',foreground='red')
    else:
        print("Database connection is not established.")
def find_id():
        id_term = dish_id_entry.get()
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM Menu WHERE Dish_ID = ?", (id_term,))
            menu_data = cur.fetchall()
            if len(menu_data) == 0:
                return 0  # ID doesn't exist
            else:
                return 1  # ID exists
        except pyodbc.Error as ex:
            print(f"Error: {ex}")
            return -1  # Some error occurred
def search_menu_item(app):
    global search_entry
    global message_label
    search_term = search_entry.get().strip()
    if len(search_term) == 0:
        message_label.configure(text="Please Enter Item Name or ID to Search", text_color='#FF0000')
    elif connection is not None:
        try:
            cur = connection.cursor()
            if radio_var.get() == 1:  # Searching by ID
                cur.execute("SELECT * FROM Menu WHERE Dish_ID = ?", (search_term,))
            elif radio_var.get() == 2:  # Searching by name
                cur.execute("SELECT * FROM Menu WHERE Dish_Name LIKE ?", ('%' + search_term + '%',))
            menu_data = cur.fetchall()
            # Clear existing items in the Treeview
            for record in app.tree.get_children():
                app.tree.delete(record)

            # Insert data into the Treeview
            for item in menu_data:
                app.tree.insert("", ctk.END, values=(item[0], item[1], item[2],item[3]))

            connection.commit()
            if len(menu_data) > 0:
                message_label.configure(text='Item Found Successfully!', text_color="#2A8C55")
            else:
                message_label.configure(text="Item not Found", text_color='#FF0000')
        except pyodbc.Error as ex:
            message_label.configure(text="Error occurred while searching.", text_color='#FF0000')
    else:
        print("Database connection is not established.")
def add_menu_item(app):
        dish_id = dish_id_entry.get().strip()  # Strip leading and trailing whitespace
        dish_name = dish_name_entry.get()
        dish_category = dish_category_value.get()
        dish_price = dish_price_entry.get()

        if not dish_id:  # Check if dish_id is empty
            message_label.configure(text="Dish ID is mandatory", text_color='#FF0000')
        elif find_id() == 1:
            message_label.configure(text="Item already exists", text_color='#FF0000')
        else:
            try:
                cur = connection.cursor()
                cur.execute("INSERT INTO Menu (Dish_ID, Dish_Name, Dish_Category, Dish_Price_PKR) VALUES (?, ?, ?, ?)",(dish_id, dish_name, dish_category, dish_price))
                connection.commit()
                message_label.configure(text="Success: Item added to the menu.", text_color='#2A8C55')
                load_menu_data(connection,app)  # Reload data in Treeview after adding new item
            except pyodbc.Error as ex:
                print(f"Error inserting data into the database: {ex}")
                message_label.configure(text="Error: Failed to add item to the menu.", text_color='#FF0000')

def delete_menu_item(app):
        dish_id = dish_id_entry.get().strip()  # Strip leading and trailing whitespace
        if not dish_id:  # Check if dish_id is empty
            message_label.configure(text="Dish ID is mandatory for deletion", text_color='#FF0000')
        elif find_id() == 0:
            message_label.configure(text="Item does not exist",text_color='#FF0000')
        elif connection is not None:
            try:
                cur = connection.cursor()
                cur.execute("DELETE FROM Menu WHERE Dish_ID = ?", (dish_id,))
                connection.commit()
                message_label.configure(text='Item deleted from the menu successfully!', text_color="#2A8C55")
                load_menu_data(connection,app)  # Reload data in Treeview after deleting item
            except pyodbc.Error as ex:
                print(f"Error deleting data from the database: {ex}")
                message_label.configure(text="Failed to delete item from the menu", text_color='#FF000')
        else:
            print("Database connection is not established.")


def update_menu_item(app):
        dish_id = dish_id_entry.get().strip()
        dish_name = dish_name_entry.get()
        dish_category =dish_category_value.get()
        dish_price = dish_price_entry.get()
        if not dish_id:
                message_label.configure(text="Dish Id is Mandatory for Updating",text_color='#FF0000')
        elif (find_id()==0):
            message_label.configure(text="Item Does Not Exist ",text_color='#FF0000')

        elif connection is not None:
            try:
                cur = connection.cursor()
                cur.execute("UPDATE Menu SET Dish_Name=?, Dish_Category=?, Dish_Price_PKR=? WHERE Dish_ID=?", (dish_name, dish_category, dish_price, dish_id))
                connection.commit()
                message_label.configure(text="Item updated in the menu successfully!",text_color="#2A8C55")
                load_menu_data(connection,app)  # Reload data in Treeview after updating item
            except pyodbc.Error as ex:
                print(f"Error updating data in the database: {ex}")
                message_label.configure(text="Failed to update item in the menu!",text_color='FF0000')
        else:
            print("Database connection is not established.")

def sort_menu_from_database(app):
    sort_criteria = sort_value.get()

    if sort_criteria == "Sort By Name":
        column_to_sort = "Dish_Name"
        ascending = True
    elif sort_criteria == "Sort By Category":
        column_to_sort = "Dish_Category"
        ascending = True
    elif sort_criteria == "Sort By Price(Lowest)":
        column_to_sort = "Dish_Price_PKR"
        ascending = True
    elif sort_criteria == "Sort By Price(Highest)":
        column_to_sort = "Dish_Price_PKR"
        ascending = False
    else:
        # No sorting criteria selected
        return

    try:
        cur = connection.cursor()
        # Constructing the SQL query dynamically based on the selected criteria
        query = f"SELECT * FROM Menu ORDER BY {column_to_sort} {'ASC' if ascending else 'DESC'}"
        cur.execute(query)
        sorted_menu_data = cur.fetchall()

        # Clear existing items in the Treeview
        for record in app.tree.get_children():
            app.tree.delete(record)

        # Insert sorted data into the Treeview
        for item in sorted_menu_data:
            app.tree.insert("", ctk.END, values=(item[0], item[1], item[2],item[3]))

        message_label.configure(text='Menu items sorted successfully!', text_color="#2A8C55")
    except pyodbc.Error as ex:
        print(f"Error sorting menu items: {ex}")
        message_label.configure(text="Error occurred while sorting menu items.", text_color='#FF0000')


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
            load_menu_data(connection,app)
            app.mainloop()
        finally:
            # Close the database connection
            connection.close()
    else:
        print("Failed to establish a database connection.")
