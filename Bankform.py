"""
import tkinter as tk
import tkinter as messagebox

root = tk.Tk()
root.title("Bank Form")
root.geometry("500x500")

tk.Label(root, text="Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Account No").pack()
acc = tk.Entry(root)
acc.pack()

tk.Label(root, text="IFSC").pack()
ifsc = tk.Entry(root)
ifsc.pack()

tk.Label(root, text="savings acc").pack()
savings_acc = tk.Entry(root)
savings_acc.pack()


tk.Button(root, text="Submit").pack()

root.mainloop()

"""
#display the message boxes on this form iin the following way
#1-by opening the form it should display the info box consisting the name of the bank and the welcome message
#2-whenever the user opt for the withdrawal option the warning message box should be display with the message  min m  500 rs wil be in uyr acc
#3- whenever the use click in the deposit opt the message box should ask a question whether it is a joint acc or individual
#4-whenever the use click on the enquiry button display one error message ,visit to the branch for any enquiries
import tkinter as tk
from tkinter import messagebox

from matplotlib_inline.backend_inline import show

"""

def withdraw():
    messagebox.showwarning("Warning", "Minimum 500 Rs will remain in your account")


def deposit():
    result = messagebox.askquestion("Deposit", "Is this a Joint Account?")

    if result == "yes":
        messagebox.showinfo("Type", "Joint Account Selected")
    else:
        messagebox.showinfo("Type", "Individual Account Selected")


def enquiry():
    messagebox.showerror("Error", "Visit the branch for any enquiries")


def submit():
    name_val = name.get()
    acc_val = acc.get()




root = tk.Tk()
root.title("Bank Form")
root.geometry("350x400")


root.after(100, lambda: messagebox.showinfo("Welcome", "ABC Bank\nWelcome to our service"))


tk.Label(root, text="Name").pack()
tk.Label(root, text="Account Number").pack()
name = tk.Entry(root)
acc = tk.Entry(root)
acc.pack()
name.pack()


tk.Button(root, text="Withdraw", command=withdraw).pack(pady=5)

tk.Button(root, text="Deposit", command=deposit).pack(pady=5)
tk.Button(root, text="Enquiry", command=enquiry).pack(pady=5)
tk.Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()
"""

#2nd questian
def name():
    messagebox.showwarning("bisanjeet", "name should be 10 char minm")


def mobile():
    result = messagebox.askquestion("mobile number", "minm 10 character")


def enquiry():
    messagebox.showerror("Error", "form is wrong")


def submit():
    name_val = name.get()


root = tk.Tk()
root.title("student_add_form")
root.geometry("350x400")
tk.Label(root, text="Name").pack()
tk.Label(root, text="Account Number").pack()

tk.Button(root, text="ug", command=show()).pack(pady=5)

root.mainloop()




