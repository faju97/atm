"""
    Lesson one 
    Creating GUI 
    Date: 29/09/2022

"""

import tkinter as tk
from tkinter import *
import sqlite3


def login():
    
 #l_window = tk.Tk()
 l_window = Toplevel(window)
 l_window.geometry("500x500")
 l_window.title("OSHWAL COLLEGE BANK")

#Labels
 title_lbl = Label(l_window, text = "Login Page", width = 20, font = ("bold", 20)).pack()

 username_lbl = Label(l_window, text = "Username", width = 20).place(x=80, y=100)
 name_entry = Entry(l_window).place(x=200, y=100)

 password_lbl = Label(l_window, text = "Password", width = 20).place(x=80, y=140)
 name_entry = Entry(l_window).place(x=200, y=140)

 Login_btn = Button(l_window, text = "Login", width = 20).place(x=180, y=180)

def register():
    #r_window = tk.Tk()
    r_window = Toplevel(window)
    r_window.geometry("500x500")
    r_window.title("OSHWAL COLLEGE BANK")

    #Labels
    title_lbl = Label(r_window, text = "Registration Form", width = 20, font = ("bold", 20)).pack()

    fullName = StringVar()
    Email = StringVar()
    contact = IntVar()
    City = StringVar()
    gender_var = IntVar()

    def database():
        name1 = fullName.get()
        email = Email.get()
        phone = contact.get()
        gender = gender_var.get()
        city1 = City.get()

        conn = sqlite3.connect('Regitration.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Registration(fullName TEXT, Email TEXT, contact TEXT, City TEXT, gender_var TEXT)')
            cursor.execute('INSERT INTO Registration(FullName,Email,Contact,City,Gender) VALUES(?, ?, ?, ?, ?)',(name1,email,phone,gender,city1,))
            conn.commit()

    name_lbl = Label(r_window, text = "Full Name", width = 20).place(x=80, y=100)
    name_entry = Entry(r_window).place(x=200, y=100)

    contact_lbl = Label(r_window, text = "Contact", width = 20).place(x=80, y=140)
    name_entry = Entry(r_window).place(x=200, y=140)

    email_lbl = Label(r_window, text = "Email", width = 20).place(x=80, y=180)
    name_entry = Entry(r_window).place(x=200, y=180)

    #list of cities
    city_lbl = Label(r_window, text = "City", width = 20).place(x=80, y=220)
    #name_entry = Entry(r_window).place(x=200, y=220)
    cities_list = ['Nairobi', 'Mombasa', 'Kisumu']
    droplist = OptionMenu(r_window, City, *cities_list)
    droplist.config(width=15)
    droplist.place(x=200, y=220)




    gender_lbl = Label(r_window, text = "Gender", width = 20).place(x=80, y=260)
    Radiobutton(r_window, text = "Male", padx = 5, variable = gender_var, value = 1).place(x=200, y=260)
    Radiobutton(r_window, text = "Female", padx = 5, variable = gender_var, value = 2).place(x=280, y=260)

    submit_btn = Button(r_window, text = "Submit", width = 20).place(x=180, y=300)


















window = tk.Tk()
# window.title()
window.title("OSHWAL COLLEGE BANK")
window.geometry("500x350")
lbl_Header = Label(window, text="OSHWAL COLLEGE ATM" ).pack()
# lbl_Header.place(x=20, y=10)

login_btn = Button(window, text="Login", fg='white', bg='green', width=15, height=2,command=login).place(x=150, y=150)
register_btn = Button(window, text="Register", fg='white', bg='red', width=15, height=2, command=register).place(x=300, y=150)


window.mainloop()




################
