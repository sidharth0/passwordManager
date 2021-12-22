import tkinter as tk
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePass():
    capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    nos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    spChar = ['@', '#', '!', '$', '&']
    capital_no = random.randint(8, 12)
    small_no = random.randint(4, 8)
    nos_no = random.randint(2, 4)
    sp_no = random.randint(2, 4)
    capitals = [random.choice(capital) for _ in range(capital_no)]
    smalls = [random.choice(small) for _ in range(small_no)]
    numbers = [random.choice(nos) for _ in range(nos_no)]
    sps = [random.choice(spChar) for _ in range(sp_no)]
    password_str = capitals + smalls + numbers + sps
    random.shuffle(password_str)
    passwordGen = ''
    for i in password_str:
        passwordGen += i
    password_entry.delete(0,tk.END)
    password_entry.insert(0,passwordGen)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = site_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(site) < 1 or len(password) < 1 or len(username) < 1:
        msg = f"Please add valid credentials !"
        messagebox.showwarning(message=msg)
    else:
        msg = f"Are you sure you want to save the Password Information to database\nSite:{site}\nUsername:{username}\nPassword{password} "
        choice = messagebox.askyesno(message=msg)
        with open("save.txt", 'a') as file:
            if choice:
                file.write(f"Site:{site},Username:{username},Password{password}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = tk.Canvas(height=200, width=200)
logoImage = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImage)
canvas.grid(column=1, row=0)

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

generatePass_but = tk.Button(text="Generate Password",command=generatePass)
generatePass_but.grid(row=3, column=2)
store_but = tk.Button(text="SAVE/ADD", command=save)
store_but.grid(row=4, column=1, columnspan=2, sticky="we")

window.mainloop()
