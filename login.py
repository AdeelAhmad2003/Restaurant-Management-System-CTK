from customtkinter import *
from PIL import Image
import pyodbc
from tkinter import messagebox
from user import user_file 

class DatabaseManager:
    def __init__(self, server, database, driver='SQL Server'):
        self.connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trust_Connection=yes;'
        self.conn = None

    def connect(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            print("Connection success")
        except pyodbc.Error as ex:
            print(f"Error connecting to the database: {ex}")

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def find_user(self, username, password):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Employee WHERE Employee_Username=? AND Employee_Password=?"
        cursor.execute(query, (username, password,))
        data = cursor.fetchone()
        cursor.close()
        return data

    def find_admin(self, username, password):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Admin WHERE Username=? AND Password=?"
        cursor.execute(query, (username, password,))
        data = cursor.fetchone()
        cursor.close()
        return data

class LoginPage:
    def __init__(self, root, database_manager):
        self.root = root
        self.db_manager = database_manager

        self.root.geometry("700x480")
        self.root.resizable(0,0)

        side_img_data = Image.open("Restaurant Logo.png")
        email_icon_data = Image.open("email-icon.png")
        password_icon_data = Image.open("password-icon.png")

        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(400, 480))
        email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
        password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))

        CTkLabel(master=self.root, text="", image=side_img).pack(expand=True, side="left")

        self.frame = CTkFrame(master=self.root, width=300, height=480, fg_color="#ffffff")
        self.frame.pack_propagate(0)
        self.frame.pack(expand=True, side="right")

        CTkLabel(master=self.frame, text="Welcome Back!", text_color="#2A8C55", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=self.frame, text="Sign in to your account", text_color="#2A8C55", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=self.frame, text="  ID:", text_color="#2A8C55", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        self.username_entry = CTkEntry(master=self.frame, width=225, fg_color="#EEEEEE", border_color="#2A8C55", border_width=1, text_color="#000000")
        self.username_entry.pack(anchor="w", padx=(25, 0))

        CTkLabel(master=self.frame, text="  Password:", text_color="#2A8C55", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        self.password_entry = CTkEntry(master=self.frame, width=225, fg_color="#EEEEEE", border_color="#2A8C55", border_width=1, text_color="#000000", show="*")
        self.password_entry.pack(anchor="w", padx=(25, 0))

        CTkButton(master=self.frame, text="Login", fg_color="#2A8C55", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=self.login).pack(anchor="w", pady=(40, 0), padx=(25, 0))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user_data = self.db_manager.find_user(username, password)
        if user_data:
            messagebox.showinfo("Login", "User Login Successful")
            self.root.destroy()
            user_file()

        else:
            admin_data = self.db_manager.find_admin(username, password)
            if admin_data:
                messagebox.showinfo("Login", "Admin Login Successful")
            else:
                messagebox.showerror("Login", "Invalid Username or Password")

def main():
    server = 'DESKTOP-DTNJB1H\SQLEXPRESS'
    database = 'tastytrack'

    db_manager = DatabaseManager(server, database)

    try:
        db_manager.connect()

        root = CTk()
        login_page = LoginPage(root, db_manager)
        root.mainloop()

    except pyodbc.Error as ex:
        print(f"Error connecting to the database: {ex}")
    finally:
        db_manager.disconnect()

if __name__ == "__main__":
    main()
