import tkinter
from tkinter import messagebox
import password_generator
import pyperclip
import json

FONT = ('Times New Roman', 13, 'bold')
BUTTON_FONT = ('Arial', 9, 'bold')
BUTTON_BG = 'saddlebrown'
BG = 'wheat'


# Add Button Functionality

def add_func():
    website = website_input.get().capitalize()
    email = Email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please Don't leave any of the fields empty")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\nIs it okay?")
    if not is_ok:
        return

    new_item = {
        website: {
            "email": email,
            "password": password
        }
    }
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", 'w') as file:
            json.dump(new_item, file, indent=4)
    else:
        if website in data:
            flag = messagebox.askokcancel(title="Already Exists", message="The given credentials will replace the old credentials for this website")
            if not flag:
                return
            data[website] = {"email": email, "password": password}

        else:
            data.update(new_item)

        with open("data.json", 'w') as file:
            json.dump(data, file, indent=4)
    finally:
        messagebox.showinfo(title="Message", message="Credentials successfully saved")
        website_input.delete(0, tkinter.END)
        password_input.delete(0, tkinter.END)


# Search Button Functionality

def search_func():
    website = website_input.get()
    if len(website) == 0:
        messagebox.showinfo(title="Message", message="Empty fields are not entertained")
        return
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="No credentials found for the given website")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(text=password)
        else:
            messagebox.showinfo(title="Not Found", message="No credentials found for the given website")


# Reset Button Functionality

def reset_func():
    website_input.delete(0, tkinter.END)
    password_input.delete(0, tkinter.END)
    Email_input.delete(0, tkinter.END)


# Generate Button Functionality

def generate():
    password_input.delete(0, tkinter.END)
    password = password_generator.generate_password()
    password_input.insert(0, password)
    pyperclip.copy(password)


# Main window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=BG)
window.minsize(width=600, height=500)

# canvas
canvas = tkinter.Canvas(width=300, height=250, bg=BG, highlightthickness=0)
image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(150, 125, image=image)
canvas.grid(row=0, column=1)

# Website Label
website_label = tkinter.Label(text="Website : ", font=FONT, bg=BG)
website_label.grid(row=1, column=0)

# Website Input
website_input = tkinter.Entry(width=31, font=('Arial', 12))
website_input.focus()
website_input.grid(row=1, column=1, ipadx=5, ipady=5, pady=5, padx=5)

# Search Button
search_button = tkinter.Button(text="Search".upper(), font=BUTTON_FONT, bg=BUTTON_BG, width=10, command=search_func)
search_button.grid(row=1, column=2, ipadx=5, ipady=5, pady=5, padx=0)

# Email Label
Email_label = tkinter.Label(text="Email/Username : ", font=FONT, bg=BG)
Email_label.grid(row=2, column=0)

# Email Input
Email_input = tkinter.Entry(width=42, font=('Arial', 12))
Email_input.insert(0, "user@gmail.com")
Email_input.grid(row=2, column=1, columnspan=2, ipadx=5, ipady=5, pady=5, padx=5)

# Password Label
password_label = tkinter.Label(text="Password : ", font=FONT, bg=BG)
password_label.grid(row=3, column=0)

# Password Input
password_input = tkinter.Entry(width=31, font=('Arial', 12))
password_input.grid(row=3, column=1, ipadx=5, ipady=5, pady=5, padx=0)

# Generate Button
generate_button = tkinter.Button(text="Generate".upper(), font=BUTTON_FONT, bg=BUTTON_BG, width=10, command=generate)
generate_button.grid(row=3, column=2, ipadx=5, ipady=5, pady=5, padx=0)

# Add Button
add_button = tkinter.Button(text="ADD", width=52, font=BUTTON_FONT, bg=BUTTON_BG, command=add_func)
add_button.grid(row=4, column=1, columnspan=2, ipadx=5, ipady=5, pady=5)

# Reset Button
reset_button = tkinter.Button(text="RESET", width=52, font=BUTTON_FONT, bg=BUTTON_BG, command=reset_func)
reset_button.grid(row=5, column=1, columnspan=2, ipady=5, ipadx=5, padx=5, pady=5)

window.mainloop()
