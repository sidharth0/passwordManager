from dbManager import create_connection, DATABASE
import dbManager
import tkinter as tk
from tkinter import messagebox
from encryption import encrypt_message,decrypt_message
from passGenerator import generatePass
from savePass import save
from search import search


def login(window,loginButton,signupButton):
    def setup():
        db = create_connection(DATABASE)
        row=db.execute(f'SELECT * FROM userInfo WHERE username="{loginName.get()}"')
        res=row.fetchone()
        enteredPass=loginPass.get()
        enteredPass=enteredPass.encode()
        if res is None or enteredPass!=decrypt_message(res[1]):
            messagebox.showinfo(title="Wrong Credentials",message="Wrong username or Password !")
        else:

            dbManager.KEY=res[2]
            dbManager.USERNAME=loginName.get()
            loginWin.destroy()
            loginButton.destroy()
            signupButton.destroy()
            label1 = tk.Label(window, text="Website")
            label1.grid(column=0, row=1, sticky='w')
            label2 = tk.Label(window, text="Email/Username")
            label2.grid(column=0, row=2, sticky='w')
            label3 = tk.Label(window, text="Password")
            label3.grid(column=0, row=3, sticky='w')

            site_entry = tk.Entry(window)
            site_entry.grid(row=1, column=1, sticky='we')
            site_entry.focus()
            searchSite=tk.Button(window,text="Search",command=lambda:search(site_entry.get()))
            searchSite.grid(row=1,column=2,sticky='we')
            username_entry = tk.Entry(window)
            username_entry.grid(row=2, column=1, columnspan=2, sticky='we')
            username_entry.insert(0, "sidharth@gmail.com")
            password_entry = tk.Entry(window)
            password_entry.grid(row=3, column=1, sticky='we')

            generatePass_but = tk.Button(window, text="Generate Password", command=lambda:generatePass(password_entry))
            generatePass_but.grid(row=3, column=2)
            store_but = tk.Button(window, text="SAVE/ADD", command=lambda:save(username_entry,password_entry,site_entry))
            store_but.grid(row=4, column=1, columnspan=2, sticky="we")
    loginWin = tk.Toplevel(window)
    loginWin.title("Login")
    loginWin.config(padx=10, pady=10)
    loginNameLabel = tk.Label(loginWin, text="Username", padx=10, pady=5)
    loginPassLabel = tk.Label(loginWin, text="Password", padx=10, pady=5)
    loginName = tk.Entry(loginWin)
    loginPass = tk.Entry(loginWin)

    submit = tk.Button(loginWin, text="Submit", command=setup)
    loginNameLabel.grid(column=0, row=0, sticky='w')
    loginPassLabel.grid(column=0, row=1, sticky='w')
    loginName.grid(column=1, row=0)
    loginPass.grid(column=1, row=1)
    submit.grid(column=0, row=2, columnspan=2, sticky='ew')


