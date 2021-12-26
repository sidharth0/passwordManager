import tkinter as tk
from dbManager import firstRun
from signup import signup
from login import login

firstRun()
# ----------------------------- SETUP ---------------------------------------#

# -------------------------------LOGIN---------------------------------------#



# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = tk.Canvas(height=200, width=200)
logoImage = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImage)
canvas.grid(column=1, row=0)

signupButton = tk.Button(text="SignUp", command=lambda: signup(window))
signupButton.grid(row=1, column=1, sticky='e')
loginButton = tk.Button(text="Login", command=lambda:login(window,loginButton,signupButton))
loginButton.grid(column=1,row=1,sticky='w')

window.mainloop()
