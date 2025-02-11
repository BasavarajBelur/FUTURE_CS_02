import tkinter as tk
from tkinter import messagebox, Label
import re
import hashlib
from PIL import Image,ImageTk


# Function to check the password strength
def check_password_strength(password):
        # Regular expressions for password strength checks
        length_check = len(password) >= 8
        lower_check = re.search(r'[a-z]', password)
        upper_check = re.search(r'[A-Z]', password)
        digit_check = re.search(r'[0-9]', password)
        special_check = re.search(r'[\W_]', password)

        # Password strength conditions
        if length_check and lower_check and upper_check and digit_check and special_check:
            return "Strong"
        elif length_check and (lower_check or upper_check) and digit_check:
            return "Moderate"
        else:
            return "Weak"

    # Function to hash the password
def hash_password(password):
        # Hashing the password using SHA256
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return hashed

    # Function to handle the "Check Strength" button click
def on_check_button_click():
        password = password_entry.get()
        if password == "":
            messagebox.showwarning("Input Error", "Please enter a password")
            return
        
        strength = check_password_strength(password)
        result_label.config(text=f"Password Strength: {strength}")

    # Function to handle the "Hash Password" button click
def on_hash_button_click():
        password = password_entry.get()
        if password == "":
            messagebox.showwarning("Input Error", "Please enter a password")
            return
        
        hashed_password = hash_password(password)
        hashed_label.config(text=f"Hashed Password: {hashed_password}")

    # Creating the main window
root = tk.Tk()
root.title("Password Strength Analyzer Tool")
root.geometry("400x300")


img=Image.open(r"C:\Users\win11\OneDrive\Desktop\Futer _intern\bg4.png")
img=img.resize((1500,1500))
photoimg=ImageTk.PhotoImage(img)

# set image as lable
f_lb1 = Label(root,image=photoimg)
f_lb1.place(x=0,y=0,width=1500,height=1500)

# TITLE 
title_lb1 = Label(root,text="WELCOME TO PASSWORD STRENGTH ANALYZER TOOL",font=("times new roman",30,"bold"),bg="white",fg="navyblue")
title_lb1.place(x=0,y=0,width=1500,height=45)


# Label for password input
password_label = tk.Label(root, text="Enter your password:",font=("times new roman",20,"bold"),background="white",fg="navyblue",width=16)
password_label.pack(pady=70)

# Entry widget for password
password_entry = tk.Entry(root,font=("times new roman",15,"bold"),background="white",fg="black")
password_entry.place(x=690,y=130,width=170,height=30)

# Button to check password strength
check_button = tk.Button(root, text="Check Strength",command=on_check_button_click,font=("times new roman",20,"bold"),background="white",fg="navyblue",width=14)
check_button.pack(pady=10)

        # Label to display the password strength result
result_label = tk.Label(root, text="Password Strength: Not Checked",font=("times new roman",20,"bold"),background="white",fg="navyblue",width=25)
result_label.pack(pady=15)

    # Button to hash the password
hash_button = tk.Button(root, text="Hash Password", command=on_hash_button_click,font=("times new roman",20,"bold"),background="white",fg="navyblue",width=14)
hash_button.pack(pady=50)

    # Label to display the hashed password
hashed_label = tk.Label(root, text="Hashed Password: Not Generated",font=("times new roman",20,"bold"),background="white",fg="navyblue",width=70)
hashed_label.pack(pady=5)


    # Run the main loop
root.mainloop()
