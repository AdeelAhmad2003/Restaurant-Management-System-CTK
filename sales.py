from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import pyodbc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
from datetime import datetime
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
app = CTk()
app.geometry("1200x670")
app.resizable(0, 0)

set_appearance_mode("light")

# Sidebar frame setup
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55", width=250, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))
label1 = CTkLabel(master=sidebar_frame, text="", image=logo_img)
label1.pack(pady=(38, 10), anchor="center")

# Scrollable frame for buttons
button_frame = CTkScrollableFrame(master=sidebar_frame, fg_color="#2A8C55", label_text="Menu")
button_frame.pack(fill="both", expand=True)

# Sales Report buttons
daily_img_data = Image.open("report.png")
daily_img = CTkImage(dark_image=daily_img_data, light_image=daily_img_data)
daily_button = CTkButton(master=button_frame, image=daily_img, text="Daily Report", fg_color="transparent",
                         font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda: generate_sales_report("daily"))
daily_button.pack(anchor="center", ipady=10, pady=(16, 0))

weekly_img_data = Image.open("report.png")
weekly_img = CTkImage(dark_image=weekly_img_data, light_image=weekly_img_data)
weekly_button = CTkButton(master=button_frame, image=weekly_img, text="Weekly Report", fg_color="transparent",
                          font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda: generate_sales_report("weekly"))
weekly_button.pack(anchor="center", ipady=10, pady=(16, 0))

monthly_img_data = Image.open("report.png")
monthly_img = CTkImage(dark_image=monthly_img_data, light_image=monthly_img_data)
monthly_button = CTkButton(master=button_frame, image=monthly_img, text="Monthly Report", fg_color="transparent",
                           font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda: generate_sales_report("monthly"))
monthly_button.pack(anchor="center", ipady=10, pady=(16, 0))

annual_img_data = Image.open("report.png")
annual_img = CTkImage(dark_image=annual_img_data, light_image=annual_img_data)
annual_button = CTkButton(master=button_frame, image=annual_img, text="Annual Report", fg_color="transparent",
                          font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda: generate_sales_report("annual"))
annual_button.pack(anchor="center", ipady=10, pady=(16, 0))

# Profit Report buttons
daily_profit_button = CTkButton(master=button_frame, image=daily_img, text="Daily Profit", fg_color="transparent",
                                font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda: generate_profit_report("daily_profit"))
daily_profit_button.pack(anchor="center", ipady=10, pady=(16, 0))

weekly_profit_button = CTkButton(master=button_frame, image=weekly_img, text="Weekly Profit", fg_color="transparent",
                                 font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda: generate_profit_report("weekly_profit"))
weekly_profit_button.pack(anchor="center", ipady=10, pady=(16, 0))

monthly_profit_button = CTkButton(master=button_frame, image=monthly_img, text="Monthly Profit", fg_color="transparent",
                                  font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda: generate_profit_report("monthly_profit"))
monthly_profit_button.pack(anchor="center", ipady=10, pady=(16, 0))

annual_profit_button = CTkButton(master=button_frame, image=annual_img, text="Annual Profit", fg_color="transparent",
                                 font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda: generate_profit_report("annual_profit"))
annual_profit_button.pack(anchor="center", ipady=10, pady=(16, 0))

# Additional Analysis buttons
repeated_customers_button = CTkButton(master=button_frame, image=annual_img, text="Repeated Customers", fg_color="transparent",
                                      font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda:generate_repeated_customers_report())
repeated_customers_button.pack(anchor="center", ipady=10, pady=(16, 0))

items_selling_ratio_button = CTkButton(master=button_frame, image=annual_img, text="Items Selling Ratio", fg_color="transparent",
                                       font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda:generate_items_selling_ratio_report())
items_selling_ratio_button.pack(anchor="center", ipady=10, pady=(16, 0))

