#LIST BOX

from tkinter import *
"""
from numpy.ma.core import left_shift

top=Tk()

Lb1=Listbox(top)

Lb1.insert(1,"python")
Lb1.insert(2,"java")
Lb1.insert(3,"c++")
Lb1.insert(4,"ruby")
Lb1.insert(5,"javascript")

Lb2=Listbox(top)
Lb2.insert(1,"c++")
Lb2.insert(2,"ruby")

Lb2.pack()

Lb1.pack()
top.mainloop()
"""
#spinbox------------------------------------------------------------------------------
"""
root=Tk()
t1=StringVar()
List_2=["one","two","three","four","five","six","seven","eight"]
spnbx_1=Spinbox(root,from_=0,to=8,textvariable=t1)
t1.set("two")


spnbx_1.pack()
root.mainloop()

"""
#create a spinbox with the name of all ur courses and display and highlight the code python programming------------
"""
root=Tk()
t1=StringVar()
List_2=["python","java","c++","ruby","javascript","DCN","BDA"]
spnbx_1=Spinbox(root,from_=0,to=7,textvariable=t1)
t1.set("python")
spnbx_1.pack()
root.mainloop()
"""

#msgbox---------------------------------------------------------------------
from tkinter import messagebox
root=Tk()
root.geometry("500x600")

messagebox.showinfo("university","tomorrow is holiday")
messagebox.showwarning("class Teacher","Submit the assignments pon time")
messagebox.showerror("student","i am not able to solve it")

messagebox.askquestion("parents","why u have short attendence")
messagebox.askokcancel("friend","will u join for cofee")
messagebox.askyesno("results","are u promoted for next class")
messagebox.askretrycancel("online course","do u want to join")


root=mainloop()