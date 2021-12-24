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
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                site_entry.delete(0, tk.END)