inventory_status_button = CTkButton(master=button_frame, image=annual_img, text="Inventory Status", fg_color="transparent",
                                    font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda:generate_inventory_status_report())
inventory_status_button.pack(anchor="center", ipady=10, pady=(16, 0))
# Sales Report Frame
report_frame = CTkFrame(master=app, fg_color="#fff", width=1000, height=670, corner_radius=0)
report_frame.pack_propagate(0)
report_frame.pack(side="left", fill="both", expand=True)

# Today's summary
summary_frame = CTkFrame(master=report_frame, fg_color="#f7f7f7", width=1000, height=50, corner_radius=0)
summary_frame.pack_propagate(0)
summary_frame.pack(fill="x", anchor="n")

total_orders_label = CTkLabel(master=summary_frame, text="Total Orders Today: ", font=("Arial Bold", 14), text_color="#2A8C55")
total_orders_label.pack(side="left", padx=20, pady=10)

total_revenue_label = CTkLabel(master=summary_frame, text="Today's Revenue: ", font=("Arial Bold", 14), text_color="#2A8C55")
total_revenue_label.pack(side="left", padx=20, pady=10)

message_label = CTkLabel(master=report_frame, text="Report will be displayed here!", font=("Arial Bold", 18), text_color="#2A8C55")
message_label.pack(pady=20)

# Database connection function
def connect_to_database(server, database):
    try:
        connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        print("Database connection established successfully!")
        return connection
    except pyodbc.Error as ex:
        print(f"Error connecting to the database: {ex}")
        messagebox.showerror("Database Connection Error", "Failed to connect to the database.")
        return None

def fetch_data(query):
    try:
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return data
    except pyodbc.Error as ex:
        print(f"Error fetching data from the database: {ex}")
        messagebox.showerror("Database Error", "Failed to fetch data from the database.")
        return []

# Generate report function
# Generate sales report
def generate_sales_report(report_type):
    query = ""
    title = ""
    
    if report_type == "daily":
        query = """
            SELECT CONVERT(date, o.Order_Date) AS Payment_Date, SUM(p.Payment_Amount) AS Total_Amount
            FROM Payments p
            JOIN Orders o ON p.Order_ID = o.Order_Id
            GROUP BY CONVERT(date, o.Order_Date)
        """
        title = "Daily Sales Report"
    elif report_type == "weekly":
        query = """
            SELECT DATEPART(week, o.Order_Date) AS Week, SUM(p.Payment_Amount) AS Total_Amount
            FROM Payments p
            JOIN Orders o ON p.Order_ID = o.Order_Id
            GROUP BY DATEPART(week, o.Order_Date)
        """
        title = "Weekly Sales Report"
    elif report_type == "monthly":
        query = """
            SELECT DATEPART(month, o.Order_Date) AS Month, SUM(p.Payment_Amount) AS Total_Amount
            FROM Payments p
            JOIN Orders o ON p.Order_ID = o.Order_Id
            GROUP BY DATEPART(month, o.Order_Date)
        """
        title = "Monthly Sales Report"
    elif report_type == "annual":
        query = """
            SELECT DATEPART(year, o.Order_Date) AS Year, SUM(p.Payment_Amount) AS Total_Amount
            FROM Payments p
            JOIN Orders o ON p.Order_ID = o.Order_Id
            GROUP BY DATEPART(year, o.Order_Date)
        """
        title = "Annual Sales Report"
    
    data = fetch_data(query)
    if data:
        dates, amounts = zip(*data)
        for widget in report_frame.winfo_children():
            widget.destroy()
        plot_chart(dates, amounts, title, "Amount", "Date", "line", ["green"])
    else:
        for widget in report_frame.winfo_children():
            widget.destroy()
        message_label = CTkLabel(master=report_frame, text="No data available for the selected report type.", font=("Arial Bold", 18), text_color="#FF0000")
        message_label.pack(pady=20)

