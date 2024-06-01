from customtkinter import *
from PIL import Image
from tkinter import ttk

app = CTk()
app.geometry("1400x670")
#app.resizable(0, 0)

set_appearance_mode("light")

sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55", width=180, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))

label1 = CTkLabel(master=sidebar_frame, text="", image=logo_img)
label1.pack(pady=(38, 10), anchor="center")

# Create a canvas to contain the buttons
canvas = CTkCanvas(master=sidebar_frame, width=180, height=650, bg="#2A8C55", highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

# Create a frame inside the canvas to contain the buttons
button_frame = CTkFrame(canvas, fg_color="#2A8C55")
canvas.create_window((0, 0), window=button_frame, anchor="nw")

#=============Appetizer=================
appetizer_img_data = Image.open("appetizer.png")
appetizer_img = CTkImage(dark_image=appetizer_img_data, light_image=appetizer_img_data, size=(45, 45))
appetizer = CTkButton(master=button_frame, image=appetizer_img, text="Appetizer", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
appetizer.pack(anchor="center", ipady=10, pady=(16, 0))
#==============Soup=====================
soup_img_data = Image.open("soup.png")
soup_img = CTkImage(dark_image=soup_img_data, light_image=soup_img_data, size=(45, 45))
soup = CTkButton(master=button_frame, image=soup_img, text="Soup", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
soup.pack(anchor="center", ipady=10, pady=(16, 0))
#===============Salad===================
salad_img_data = Image.open("salad.png")
salad_img = CTkImage(dark_image=salad_img_data, light_image=salad_img_data, size=(45, 45))
salad = CTkButton(master=button_frame, image=salad_img, text="Salad", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
salad.pack(anchor="center", ipady=10, pady=(16, 0))
#==============Seafood====================
seafood_img_data = Image.open("seafood.png")
seafood_img = CTkImage(dark_image=seafood_img_data, light_image=seafood_img_data, size=(45, 45))
seafood = CTkButton(master=button_frame, image=seafood_img, text="Seafood", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
seafood.pack(anchor="center", ipady=10, pady=(16, 0))
#===============Burger======================
burger_img_data = Image.open("burger.png")
burger_img = CTkImage(dark_image=burger_img_data, light_image=burger_img_data, size=(45, 45))
burger = CTkButton(master=button_frame, image=burger_img, text="Burger", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
burger.pack(anchor="center", ipady=10, pady=(16, 0))
#===============Rice=======================
rice_img_data = Image.open("fried-rice.png")
rice_img = CTkImage(dark_image=rice_img_data, light_image=rice_img_data, size=(45, 45))
rice = CTkButton(master=button_frame, image=rice_img, text="Rice", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
rice.pack(anchor="center", ipady=10, pady=(16, 0))

# Create a vertical scrollbar
scrollbar = ttk.Scrollbar(sidebar_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="left", fill="y")

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Function to update the canvas scroll region
def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Bind the canvas to the function to update scroll region
button_frame.bind("<Configure>", update_scroll_region)

app.mainloop()
