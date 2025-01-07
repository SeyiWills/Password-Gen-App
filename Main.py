import tkinter as tk
import random
import string
import clipboard

# Function to generate a random password
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to copy the generated password to the clipboard
def copy_password():
    password = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    clipboard.copy(password)
    password_label.config(text="Generated Password: " + password)

# Function to copy the generated password to the clipboard
def copy_to_clipboard():
    clipboard.copy(password_entry.get())
    
# Create the GUI
root = tk.Tk()
root.title("Password Generator")
password_label = tk.Label(root, text="Generated Password:")
password_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=copy_password)
copy_button = tk.Button(root, text="Copy Password", command=copy_to_clipboard) 
password_label.pack()
password_entry.pack()
generate_button.pack()
copy_button.pack()
root.mainloop()