# Generate profit report
def generate_profit_report(report_type):
    query = ""
    title = ""
    
    if report_type == "daily_profit":
        query = """
            SELECT 
                CONVERT(date, o.Order_Date) AS Payment_Date, 
                SUM(p.Payment_Amount) - SUM(i.Item_Price * oi.Quantity) AS Total_Profit
            FROM 
                Payments p
            JOIN 
                Orders o ON p.Order_ID = o.Order_Id
            JOIN 
                OrderedItems oi ON o.Order_Id = oi.Order_ID
            JOIN 
                Inventory i ON oi.Dish_ID = i.Item_ID
            GROUP BY 
                CONVERT(date, o.Order_Date)
        """
        title = "Daily Profit Report"
    elif report_type == "weekly_profit":
        query = """
            SELECT 
                DATEPART(week, o.Order_Date) AS Week, 
                SUM(p.Payment_Amount) - SUM(i.Item_Price * oi.Quantity) AS Total_Profit
            FROM 
                Payments p
            JOIN 
                Orders o ON p.Order_ID = o.Order_Id
            JOIN 
                OrderedItems oi ON o.Order_Id = oi.Order_ID
            JOIN 
                Inventory i ON oi.Dish_ID = i.Item_ID
            GROUP BY 
                DATEPART(week, o.Order_Date)
        """
        title = "Weekly Profit Report"
    elif report_type == "monthly_profit":
        query = """
            SELECT 
                DATEPART(month, o.Order_Date) AS Month, 
                SUM(p.Payment_Amount) - SUM(i.Item_Price * oi.Quantity) AS Total_Profit
            FROM 
                Payments p
            JOIN 
                Orders o ON p.Order_ID = o.Order_Id
            JOIN 
                OrderedItems oi ON o.Order_Id = oi.Order_ID
            JOIN 
                Inventory i ON oi.Dish_ID = i.Item_ID
            GROUP BY 
                DATEPART(month, o.Order_Date)
        """
        title = "Monthly Profit Report"
    elif report_type == "annual_profit":
        query = """
            SELECT 
                DATEPART(year, o.Order_Date) AS Year, 
                SUM(p.Payment_Amount) - SUM(i.Item_Price * oi.Quantity) AS Total_Profit
            FROM 
                Payments p
            JOIN 
                Orders o ON p.Order_ID = o.Order_Id
            JOIN 
                OrderedItems oi ON o.Order_Id = oi.Order_ID
            JOIN 
                Inventory i ON oi.Dish_ID = i.Item_ID
            GROUP BY 
                DATEPART(year, o.Order_Date)
        """
        title = "Yearly Profit Report"
    
    data = fetch_data(query)
    if data:
        dates, amounts = zip(*data)
        for widget in report_frame.winfo_children():
            widget.destroy()
        plot_chart(dates, amounts, title, "Amount", "Date", "bar", ["red"])
    else:
        for widget in report_frame.winfo_children():
            widget.destroy()
        message_label = CTkLabel(master=report_frame, text="No data available for the selected report type.", font=("Arial Bold", 18), text_color="#FF0000")
        message_label.pack(pady=20)
def generate_repeated_customers_report():
    query = """
    SELECT c.Customer_Name, COUNT(*) AS Order_Count
    FROM OrderedItems o
    JOIN Customer c ON o.Customer_ID = c.Customer_ID
    GROUP BY c.Customer_Name
    HAVING COUNT(*) > 1
        """
    data = fetch_data(query)
    if data:
        customers, counts = zip(*data)
        plot_pie_chart(customers, counts, "Repeated Customers")
    else:
        for widget in report_frame.winfo_children():
            widget.destroy()
        global message_label
        message_label = CTkLabel(master=report_frame, text="No repeated customers found.", font=("Arial Bold", 18), text_color="#FF0000")
        message_label.pack(pady=20)


