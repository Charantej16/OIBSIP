import tkinter as tk
import random

def generate_password():
    output_entry.delete(0, tk.END)

    try:
        pwd_length = int(length_entry.get())
    except:
        output_entry.insert(0, "Enter valid length")
        return

    character_set = ""

    if letters_var.get():
        character_set += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if numbers_var.get():
        character_set += "0123456789"

    if symbols_var.get():
        character_set += "!@#$%^&*()_+-=[]{}<>?/"

    if character_set == "":
        output_entry.insert(0, "Select at least one option")
        return

    password = ""
    for _ in range(pwd_length):
        index = random.randint(0, len(character_set) - 1)
        password += character_set[index]

    output_entry.insert(0, password)


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_entry.get())


# GUI setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("380x360")
root.resizable(False, False)

# Heading
tk.Label(root, text="🔐 Random Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Password length
tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root, justify="center")
length_entry.pack(pady=5)

# Options
letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Output
output_entry = tk.Entry(root, font=("Arial", 12), justify="center")
output_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy Password", command=copy_to_clipboard).pack(pady=10)

root.mainloop()
