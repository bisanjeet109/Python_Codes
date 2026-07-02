"""file=open("example.txt","r")
content=file.readlines()
print(content)
file.close()"""
"""file=open("example.txt","a")
file.write("namaste,kaise ho main  ISA HO ")
file.write("\n thik hhhhh")
file.close()"""

import tkinter as tk
from tkinter import messagebox, Button

# ---------- Event Function ----------
"""def submit():
    name = entry_name.get()
    acc = entry_acc.get()
    amount = spin_amount.get()
    account_type = acc_listbox.get(tk.ACTIVE)
    details = text_details.get("1.0", tk.END)

    result = f"Name: {name}\nAccount No: {acc}\nType: {account_type}\nAmount: {amount}\nDetails: {details}"
    messagebox.showinfo("Bank Info", result)"""


def submit():
    messagebox.showinfo("bankform","data saved")

# ---------- Root Window ----------
root = tk.Tk()
root.title("Bank Form")
root.geometry("400x500")

# ---------- Menu ----------
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Options", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# ---------- Widgets ----------
tk.Label(root, text="Bank Form", font=("Arial", 16)).pack()

(tk.Label(root, text="Account Holder Name").pack())
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Account Number").pack()
entry_acc = tk.Entry(root)
entry_acc.pack()

# Listbox (Account Type)
tk.Label(root, text="Account Type").pack()
acc_listbox = tk.Listbox(root)
acc_listbox.insert(1, "Savings")
acc_listbox.insert(2, "Current")
acc_listbox.insert(3, "Fixed Deposit")
acc_listbox.pack()

# Spinbox (Amount)
tk.Label(root, text="Amount").pack()
spin_amount = tk.Spinbox(root, from_=100, to=100000)
spin_amount.pack()

# Text widget (Extra details)
tk.Label(root, text="Details").pack()
#text_details = tk.Text(root, height=4)
tk.Entry(root,width=20)


# Button
button=tk.Button(text="clicked",command=root.destroy)
button.pack()

messagebox.showinfo("operation success")
root.mainloop()
