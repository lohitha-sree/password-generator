import random
import string
import tkinter as tk
from tkinter import messagebox

# ---------------- PASSWORD GENERATOR FUNCTION ----------------
def create_password():
    try:
        length = int(entry_length.get())
        use_letters = var_letters.get()
        use_numbers = var_numbers.get()
        use_symbols = var_symbols.get()

        if length <= 0:
            messagebox.showerror("Oops!", "Password length must be more than 0!")
            return

        pool = ""
        if use_letters:
            pool += string.ascii_letters
        if use_numbers:
            pool += string.digits
        if use_symbols:
            pool += string.punctuation

        if not pool:
            messagebox.showerror("Oops!", "Select at least one character type!")
            return

        new_password = ''.join(random.choice(pool) for _ in range(length))
        entry_password.config(state="normal")
        entry_password.delete(0, tk.END)
        entry_password.insert(0, new_password)
        entry_password.config(state="readonly")
    except ValueError:
        messagebox.showerror("Oops!", "Please enter a valid number for length!")

# ---------------- COPY FUNCTION ----------------
def copy_to_clipboard():
    pwd = entry_password.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Done!", "Password copied!")

# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("Random Password Maker")
root.geometry("420x320")
root.resizable(False, False)
root.config(bg="#262626")

# Labels
tk.Label(root, text="Enter desired password length:", bg="#262626", fg="white", font=("Arial", 12)).pack(pady=(20, 5))
entry_length = tk.Entry(root, font=("Arial", 12), width=10)
entry_length.pack()

# Checkboxes
var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include letters", variable=var_letters, bg="#262626", fg="white", selectcolor="#262626").pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include numbers", variable=var_numbers, bg="#262626", fg="white", selectcolor="#262626").pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include symbols", variable=var_symbols, bg="#262626", fg="white", selectcolor="#262626").pack(anchor="w", padx=60)

# Buttons
tk.Button(root, text="Generate!", command=create_password, bg="#ff6347", fg="white", font=("Arial", 12, "bold")).pack(pady=15)
tk.Button(root, text="Copy Password", command=copy_to_clipboard, bg="#32cd32", fg="white", font=("Arial", 12, "bold")).pack()

# Entry to display password
entry_password = tk.Entry(root, font=("Arial", 14), width=30, state="readonly", justify="center")
entry_password.pack(pady=20)

root.mainloop()