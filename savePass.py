# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
import tkinter as tk
import dbManager
from encryption import encrypt_message
import json


def save(username_entry, password_entry, site_entry):
    site = site_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(site) < 1 or len(password) < 1 or len(username) < 1:
        msg = f"Please add valid credentials !"
        messagebox.showwarning(message=msg)
    else:
        msg = f"Are you sure you want to save the Password Information to database\nSite:{site}\nUsername:{username}\nPassword:{password}"
        choice = messagebox.askyesno(message=msg)
        new_data={encrypt_message(site).decode():{
            "username":encrypt_message(username).decode(),
            "password":encrypt_message(password).decode()
        }}
        if choice:
            try:
                with open(f"save{dbManager.USERNAME}.txt", 'r') as file:
                    data=json.load(file)
            except FileNotFoundError:
                with open(f"save{dbManager.USERNAME}.txt", 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open(f"save{dbManager.USERNAME}.txt", 'w') as file:
                    data.update(new_data)
                    json.dump(data,file,indent=4)
            finally:
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                site_entry.delete(0, tk.END)
