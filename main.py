import string
import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
from pykeepass import PyKeePass

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password():
    password_entry.delete(0, END)

    # Password options
    password_length = 16  # Default length
    include_small_letters = BooleanVar(value=False)
    include_big_letters = BooleanVar(value=False)
    include_digits = BooleanVar(value=False)
    include_punctuation = BooleanVar(value=False)
    include_special_characters = BooleanVar(value=False)

    # Prompt for password options
    password_options_window = Toplevel(window)
    password_options_window.title("Password Options")
    password_options_window.config(padx=20, pady=20)

    # Length Label and Entry
    length_label = Label(password_options_window, text="Password Length:")
    length_label.grid(row=0, column=0, sticky=W)
    length_entry = Entry(password_options_window, width=5)
    length_entry.grid(row=0, column=1, sticky=W)
    length_entry.insert(END, password_length)

    # Options Checkboxes
    small_letters_checkbox = Checkbutton(password_options_window, text="Include Small Letters",
                                         variable=include_small_letters)
    small_letters_checkbox.grid(row=1, column=0, sticky=W)
    big_letters_checkbox = Checkbutton(password_options_window, text="Include Big Letters",
                                       variable=include_big_letters)
    big_letters_checkbox.grid(row=2, column=0, sticky=W)
    digits_checkbox = Checkbutton(password_options_window, text="Include Digits", variable=include_digits)
    digits_checkbox.grid(row=3, column=0, sticky=W)
    punctuation_checkbox = Checkbutton(password_options_window, text="Include Punctuation",
                                       variable=include_punctuation)
    punctuation_checkbox.grid(row=4, column=0, sticky=W)
    special_chars_checkbox = Checkbutton(password_options_window, text="Include Special Characters",
                                         variable=include_special_characters)
    special_chars_checkbox.grid(row=5, column=0, sticky=W)

    def generate_password_with_options():
        nonlocal password_length
        password_length = int(length_entry.get())
        password_options_window.destroy()

        characters = ""
        if include_small_letters.get():
            characters += string.ascii_lowercase
        if include_big_letters.get():
            characters += string.ascii_uppercase
        if include_digits.get():
            characters += string.digits
        if include_punctuation.get():
            characters += string.punctuation
        if include_special_characters.get():
            # Add your own special characters here
            characters += "@#$%"

        password = "".join(random.choice(characters) for _ in range(password_length))
        password_entry.insert(END, password)
        pyperclip.copy(password)

    # Generate Button
    generate_button = Button(password_options_window, text="Generate", command=generate_password_with_options)
    generate_button.grid(row=6, column=0, columnspan=2, pady=10)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_keepass():
    web_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    if len(web_text) == 0 or len(email_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops", message="You have empty fields")
        return

    keepass_file = "Enter your keepass file directory"
    keepass_password = "Enter your password"

    try:
        kp = PyKeePass(keepass_file, password=keepass_password)
    except Exception as e:
        messagebox.showinfo(title="Oops", message="Failed to open Keepass file")
        return

    entry = kp.find_entries(title=web_text)
    if entry:
        entry = entry[0]

        entry.username = email_text
        entry.password = password_text
    else:
        try:
            entry = kp.add_entry(kp.root_group, web_text, email_text, password_text)
        except Exception as e:
            messagebox.showinfo(title="Oops", message="Failed to add entry to Keepass")
            return

    try:
        kp.save()
    except Exception as e:
        messagebox.showinfo(title="Oops", message="Failed to save Keepass file")
        return

    messagebox.showinfo(title="Success", message="Password saved in Keepass")

    website_entry.delete(0, END)
    password_entry.delete(0, END)


def search_entry():
    web_text = website_entry.get()

    if len(web_text) == 0:
        messagebox.showinfo(title="Oops", message="Please enter a website to search")
        return

    keepass_file = "database.kdbx"
    keepass_password = ""

    try:
        kp = PyKeePass(keepass_file, password=keepass_password)
    except Exception as e:
        messagebox.showinfo(title="Oops", message="Failed to open Keepass file")
        return

    entry = kp.find_entries(title=web_text)
    if entry:
        entry = entry[0]
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        email_entry.insert(END, entry.username)
        password_entry.insert(END, entry.password)
    else:
        messagebox.showinfo(title="Not Found", message="No entry found for the website")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(60, 80, image=image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry Fields
website_entry = Entry(width=20)
website_entry.grid(row=1, column=1, sticky=W, columnspan=2, pady=2)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, sticky=W, columnspan=2, pady=2)
email_entry.insert(0, "")

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, sticky=W, pady=2)

# Buttons
generate_password_button = Button(text="Generate Password", width=15, command=random_password)
generate_password_button.grid(row=3, column=1, sticky=E, columnspan=2, pady=2)

add_button = Button(text="Add/Update", width=32, command=save_to_keepass)
add_button.grid(row=4, column=1, padx=2, pady=5)

search_button = Button(text="Search", width=15, command=search_entry)
search_button.grid(row=1, column=1, sticky=E, columnspan=2, padx=2, pady=5)

window.mainloop()
