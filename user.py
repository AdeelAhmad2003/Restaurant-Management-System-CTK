from customtkinter import *
from datetime import datetime
from CTkTable import CTkTable
from PIL import Image
import customtkinter as ctk
from tkinter import ttk, Scrollbar
import tkinter as tk
import pyodbc
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import reportlab.lib.pagesizes
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from datetime import datetime
app = CTk()
app.geometry("1350x670")
app.resizable(0,0)

set_appearance_mode("light")

sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55",  width=200, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

# Display current time
time_label = CTkLabel(master=sidebar_frame, text="Time:", fg_color="#2A8C55", font=("Arial", 20))
time_label.pack(pady=10)

# Display current date
date_label = CTkLabel(master=sidebar_frame, text="Date:", fg_color="#2A8C55", font=("Arial", 14))
date_label.pack(pady=10)

# Function to update the time and date every second
def update_time_and_date():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    current_date = datetime.now().strftime("%A, %B %d, %Y")
    time_label.configure(text=current_time)
    date_label.configure(text=current_date)
    app.after(1000, update_time_and_date)  # Update every second

# Initial call to update_time_and_date function to start updating the time and date
update_time_and_date()

logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))

label1=CTkLabel(master=sidebar_frame, text="", image=logo_img)
label1.pack(pady=(38, 10), anchor="center")
#================Button Frame=========
button_frame = CTkScrollableFrame(master=sidebar_frame, fg_color="#2A8C55",label_text="Menu")
button_frame.pack(fill="both", expand=True)
#=============Appetizer=================
appetizer_img_data = Image.open("appetizer.png")
appetizer_img = CTkImage(dark_image=appetizer_img_data, light_image=appetizer_img_data,size=(45,45))
appetizer=CTkButton(master=button_frame, image=appetizer_img, text="Appetizer",fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
appetizer.pack(anchor="center", ipady=10, pady=(16, 0))
#==============Soup=====================
soup_img_data = Image.open("soup.png")
soup_img = CTkImage(dark_image=soup_img_data, light_image=soup_img_data,size=(45,45))
soup=CTkButton(master=button_frame, image=soup_img, text="Soup", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
soup.pack(anchor="center", ipady=10, pady=(16, 0))
#===============Salad===================
salad_img_data = Image.open("salad.png")
salad_img = CTkImage(dark_image=salad_img_data, light_image=salad_img_data,size=(45,45))
salad=CTkButton(master=button_frame, image=salad_img, text="Salad", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
salad.pack(anchor="center", ipady=10, pady=(16, 0))
#===============Rice=======================
rice_img_data = Image.open("fried-rice.png")
rice_img = CTkImage(dark_image=rice_img_data, light_image=rice_img_data,size=(45,45))
rice=CTkButton(master=button_frame, image=rice_img, text="Rice", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
rice.pack(anchor="center", ipady=10, pady=(16, 0))
#===============Mutton=====================
mutton_img_data = Image.open("mutton.png")
mutton_img = CTkImage(dark_image=mutton_img_data, light_image=mutton_img_data,size=(45,45))
mutton=CTkButton(master=button_frame, image=mutton_img, text="Mutton Handian", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
mutton.pack(anchor="center", ipady=10, pady=(16, 0))
#===============Chicken===================
chicken_img_data = Image.open("chickenleg.png")
chicken_img = CTkImage(dark_image=chicken_img_data, light_image=chicken_img_data,size=(45,45))
chicken=CTkButton(master=button_frame, image=chicken_img, text="Chicken Handian", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
chicken.pack(anchor="center", ipady=10, pady=(16, 0))
#================Beef=====================
beef_img_data = Image.open("beef.png")
beef_img = CTkImage(dark_image=beef_img_data, light_image=beef_img_data,size=(45,45))
beef=CTkButton(master=button_frame, image=beef_img, text="Beef Handian", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
beef.pack(anchor="center", ipady=10, pady=(16, 0))
#===========Traditional Food==============
traditional_img_data = Image.open("traditional food.png")
traditional_img = CTkImage(dark_image=traditional_img_data, light_image=traditional_img_data,size=(45,45))
traditional=CTkButton(master=button_frame, image=traditional_img, text="Traditional", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
traditional.pack(anchor="center", ipady=10, pady=(16, 0))
#==============Seafood====================
seafood_img_data = Image.open("seafood.png")
seafood_img = CTkImage(dark_image=seafood_img_data, light_image=seafood_img_data,size=(45,45))
seafood=CTkButton(master=button_frame, image=seafood_img, text="Seafood", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
seafood.pack(anchor="center", ipady=10, pady=(16, 0))
#===============Burger=====================
burger_img_data = Image.open("burger.png")
burger_img = CTkImage(dark_image=burger_img_data, light_image=burger_img_data,size=(45,45))
burger=CTkButton(master=button_frame, image=burger_img, text="Burger", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
burger.pack(anchor="center", ipady=10, pady=(16, 0))
#================Pizza=====================
pizza_img_data = Image.open("pizza.png")
pizza_img = CTkImage(dark_image=pizza_img_data, light_image=pizza_img_data,size=(45,45))
pizza=CTkButton(master=button_frame, image=pizza_img, text="Pizza", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
pizza.pack(anchor="center", ipady=10, pady=(16, 0))
#================Tandoor==================
tandoor_img_data = Image.open("tandoor.png")
tandoor_img = CTkImage(dark_image=tandoor_img_data, light_image=tandoor_img_data,size=(45,45))
tandoor=CTkButton(master=button_frame, image=tandoor_img, text="Tandoor", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
tandoor.pack(anchor="center", ipady=10, pady=(16, 0))
#================SoftDrink================
softdrink_img_data = Image.open("softdrink.png")
softdrink_img = CTkImage(dark_image=softdrink_img_data, light_image=softdrink_img_data,size=(45,45))
softdrink=CTkButton(master=button_frame, image=softdrink_img, text="SoftDrinks", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
softdrink.pack(anchor="center", ipady=10, pady=(16, 0))
#===============HotDrinks=================
hotdrink_img_data = Image.open("coffee.png")
hotdrink_img = CTkImage(dark_image=hotdrink_img_data, light_image=hotdrink_img_data,size=(45,45))
hotdrink=CTkButton(master=button_frame, image=hotdrink_img, text="HotDrinks", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
hotdrink.pack(anchor="center", ipady=10, pady=(16, 0))
#===============Shake=====================
shake_img_data = Image.open("shake.png")
shake_img = CTkImage(dark_image=shake_img_data, light_image=shake_img_data,size=(45,45))
shake=CTkButton(master=button_frame, image=shake_img, text="Shakes", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
shake.pack(anchor="center", ipady=10, pady=(16, 0))
#================Ice-Cream================
ice_cream_img_data = Image.open("ice-cream.png")
ice_cream_img = CTkImage(dark_image=ice_cream_img_data, light_image=ice_cream_img_data,size=(45,45))
ice_cream=CTkButton(master=button_frame, image=ice_cream_img, text="Ice-Cream", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
ice_cream.pack(anchor="center", ipady=10, pady=(16, 0))
#===============Dessert===================
dessert_img_data = Image.open("dessert.png")
dessert_img = CTkImage(dark_image=dessert_img_data, light_image=dessert_img_data,size=(45,45))
dessert=CTkButton(master=button_frame, image=dessert_img, text="Dessert", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
dessert.pack(anchor="center", ipady=10, pady=(16, 0))
# sort_value=CTkComboBox(master=sidebar_frame, width=175, values=["Sort By ...", "Sort By Name", "Sort By Category", "Sort By Price"], button_color="#454545", border_color="#454545", border_width=2,
#      button_hover_color="#FFF",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
# sort_value.pack(anchor="center", ipady=1, pady=(16, 0))

#============================Button Result Frame=======================
button_result_frame = CTkFrame(master=app, fg_color="#eee",  width=450, height=670, corner_radius=0)
button_result_frame.pack_propagate(0)
button_result_frame.pack(fill="y", anchor="w", side="left")

search_entry = None

message_label_1 = CTkLabel(master=button_result_frame, text="Select Items To Order from Menu",width=100)
message_label_1.grid(row=0, column=0, columnspan=4, pady=(10, 0), sticky="n")

search_container = CTkFrame(master=button_result_frame, height=50, fg_color="#D3D3D3")
search_container.grid(row=1, column=0, columnspan=4, padx=27, sticky="ew")
radio_var = ctk.IntVar(value=0)

search_entry = CTkEntry(master=search_container, width=200, placeholder_text="Search Item", border_color="#2A8C55", border_width=2)
search_entry.grid(row=0, column=0, padx=(5, 0), pady=15)

search_img_data = Image.open("search.png")
search_img = CTkImage(dark_image=search_img_data, light_image=search_img_data, size=(20, 20))
search_button = CTkButton(master=search_container,image=search_img ,text="Search",width=10,fg_color="#2A8C55", font=("Arial Bold", 14), hover_color="#207244", command=lambda: search_menu_item(app))
search_button.grid(row=0, column=1, padx=(5, 0), pady=15)

radiobutton_1 = CTkRadioButton(master=search_container, text="By ID",width=10,variable=radio_var, value=1, border_color="#2A8C55", hover_color="#2A8C55")
radiobutton_1.grid(row=0, column=2, padx=(5, 0), pady=15)

radiobutton_2 = CTkRadioButton(master=search_container, text="By Name",width=10, variable=radio_var, value=2, border_color="#2A8C55", hover_color="#2A8C55")
radiobutton_2.grid(row=0, column=3, padx=(5, 0), pady=15)



# Create the Treeview widget
app.tree1 = ttk.Treeview(button_result_frame, columns=("ID", "Name", "Category", "Price"),height=27 ,show="headings", style="Treeview")
app.tree1.grid(row=2, column=0, columnspan=4, sticky="nsew")

# Set up the vertical scrollbar
app.tree1_scroll_y = ttk.Scrollbar(button_result_frame, orient="vertical", command=app.tree1.yview)
app.tree1_scroll_y.grid(row=2, column=4, sticky="ns")

# Set up the horizontal scrollbar
app.tree1_scroll_x = ttk.Scrollbar(button_result_frame, orient="horizontal", command=app.tree1.xview)
app.tree1_scroll_x.grid(row=3, column=0, columnspan=4, sticky="ew")

# Attach the scrollbars to the Treeview
app.tree1.configure(yscrollcommand=app.tree1_scroll_y.set, xscrollcommand=app.tree1_scroll_x.set)

# Styling the Treeview widget
bg_color = "#fff"
text_color = "#000000"
selected_color = "#2A8C55"

treestyle = ttk.Style()
treestyle.theme_use('default')
treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
treestyle.map('Treeview', background=[('selected', selected_color)], foreground=[('selected',text_color)])

# Configure column headings
app.tree1.heading("ID", text="ID")
app.tree1.heading("Name", text="Name")
app.tree1.heading("Category", text="Category")
app.tree1.heading("Price", text="Price")

# Configure column widths
column_widths = [50, 200, 100, 100]
for i, width in enumerate(column_widths):
    app.tree1.column(i, width=width, anchor='center')

#==============Buttons Data Loading ==================
def load_data(connection, app, category):
    if connection is not None:
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM Menu WHERE Dish_Category = ?", (category,))
            data = cur.fetchall()

            # Clear existing items in the Treeview
            for record in app.tree1.get_children():
                app.tree1.delete(record)

            # Insert data into the Treeview
            for item in data:
                # Format category to ensure it doesn't overflow
                formatted_category = "{:<20}".format(item[2])  # Adjust width as needed

                # Insert formatted data into Treeview
                app.tree1.insert("", ctk.END, values=(item[0], item[1], formatted_category, item[3]))

            connection.commit()
        except pyodbc.Error as ex:
            print(f"Error fetching data from the database: {ex}")
            message_label_1.configure(text='Failed to Load Data!', text_color='red')
    else:
        print("Database connection is not established.")

# Define functions for each category
def load_appetizer_data():
    load_data(connection, app, 'Appetizer')

def load_soup_data():
    load_data(connection, app, 'Soup')

def load_salad_data():
    load_data(connection, app, 'Salad')

def load_rice_data():
    load_data(connection, app, 'Rice')

def load_mutton_handian_data():
    load_data(connection, app, 'Mutton Handian')

def load_chicken_handian_data():
    load_data(connection, app, 'Chicken Handian')

def load_beef_handian_data():
    load_data(connection, app, 'Beef Handian')

def load_traditional_food_data():
    load_data(connection, app, 'Traditional Food')

def load_seafood_data():
    load_data(connection, app, 'Seafood')

def load_burger_data():
    load_data(connection, app, 'Burger')

def load_pizza_data():
    load_data(connection, app, 'Pizza')

def load_tandoor_data():
    load_data(connection, app, 'Tandoor')

def load_softdrink_data():
    load_data(connection, app, 'SoftDrink')

def load_hotdrink_data():
    load_data(connection, app, 'HotDrink')

def load_shake_data():
    load_data(connection, app, 'Shake')

def load_ice_cream_data():
    load_data(connection, app, 'Ice-Cream')

def load_dessert_data():
    load_data(connection, app, 'Dessert')

# Associate each button with its respective function
appetizer.configure(command=load_appetizer_data)
soup.configure(command=load_soup_data)
salad.configure(command=load_salad_data)
rice.configure(command=load_rice_data)
mutton.configure(command=load_mutton_handian_data)
chicken.configure(command=load_chicken_handian_data)
beef.configure(command=load_beef_handian_data)
traditional.configure(command=load_traditional_food_data)
seafood.configure(command=load_seafood_data)
burger.configure(command=load_burger_data)
pizza.configure(command=load_pizza_data)
tandoor.configure(command=load_tandoor_data)
softdrink.configure(command=load_softdrink_data)
hotdrink.configure(command=load_hotdrink_data)
shake.configure(command=load_shake_data)
ice_cream.configure(command=load_ice_cream_data)
dessert.configure(command=load_dessert_data)

my_tab=CTkTabview(master=app,fg_color="#2A8C55",  width=680, height=670, corner_radius=10,segmented_button_fg_color='#2A8C55',segmented_button_selected_color='#207244',segmented_button_unselected_hover_color='#207244')
my_tab.pack(side="left",anchor='n',pady=0)
tab_1=my_tab.add("Terminal")
tab_2=my_tab.add("Order")
tab_3=my_tab.add("Payment")
#=================================Print Frame==========================

main_view = CTkFrame(master=tab_1, fg_color="#fff", width=680, height=335, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side='top', pady=(16, 10))

message_label = CTkLabel(master=main_view,text="Selected Order", font=("Arial Black", 25), text_color="#2A8C55")
message_label.grid(row=0, column=0, columnspan=4, pady=(10, 0), sticky="n")

app.tree = ttk.Treeview(main_view, columns=("ID", "Name", "Category", "Price"),show="headings", style="Treeview")
app.tree.grid(row=1, column=0, columnspan=4, sticky="nsew")

app.tree_scroll_y = ttk.Scrollbar(main_view, orient="vertical", command=app.tree.yview)
app.tree_scroll_y.grid(row=1, column=4, sticky="ns")

app.tree_scroll_x = ttk.Scrollbar(main_view, orient="horizontal", command=app.tree.xview)
app.tree_scroll_x.grid(row=2, column=0, columnspan=4, sticky="ew")

app.tree.configure(yscrollcommand=app.tree_scroll_y.set, xscrollcommand=app.tree_scroll_x.set)
bg_color = "#fff"
text_color = "#000000"
selected_color = "#2A8C55"

treestyle = ttk.Style()
treestyle.theme_use('default')
treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
treestyle.map('Treeview', background=[('selected', selected_color)], foreground=[('selected', text_color)])

main_view.bind("<<TreeviewSelect>>", lambda event: main_view.focus_set())

# Configure column headings
app.tree.heading("ID", text="ID")
app.tree.heading("Name", text="Name")
app.tree.heading("Category", text="Category")
app.tree.heading("Price", text="Price")

# Configure column widths
column_widths = [120, 150, 150, 150]
for i, width in enumerate(column_widths):
    app.tree.column(i, width=width, anchor='center')

def on_treeview_select(event):
    selected_item = event.widget.selection()
    if selected_item:
        values = event.widget.item(selected_item, 'values')
        if values:
            app.tree.insert("", 'end', values=values)


# Bind the TreeviewSelect event of the first Treeview to the function
app.tree1.bind("<<TreeviewSelect>>", on_treeview_select)
#=====DElete==============

def remove_selected(app,event=None):
        selected_items = app.tree.selection()
        if selected_items:
            for item in selected_items:
                app.tree.delete(item)
        else:
            tk.messagebox.showinfo("No Selection", "Please select an item to remove.")
app.tree.bind("<Delete>",lambda event: remove_selected(app,event))
#===========Table=========
# Table Frame
table_frame = CTkFrame(master=tab_1, fg_color="#2A8C55", width=680, height=335, corner_radius=10)
table_frame.pack_propagate(0)
table_frame.pack(side='top', pady=(16, 10))

# Define frame for the first row of buttons
table_row1_frame = CTkFrame(master=table_frame,fg_color="#2A8C55", width=680)
table_row1_frame.pack(side='top', pady=(16, 10))

# Define frame for the second row of buttons
table_row2_frame = CTkFrame(master=table_frame,fg_color="#2A8C55", width=680)
table_row2_frame.pack(side='top', pady=(16, 10))

# Define frame for the third row of buttons
table_row3_frame = CTkFrame(master=table_frame,fg_color="#2A8C55", width=680)
table_row3_frame.pack(side='top', pady=(16, 10))

# Add buttons for the first row
table1_img_data = Image.open("table.png")
table1_img = CTkImage(dark_image=table1_img_data, light_image=table1_img_data, size=(45, 45))
table1 = CTkButton(master=table_row1_frame, image=table1_img, text="Table 1", text_color='black', fg_color="#D3D3D3", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda: update_selected_table(1))
table1.pack(side='left', padx=(16, 0), pady=(0, 0))

table2_img_data = Image.open("table.png")
table2_img = CTkImage(dark_image=table2_img_data, light_image=table2_img_data, size=(45, 45))
table2 = CTkButton(master=table_row1_frame, image=table2_img, text="Table 2", text_color='black', fg_color="#D3D3D3", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda: update_selected_table(2))
table2.pack(side='left', padx=(16, 0), pady=(0, 0))

table3_img_data = Image.open("table.png")
table3_img = CTkImage(dark_image=table3_img_data, light_image=table3_img_data, size=(45, 45))
table3 = CTkButton(master=table_row1_frame, image=table3_img, text="Table 3", text_color='black', fg_color="#D3D3D3", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda: update_selected_table(3))
table3.pack(side='left', padx=(16, 0), pady=(0, 0))

table4_img_data = Image.open("table.png")
table4_img = CTkImage(dark_image=table4_img_data, light_image=table4_img_data, size=(45, 45))
table4 = CTkButton(master=table_row1_frame, image=table4_img, text="Table 4", text_color='black', fg_color="#D3D3D3", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda: update_selected_table(4))
table4.pack(side='left', padx=(16, 0), pady=(0, 0))

# Add buttons for the second row
table5_img_data = Image.open("table.png")
table5_img = CTkImage(dark_image=table5_img_data, light_image=table5_img_data, size=(45, 45))
table5 = CTkButton(master=table_row2_frame, image=table5_img, text="Table 5", text_color='black', fg_color="#D3D3D3", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda: update_selected_table(5))
table5.pack(side='left', padx=(16, 0), pady=(0, 0))

table6_img_data = Image.open("table.png")
table6_img = CTkImage(dark_image=table6_img_data, light_image=table6_img_data, size=(45, 45))
table6 = CTkButton(master=table_row2_frame, image=table6_img, text="Table 6", text_color='black', fg_color="#D3D3D3", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda: update_selected_table(6))
table6.pack(side='left', padx=(16, 0), pady=(0, 0))

table7_img_data = Image.open("table.png")
table7_img = CTkImage(dark_image=table7_img_data, light_image=table7_img_data, size=(45, 45))
table7 = CTkButton(master=table_row2_frame, image=table7_img, text="Table 7", text_color='black', fg_color="#D3D3D3", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda: update_selected_table(7))
table7.pack(side='left', padx=(16, 0), pady=(0, 0))

table8_img_data = Image.open("table.png")
table8_img = CTkImage(dark_image=table8_img_data, light_image=table8_img_data, size=(45, 45))
table8 = CTkButton(master=table_row2_frame, image=table8_img, text="Table 8", text_color='black', fg_color="#D3D3D3", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda: update_selected_table(8))
table8.pack(side='left', padx=(16, 0), pady=(0, 0))

# Add buttons for the third row
table9_img_data = Image.open("table.png")
table9_img = CTkImage(dark_image=table9_img_data, light_image=table9_img_data, size=(45, 45))
table9 = CTkButton(master=table_row3_frame, image=table9_img, text="Table 9", text_color='black', fg_color="#D3D3D3", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda: update_selected_table(9))
table9.pack(side='left', padx=(16, 0), pady=(0, 0))

table10_img_data = Image.open("table.png")
table10_img = CTkImage(dark_image=table10_img_data, light_image=table10_img_data, size=(45, 45))
table10 = CTkButton(master=table_row3_frame, image=table10_img, text="Table 10", text_color='black', fg_color="#D3D3D3", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda: update_selected_table(10))
table10.pack(side='left', padx=(16, 0), pady=(0, 0))

table11_img_data = Image.open("table.png")
table11_img = CTkImage(dark_image=table11_img_data, light_image=table11_img_data, size=(45, 45))
table11 = CTkButton(master=table_row3_frame, image=table11_img, text="Table 11", text_color='black', fg_color="#D3D3D3", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda: update_selected_table(11))
table11.pack(side='left', padx=(16, 0), pady=(0, 0))

table12_img_data = Image.open("table.png")
table12_img = CTkImage(dark_image=table12_img_data, light_image=table12_img_data, size=(45, 45))
table12 = CTkButton(master=table_row3_frame, image=table12_img, text="Table 12", text_color='black', fg_color="#D3D3D3", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=lambda: update_selected_table(12))
table12.pack(side='left', padx=(16, 0), pady=(0, 0))
#========================Order Frame====================================================================
order_frame = CTkFrame(master=tab_2, fg_color="#fff", width=680, height=335, corner_radius=0)
order_frame.pack_propagate(0)
order_frame.pack(side='top', pady=(16, 10))

# order_label=CTkLabel(master=order_frame, text="Place Order", font=("Arial Black", 25), text_color="#2A8C55")
# order_label.grid(row=0,column=0,columnspan=3)
message_label_2 = CTkLabel(master=order_frame, text="Message Will Appear Here!",width=100)
message_label_2.grid(row=0, column=0, columnspan=3, pady=(10, 0), sticky="n")

# cust_id_label=CTkLabel(master=order_frame, text="Customer ID:", font=("Arial Bold", 20), text_color="#2A8C55")
# cust_id_label.grid(row=1,column=0,padx=10, pady=10,sticky='w')
# cust_id_entry=CTkEntry(master=order_frame, width=305, placeholder_text="Enter Customer ID", border_color="#2A8C55", border_width=2)
# cust_id_entry.grid(row=2,column=0,padx=10, pady=10)

cust_name_label=CTkLabel(master=order_frame, text="Customer Name:", font=("Arial Bold", 20), text_color="#2A8C55")
cust_name_label.grid(row=1,column=0,padx=10, pady=10,sticky='w')
cust_name_entry=CTkEntry(master=order_frame, width=305, placeholder_text="Enter Customer Name", border_color="#2A8C55", border_width=2)
cust_name_entry.grid(row=2,column=0,padx=10, pady=10)

cust_ph_label = CTkLabel(master=order_frame, text="Customer Contact:", font=("Arial Bold", 20), text_color="#2A8C55")
cust_ph_label.grid(row=3,column=0,padx=10, pady=10,sticky='w')
cust_ph_entry=CTkEntry(master=order_frame, width=305, placeholder_text="Enter Customer Contact Details", border_color="#2A8C55", border_width=2)
cust_ph_entry.grid(row=4,column=0,padx=10, pady=10)

cust_add_label = CTkLabel(master=order_frame, text="Customer Address:", font=("Arial Bold", 20), text_color="#2A8C55")
cust_add_label.grid(row=5,column=0,padx=10, pady=10,sticky='w')
cust_add_entry=CTkEntry(master=order_frame, width=305, placeholder_text="Enter Customer Address", border_color="#2A8C55", border_width=2)
cust_add_entry.grid(row=6,column=0,padx=10, pady=10)

sel_table_label = CTkLabel(master=order_frame, text="Table No:", font=("Arial Bold", 20), text_color="#2A8C55")
sel_table_label.grid(row=1,column=1,padx=10, pady=10,sticky='w')
sel_table_entry=CTkEntry(master=order_frame, width=305, placeholder_text="Choose Table from Tables List", border_color="#2A8C55", border_width=2)
sel_table_entry.grid(row=2,column=1,padx=10, pady=10)

def update_selected_table(table_number):
    sel_table_entry.delete(0, tk.END)  # Clear any existing text in sel_table_entry
    sel_table_entry.insert(tk.END, f"Table {table_number}")

#order_id_entry=CTkEntry(master=order_frame, width=305, placeholder_text="Enter Order ID", border_color="#2A8C55", border_width=2)
#order_id_entry.grid(row=5,column=1,padx=10, pady=10)
order_button = CTkButton(master=order_frame, text="Generate Order", font=("Arial Bold", 14),anchor='w', fg_color="#2A8C55", bg_color="#2A8C55", hover_color="#207244", command=lambda:generate_order(app))
order_button.grid(row=3,column=1,columnspan=2,padx=10,pady=10)

new_order_button = CTkButton(master=order_frame, text="New Order", font=("Arial Bold", 14),anchor='w', fg_color="#2A8C55", bg_color="#2A8C55", hover_color="#207244", command=lambda:new_order(app))
new_order_button.grid(row=4,column=1,columnspan=2,padx=10,pady=10)

def new_order(app):
    # Clear app.tree
    app.tree.delete(*app.tree.get_children())

    # Clear all entry fields
    cust_name_entry.delete(0, tk.END)
    cust_ph_entry.delete(0, tk.END)
    cust_add_entry.delete(0, tk.END)
    sel_table_entry.delete(0, tk.END)
    message_label_2.configure(text="To Place New Order Go To Terminal", text_color='#2A8C55')


tree_frame = CTkFrame(master=tab_2, fg_color="#2A8C55", width=680, height=335, corner_radius=10)
tree_frame.pack_propagate(0)
tree_frame.pack(side='top', pady=(16, 10))

app.tree2 = ttk.Treeview(tree_frame, columns=("Order ID","Customer ID","Item ID","Customer Name","Table No","Ordered Item","Quantity","Price",),show="headings", style="Treeview")
app.tree2.grid(row=1, column=0, columnspan=4, sticky="nsew")

app.tree2_scroll_y = ttk.Scrollbar(tree_frame, orient="vertical", command=app.tree2.yview)
app.tree2_scroll_y.grid(row=1, column=4, sticky="ns")

app.tree2_scroll_x = ttk.Scrollbar(tree_frame, orient="horizontal", command=app.tree2.xview)
app.tree2_scroll_x.grid(row=2, column=0, columnspan=4, sticky="ew")

app.tree2.configure(yscrollcommand=app.tree2_scroll_y.set, xscrollcommand=app.tree2_scroll_x.set)
bg_color = "#fff"
text_color = "#000000"
selected_color = "#2A8C55"

treestyle = ttk.Style()
treestyle.theme_use('default')
treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
treestyle.map('Treeview', background=[('selected', selected_color)], foreground=[('selected', text_color)])

tree_frame.bind("<<TreeviewSelect>>", lambda event: tree_frame.focus_set())

# Configure column headings
app.tree2.heading("Order ID", text="Order ID")
app.tree2.heading("Customer ID", text="Customer ID")
app.tree2.heading("Item ID", text="Item ID")
app.tree2.heading("Customer Name", text="Customer Name")
app.tree2.heading("Table No", text="Table No")
app.tree2.heading("Ordered Item", text="Ordered Item")
app.tree2.heading("Quantity", text="Quantity")
app.tree2.heading("Price", text="Price")

# Configure column widths
column_widths = [80,80,60,90,90,90,50,70]
for i, width in enumerate(column_widths):
    app.tree2.column(i, width=width, anchor='center')

current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M:%S")
def generate_order(app):
    table_id = sel_table_entry.get().split()[1]  # Extract table number from the text
    cust_name = cust_name_entry.get()  # Get customer name
    cust_contact = cust_ph_entry.get()
    cust_add = cust_add_entry.get()

    if not cust_name:  # Check if any required field is empty
        message_label_2.configure(text="Customer Name is Mandatory", text_color='#FF0000')
    else:
        try:
            # Insert data into Customer table
            cur = connection.cursor()
            cur.execute("INSERT INTO Customer (Customer_Name, Customer_Contact, Customer_Address) VALUES (?, ?, ?)", (cust_name, cust_contact, cust_add))
            connection.commit()

            # Retrieve Latest Customer ID
            cur.execute("SELECT @@IDENTITY")
            cust_id = cur.fetchone()[0]

            # Get current date and time
            current_date = datetime.now().date()
            current_time = datetime.now().time()

            # Insert data into Orders table with current date and time
            cur.execute("INSERT INTO Orders (Customer_ID, Order_Date, Order_Time, Table_ID) VALUES (?, ?, ?, ?)", (cust_id, current_date, current_time, table_id))
            connection.commit()

            # Retrieve the order ID of the newly inserted order
            cur.execute("SELECT @@IDENTITY")
            global order_id
            order_id = cur.fetchone()[0]

            # Get all items from app.tree and count their quantities
            all_items = app.tree.get_children()
            item_quantities = {}
            for item in all_items:
                dish_id = app.tree.item(item, 'values')[0]  # Extract item ID from the item
                if dish_id in item_quantities:
                    item_quantities[dish_id] += 1
                else:
                    item_quantities[dish_id] = 1

            # Process each item and update inventory and OrderedItems table
            for dish_id, quantity in item_quantities.items():
                # Check if the item is available in inventory
                cur.execute("SELECT Item_Quantity FROM Inventory WHERE Item_Name = (SELECT Dish_Name FROM Menu WHERE Dish_ID = ?)", (dish_id,))
                item_quantity = cur.fetchone()

                if item_quantity is not None and item_quantity[0] >= quantity:
                    # Decrement the item quantity in the Inventory table
                    cur.execute("UPDATE Inventory SET Item_Quantity = Item_Quantity - ? WHERE Item_Name = (SELECT Dish_Name FROM Menu WHERE Dish_ID = ?)", (quantity, dish_id))
                    connection.commit()

                    # Insert data into OrderedItems table with the quantity
                    cur.execute("INSERT INTO OrderedItems (Dish_ID, Order_ID, Customer_ID, Quantity) VALUES (?, ?, ?, ?)", (dish_id, order_id, cust_id, quantity))
                    connection.commit()
                else:
                    message_label_2.configure(text=f"Error: Item {dish_id} is out of stock.", text_color='#FF0000')
                    return

            # Fetch all ordered items for the current customer
            cur.execute("SELECT * FROM OrderedItems WHERE Customer_ID = ?", (cust_id,))
            ordered_items = cur.fetchall()

            # Update app.tree2 with ordered items
            for ordered_item in ordered_items:
                dish_id = ordered_item[1]  # Dish ID
                quantity = ordered_item[4]  # Quantity
                # Fetch dish details from Menu table
                cur.execute("SELECT Dish_Name, Dish_Price_PKR FROM Menu WHERE Dish_ID = ?", (dish_id,))
                dish_details = cur.fetchone()
                dish_name = dish_details[0] if dish_details else "Unknown"
                dish_price = dish_details[1] if dish_details else "Unknown"
                app.tree2.insert("", "end", values=(order_id, cust_id, dish_id, cust_name, table_id, dish_name, quantity, dish_price))

            message_label_2.configure(text="Order Placed", text_color='#2A8C55')
        except pyodbc.Error as ex:
            print(f"Error inserting data into the database: {ex}")
            message_label_2.configure(text="Error: Failed to Place Order.", text_color='#FF0000')



#======================Payment Frame=======================================================================

payment_frame = CTkFrame(master=tab_3, fg_color="#eee",  width=450, height=670, corner_radius=0)
payment_frame.pack_propagate(0)
payment_frame.pack(fill="y", anchor="w", side="left")



# Function to calculate total price, tax, and tax percentage
def calculate_total_price():
    total_price = 0
    payment_meth = payment_method_value.get()
    
    for item in app.tree.get_children():
        total_price += float(app.tree.item(item, 'values')[3])  # Assuming price is in the fourth column

    # Calculate tax percentage based on payment method
    if payment_meth == "Card":
        tax_percentage = 0.025  # 2.5%
    elif payment_meth == "Cash":
        tax_percentage = 0.10  # 10%
    elif payment_meth == "Online Transfer":
        tax_percentage = 0.05  # 5%
    else:
        tax_percentage = 0.05  # Default tax percentage if none selected (fallback to 5%)

    tax = total_price * tax_percentage
    total_amount = total_price + tax
    
    # Update the fields in the payment frame
    total_price_entry.delete(0, ctk.END)
    total_price_entry.insert(0, total_price)

    tax_entry.delete(0, ctk.END)
    tax_entry.insert(0, tax)

    total_amount_entry.delete(0, ctk.END)
    total_amount_entry.insert(0, total_amount)

    try:
        cur = connection.cursor()
        cur.execute("INSERT INTO Payments (Order_ID, Payment_Method, Payment_Amount) VALUES (?, ?, ?)", (order_id, payment_meth, total_amount))
        connection.commit()
    except pyodbc.Error as ex:
        print(f"Error: {ex}")


payment_label=CTkLabel(master=payment_frame, text="Payment", font=("Arial Black", 25), text_color="#2A8C55")
payment_label.grid(row=0,column=0,columnspan=4)

total_price_label=CTkLabel(master=payment_frame, text="Total Price:", font=("Arial Bold", 20), text_color="#2A8C55")
total_price_label.grid(row=1,column=0,padx=10, pady=10,sticky='w')
total_price_entry=CTkEntry(master=payment_frame, width=305, placeholder_text="Price", border_color="#2A8C55", border_width=2)
total_price_entry.grid(row=2,column=0,columnspan=2,padx=10, pady=10)


tax_label = CTkLabel(master=payment_frame, text="Tax(%):", font=("Arial Bold", 20), text_color="#2A8C55")
tax_label.grid(row=3,column=0,padx=10, pady=10,sticky='w')
tax_entry=CTkEntry(master=payment_frame, width=305, placeholder_text="Tax", border_color="#2A8C55", border_width=2)
tax_entry.grid(row=4,column=0,columnspan=2,padx=10, pady=10)

total_amount_label = CTkLabel(master=payment_frame, text="Total Amount:", font=("Arial Bold", 20), text_color="#2A8C55")
total_amount_label.grid(row=5,column=0,padx=10, pady=10,sticky='w')
total_amount_entry=CTkEntry(master=payment_frame, width=305, placeholder_text="Amount", border_color="#2A8C55", border_width=2)
total_amount_entry.grid(row=6,column=0,columnspan=2,padx=10, pady=10)

payment_method=CTkLabel(master=payment_frame, text="Payment Method:", font=("Arial Bold", 20), text_color="#2A8C55")
payment_method.grid(row=7,column=0,padx=10, pady=10,sticky='w')
payment_method_value=CTkComboBox(master=payment_frame, width=305, values=["Cash", "Online Transfer", "Card"], button_color="#2A8C55", border_color="#2A8C55", border_width=2,
     button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
payment_method_value.grid(row=8,column=0,columnspan=2,padx=10, pady=10)
#=================PrintBill============
#=================PrintBill============
def create_bill_pdf(file_name, app):
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch

    pdf = SimpleDocTemplate(file_name, pagesize=letter)

    # Add a logo and restaurant details at the top
    logo = Image('Restaurant Logo.png', 1.5*inch, 1.5*inch)
    logo.hAlign = 'CENTER'
    
    restaurant_name = Paragraph('MAGESTIC CAFE', ParagraphStyle(name='Heading1', fontSize=18, alignment=1, spaceAfter=12))
    restaurant_contact = Paragraph('Contact: (+92) 304-1237890', ParagraphStyle(name='Normal', fontSize=12, alignment=1, spaceAfter=12))

    # Create a table for customer details
    customer_details_data = [
        ['Customer Name:', cust_name_entry.get()],
        ['Customer Address:', cust_add_entry.get()],
        ['Customer Phone:', cust_ph_entry.get()],
        ['Date:', current_date],
        ['Time:', current_time],
    ]
    customer_details_table = Table(customer_details_data)
    customer_details_table.setStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('BACKGROUND', (0,0), (-1,-1), colors.lightblue),  # Add a light blue background
    ])

    # Create a table for ordered items
    ordered_items_data = [['Item ID', 'Name', 'Quantity', 'Unit Price', 'Total Price']]
    for item in app.tree2.get_children():
        data = app.tree2.item(item, 'values')
        if data:
            quantity = int(data[6])  # Assuming quantity is in the third column
            unit_price = float(data[7])  # Assuming price is in the fourth column
            total_price = quantity * unit_price
            ordered_items_data.append([data[2], data[5], quantity, unit_price, total_price])
    ordered_items_table = Table(ordered_items_data)
    ordered_items_table.setStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),  # Add a light gray background to the header row
    ])

    # Create a table for order details
    order_details_data = [['Order ID:', app.tree2.item(app.tree2.get_children()[0], 'values')[0]],
                          ['Customer ID:', app.tree2.item(app.tree2.get_children()[0], 'values')[1]],
                          ['Table No:', app.tree2.item(app.tree2.get_children()[0], 'values')[4]]]
    for item in app.tree2.get_children():
        data = app.tree2.item(item, 'values')
        if data:
            order_details_data.append(['Item ID:', data[2]])
            order_details_data.append(['Price:', data[6]])
    order_details_table = Table(order_details_data)
    order_details_table.setStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('BACKGROUND', (0,0), (-1,-1), colors.lightblue),  # Add a light blue background
    ])

    # Create a table for payment details
    payment_details_data = [
        ['Total Price:', total_price_entry.get()],
        ['Tax:', tax_entry.get()],  # Removing the '%' sign from the tax value
        ['Total Amount:', total_amount_entry.get()],
        ['Payment Method:', payment_method_value.get()],
    ]
    payment_details_table = Table(payment_details_data)
    payment_details_table.setStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('BACKGROUND', (0,0), (-1,-1), colors.lightblue),  # Add a light blue background
    ])

    # Add elements to the PDF
    elems = [
        logo,
        restaurant_name,
        restaurant_contact,
        Spacer(1, 12),
        customer_details_table,
        Spacer(1, 12),
        ordered_items_table,
        Spacer(1, 12),
        order_details_table,
        Spacer(1, 12),
        payment_details_table,
        Spacer(1, 12),
        Paragraph('Thank you for your business!', ParagraphStyle(name='Normal', fontName='Helvetica', fontSize=12, leading=15, alignment=1)),
    ]
    pdf.build(elems)

def print_bill(app):
    # Create a PDF file
    pdf_file = "bill.pdf"
    create_bill_pdf(pdf_file, app)
    open_pdf_with_default_app(pdf_file)

def open_pdf_with_default_app(file_name):
    import os
    if os.name == 'nt':  # Windows
        os.startfile(file_name)
    elif os.name == 'posix':  # Linux, Mac
        os.system('open ' + file_name)


# Button to trigger calculation of payment
calculate_img_data = Image.open("calculate bill.png")
calculate_img = CTkImage(dark_image=calculate_img_data, light_image=calculate_img_data, size=(45,45))
calculate_button = CTkButton(master=payment_frame,image=calculate_img, text="Calculate Payment", font=("Arial Bold", 14), fg_color="#2A8C55",anchor='w',bg_color="#2A8C55", hover_color="#207244", command=lambda:calculate_total_price())
calculate_button.grid(row=9,column=0,columnspan=2,padx=10,pady=10)

print_img_data = Image.open("bill.png")
print_img = CTkImage(dark_image=print_img_data, light_image=print_img_data, size=(45,45))
print_button = CTkButton(master=payment_frame,image=print_img, text="Print Bill", font=("Arial Bold", 14),anchor='w', fg_color="#2A8C55", bg_color="#2A8C55", hover_color="#207244", command=lambda:print_bill(app))
print_button.grid(row=10,column=0,columnspan=2,padx=10,pady=10)


# payment=CTkButton(master=payment_frame, text="Payment",bg_color="#2A8C55" ,fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w",corner_radius=20,command=lambda:payment_tab())
# payment.pack(anchor="center", ipady=10, pady=(16, 0))

# def payment_tab():
#             payment_window = CTkToplevel(app)  # create window if its None or destroyed
#             payment_window.title("Payment")
#             payment_window.geometry("400x400")
#             payment_window.focus()  # if window exists focus it



# def load_menu_data(connection,ap64p):
#     if connection is not None:
#         try:
#             cur = connection.cursor()
#             cur.execute("SELECT * FROM Menu")
#             menu_data = cur.fetchall()

#             # Clear existing items in the Treeview
#             for record in app.tree.get_children():
#                 app.tree.delete(record)

#             # Insert data into the Treeview
#             for item in menu_data:
#                 # Format category to ensure it doesn't overflow
#                 formatted_category = "{:<20}".format(item[2])  # Adjust width as needed

#                 # Insert formatted data into Treeview
#                 app.tree.insert("", ctk.END, values=(item[0], item[1], formatted_category, item[3]))

#             connection.commit()
#             #app.message_label.config(text='Menu Loaded Successfully!',foreground='green')
#         except pyodbc.Error as ex:
#             print(f"Error fetching data from the database: {ex}")
#             message_label.config(text='Failed to Load Menu!',foreground='red')
#     else:
#         print("Database connection is not established.")

def find_id():
        id_term = search_entry.get()
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
        if len(search_term)==0:
            message_label_1.configure(text="Please Enter Item Name or ID to Search",text_color='#FF0000')

        elif connection is not None:
            try:
                    cur = connection.cursor()
                    if radio_var.get() == 1:  # Searching by ID
                        cur.execute("SELECT * FROM Menu WHERE Dish_ID LIKE ?", ('%' + search_term + '%',))
                    elif radio_var.get() == 2:  # Searching by name
                        cur.execute("SELECT * FROM Menu WHERE Dish_Name LIKE ?", ('%' + search_term + '%',))
                    menu_data = cur.fetchall()
                    # Clear existing items in the Treeview
                    for record in app.tree1.get_children():
                        app.tree1.delete(record)

                    # Insert data into the Treeview
                    for item in menu_data:
                        app.tree1.insert("", ctk.END, values=item)

                    connection.commit()
                    message_label_1.configure(text='Item Found Successfully!',text_color="#2A8C55")
                    if(len(menu_data)==0):
                        message_label_1.configure(text="Item not Found",text_color='#FF0000')
            except pyodbc.Error as ex:
                print(f"Error searching data from the database: {ex}")
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
            #load_menu_data(connection,app)
            app.mainloop()
        finally:
            # Close the database connection
            connection.close()
    else:
        print("Failed to establish a database connection.")