def generate_items_selling_ratio_report():
    query = """
        SELECT m.Dish_Name, COUNT(oi.Order_ID) AS Order_Count
        FROM OrderedItems oi
        JOIN Menu m ON oi.Item_ID = m.Dish_ID
        GROUP BY m.Dish_Name
    """
    title = "Items Selling Ratio Report"
    
    data = fetch_data(query)
    if data:
        items, counts = zip(*data)
        
        # Clear the previous figure if it exists
        plt.clf()

        # Create a new figure for the pie chart
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.pie(counts, labels=items, autopct='%1.1f%%', colors=plt.cm.Paired.colors, startangle=140)
        ax.set_title(title)

        # Remove previous canvas if it exists
        for widget in report_frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()

        # Create a new canvas and add the pie chart to it
        canvas = FigureCanvasTkAgg(fig, master=report_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

        # Hide the message label if present
        message_label.pack_forget()
    else:
        # Show message if no data is available
        message_label.configure(text="No data available for the items selling ratio report.")
        message_label.pack()
def generate_inventory_status_report():
    query = """
        SELECT i.Item_ID, i.Item_Quantity
        FROM Inventory i
    """
    data = fetch_data(query)
    if data:
        items, quantities = zip(*data)
        plot_bar_chart(items, quantities, "Inventory Status", "Item ID", "Quantity")
    else:
        for widget in report_frame.winfo_children():
            widget.destroy()
        global message_label
        message_label = CTkLabel(master=report_frame, text="No inventory data available.", font=("Arial Bold", 18), text_color="#FF0000")
        message_label.pack(pady=20)
# Plot chart
def plot_chart(dates, amounts, title, ylabel, xlabel, style, colors):
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    if style == "line":
        ax.plot(dates, amounts, color=colors[0])
    elif style == "bar":
        # Filter out None values from amounts
        amounts = [amount for amount in amounts if amount is not None]
        ax.bar(dates[:len(amounts)], amounts, color=colors[0])
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    
    if amounts:  # Only set limits if amounts is not empty
        ax.set_ylim([min(amounts) * 0.95, max(amounts) * 1.05])

    canvas = FigureCanvasTkAgg(fig, master=report_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def plot_pie_chart(labels, sizes, title):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title(title)

    for widget in report_frame.winfo_children():
        widget.destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=report_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

def plot_bar_chart(labels, sizes, title, xlabel, ylabel):
    # Clear existing widgets in report_frame
    for widget in report_frame.winfo_children():
        widget.destroy()

    # Determine colors based on inventory quantities
    colors = ['red' if size <= 10 else 'blue' for size in sizes]

    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Plot the bar chart with specified colors
    ax.bar(labels, sizes, color=colors)

    # Set labels and title
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    # Draw the canvas
    canvas = FigureCanvasTkAgg(fig, master=report_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
def update_summary():
    today = datetime.today().date()
    query_orders = f"""
        SELECT COUNT(*)
        FROM Orders
        WHERE CONVERT(date, Order_Date) = '{today}'
    """
    query_revenue = f"""
        SELECT SUM(Payment_Amount)
        FROM Payments p
        JOIN Orders o ON p.Order_ID = o.Order_Id
        WHERE CONVERT(date, o.Order_Date) = '{today}'
    """
    
    total_orders = fetch_data(query_orders)
    total_revenue = fetch_data(query_revenue)
    
    total_orders_label.configure(text=f"Total Orders Today: {total_orders[0][0] if total_orders else 0}")
    total_revenue_label.configure(text=f"Today's Revenue: RS: {total_revenue[0][0] if total_revenue and total_revenue[0][0] is not None else 0:.2f}")

if __name__ == "__main__":
    server = r'DESKTOP-8RO21S6\SQLEXPRESS'
    database = 'tastytrack'
    
    connection = connect_to_database(server, database)

    if connection is not None:
        update_summary()
        app.mainloop()
        connection.close()
    else:
        print("Failed to establish a database connection.")
