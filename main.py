import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
from passGenerator import generatePass
from savePass import save
from signup import signup
# ----------------------------- SETUP ---------------------------------------#

#-------------------------------LOGIN---------------------------------------#
def login():

    pass

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = tk.Canvas(height=200, width=200)
logoImage = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImage)
canvas.grid(column=1, row=0)

loginButton = tk.Button(text="SignUp", command=signup)
loginButton.grid(row=0, column=2, sticky='en')
loginButton=tk.Button(text="Login",command=login)


label1 = tk.Label(text="Website")
label1.grid(column=0, row=1, sticky='w')
label2 = tk.Label(text="Email/Username")
label2.grid(column=0, row=2, sticky='w')
label3 = tk.Label(text="Password")
label3.grid(column=0, row=3, sticky='w')

site_entry = tk.Entry()
site_entry.grid(row=1, column=1, columnspan=2, sticky='we')
site_entry.focus()
username_entry = tk.Entry()
username_entry.grid(row=2, column=1, columnspan=2, sticky='we')
username_entry.insert(0, "sidharth@gmail.com")
password_entry = tk.Entry()
password_entry.grid(row=3, column=1, sticky='we')

generatePass_but = tk.Button(text="Generate Password", command=generatePass)
generatePass_but.grid(row=3, column=2)
store_but = tk.Button(text="SAVE/ADD", command=save)
store_but.grid(row=4, column=1, columnspan=2, sticky="we")

window.mainloop()
