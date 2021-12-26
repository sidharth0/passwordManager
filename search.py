import encryption
import dbManager
import tkinter as tk
import json
from tkinter import messagebox
def search(site):
    c=0
    try:
        with open(f"save{dbManager.USERNAME}.txt", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        c=1
        messagebox.showerror(title="Credential file Missing",message=f"Unable to retrieve save{dbManager.USERNAME} file")
    else:
        for (key,value) in data.items():
            print(encryption.decrypt_message(key.encode()))
            if encryption.decrypt_message(key.encode()).decode()==site:
                messagebox.showinfo(title="Site Found",message=f"Site:{encryption.decrypt_message(key.encode()).decode()}\nUsername:{encryption.decrypt_message(value['username'].encode()).decode()}\nPassword:{encryption.decrypt_message(value['password'].encode()).decode()}")
                c=2

                break
    if c==0:
        messagebox.showinfo(title="Site Not Found",message="The searched site is not in database.")

