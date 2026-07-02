import tkinter as tk
"""
window=tk.Tk()
window.title("my first program")
window.geometry("500x500")
label=tk.Label(text="my first program",font=("Arial",25))
label.pack()
label.config(text="my first program")

user_input=tk.Entry(show="*")
user_input.pack()

def function_button():
    label.config(text="button clicked",font=("algerian",18))

button=tk.Button(text="clicked",command=function_button)
button.pack()
quit_button=tk.Button(text="quit",command=window.destroy)
quit_button.pack()
window.mainloop()
"""
#destroy method to quit window-----------------------
"""window=tk.Tk()
window.title=("exam")
window.geometry("500x500")
label=tk.Label(text="hello",font=("Arial",20))
label.pack()
button=tk.Button(text="clicked",command=window.destroy)
button.pack()

window.mainloop()"""


import tkinter as tk
from tkinter import messagebox

# ---------- Event Function ----------
def submit():
    name = entry_name.get()
    roll = entry_roll.get()
    branch = branch_listbox.get(tk.ACTIVE)
    age = spin_age.get()
    address = text_address.get("1.0", tk.END)

    result = f"Name: {name}\nRoll: {roll}\nBranch: {branch}\nAge: {age}\nAddress: {address}"
    messagebox.showinfo("Student Details", result)

# ---------- Root Window ----------
root = tk.Tk()
root.title("Student Form")
root.geometry("400x500")

# ---------- Menu ----------
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# ---------- Widgets ----------
tk.Label(root, text="Student Form", font=("Arial", 16)).pack()

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Roll No").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

# Listbox (Branch selection)
tk.Label(root, text="Select Branch").pack()
branch_listbox = tk.Listbox(root)
branch_listbox.insert(1, "CSE")
branch_listbox.insert(2, "IT")
branch_listbox.insert(3, "ECE")
branch_listbox.pack()

# Spinbox (Age)
tk.Label(root, text="Age").pack()
spin_age = tk.Spinbox(root, from_=18, to=30)
spin_age.pack()

# Text widget (Address)
tk.Label(root, text="Address").pack()
text_address = tk.Text(root, height=4)
text_address.pack()

# Button (event trigger)
tk.Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()


