import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password using the specified length
    return ''.join(random.choice(characters) for _ in range(length))

def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be a positive number.")
        else:
            password = generate_password(length)
            entry_password.delete(0, tk.END)
            entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

def copy_to_clipboard():
    password = entry_password.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("No Password", "No password to copy.")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#fcfcfa")  # Set background color

# Center the window on screen
window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
root.resizable(False, False)

# Widgets
label_title = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#fcfcfa", fg="#000000")
label_title.pack(pady=10)

label_length = tk.Label(root, text="Enter password length:", font=("Helvetica", 12), bg="#fcfcfa", fg="#000000")
label_length.pack()

entry_length = tk.Entry(root, font=("Helvetica", 12), justify="center", bg="#d6d6d6")
entry_length.pack(pady=5)

btn_generate = tk.Button(root, text="Generate Password", font=("Helvetica", 12, "bold"), bg="#7c02f5", fg="#fcfcfa", command=on_generate)
btn_generate.pack(pady=5)

entry_password = tk.Entry(root, font=("Helvetica", 12), justify="center", bg="#d6d6d6", fg="#000000", relief="flat")
entry_password.pack(pady=5)

btn_copy = tk.Button(root, text="Copy to Clipboard", font=("Helvetica", 12, "bold"), bg="#7c02f5", fg="#fcfcfa", command=copy_to_clipboard)
btn_copy.pack(pady=5)

# Start the application
root.mainloop()
