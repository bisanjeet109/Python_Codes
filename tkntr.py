
#T K I N T E R----------------------------------------------------------------------------------------

"""
check nox----
that allows to select multiple option from the multiple choices
all these checkboxex usually available on one frame in a group format
from this group we can select multiple values agt the same time.

*RADIO BUTTON---------
it provides the facility to opt any one option from the multiple options usually a group of radio buttons are available on this same and allows us to select any one option from that group

*SPINNER----------------------
it is also known as publish bar and usually use to denote the completion or th progress towards completion towards the program

these all gui widgets are also known as windgets means window gadgets
"""


"""
import tkinter as tk
m = tk.Tk()
greeting=tk.Label (text="this is my first Gui program",
                   foreground="silver",
                   background="black",
                   width=100,
                   height=90,)
greeting.pack()                                           #pack is used to group all the objects present in the window
m.mainloop()                       #calling the whole loop 

"""


"""

from tkinter import *
import tkinter as tk

bisanjeet=Tk()

info_Tf=Entry(bisanjeet)
info_Tf.insert(END,"these are the last char")

bisanjeet.mainloop()
"""


"""
entry boxes are single line only
height is required to facilitate multiple ine input.
height keyword is used & it takes an integer as input.
multiple line entry boxes are also called textarea.
insert keyword is used to insert the word or sentence.
ENDdetermine the text char sjould beentered immidiately after the last character 

"""

"""
from tkinter import *
import tkinter as tk
ws=Tk()
ws.geometry("400x400")
msg="my first program"
text_box=Text(
    ws,
    height=25,
    width=50,
    background="black",
    foreground="silver",
    wrap="word",
    font=("arial",10,"bold"))

text_box.pack(expand=True)
text_box.insert(END,msg)
ws.mainloop()
"""

#wap to input name and address sof an student .for this it should display 2 laBEL BOXXES,TO INFORM THE CANDIDATE,where to write the name and where to write the address.it should cioontain 2 boxes
# to take the name in a single line
#to take the address in multiple line
#The colour of both the labels should be diff.
#The captions must be in bold and black color
"""
import tkinter as tk
from tkinter import font


ws= tk.Tk()

ws.geometry("400x400")


bold_font = font.Font(family="Arial", size=10, )


name_label = tk.Label(
    ws,
    bg="blue",
    font=bold_font,
    text="Enter Name:",
    fg="black",)
name_label.pack()


name_entry = tk.Entry(ws, width=40)
name_entry.pack()


address_label = tk.Label(
    ws,
    text="Enter Address:",
    fg="black",
    bg="yellow",
    font=bold_font
)
address_label.pack()


address_text = tk.Text(ws, width=40, height=5)
address_text.pack()


ws.mainloop()

"""

"""
Q.create the indian tricolour flag wit the help of lebels  
"""

"""
import tkinter as tk
from tkinter import font

flag= tk.Tk()

flag.geometry("400x400")



bold_font = font.Font(family="Arial", size=10, )


maroon_label = tk.Label(
    flag,
    bg="maroon",
    font=bold_font,
    text="__________________________________",
    fg="maroon",)
maroon_label.pack()


maroon_entry = tk.Entry(flag, width=40)
maroon_entry.pack()


white_label = tk.Label(
    flag,

    bg="white",
    text="_________________________________",
    fg="white", )
white_label.pack()

white_entry = tk.Entry(flag, width=40)
white_entry.pack()

green_label = tk.Label(
    flag,

    bg="green",
    text="_________________________________",
    fg="green", )
green_label.pack()

green_entry = tk.Entry(flag, width=40)
green_entry.pack()
flag.mainloop()
"""

#correction--------------
"""
import tkinter as tk
import math

# Create window
root = tk.Tk()
root.title("Indian Tricolor Flag")

# Canvas
canvas = tk.Canvas(root, width=450, height=300)
canvas.pack()

# Flag dimensions
width = 450
height = 300
stripe_height = height // 3

# Draw stripes
canvas.create_rectangle(0, 0, width, stripe_height, fill="#FF9933", outline="")
canvas.create_rectangle(0, stripe_height, width, 2*stripe_height, fill="white", outline="")
canvas.create_rectangle(0, 2*stripe_height, width, height, fill="#138808", outline="")

# Draw Ashoka Chakra
center_x = width // 2
center_y = height // 2
radius = 40

# Outer circle
canvas.create_oval(center_x - radius, center_y - radius,
                   center_x + radius, center_y + radius,
                   outline="navy", width=2)


for i in range(24):
    angle = math.radians(i * 15)  # 360/24 = 15 degrees
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    canvas.create_line(center_x, center_y, x, y, fill="navy", width=1)

root.mainloop()
"""


"""
Q.creation of text boxex with the help of user defined function---------------------
.wap to display first 15 students of the class.on the basis of reg no. .The text area must contain two scroll bars one in vertical and one in horizontal scrolling.

"""

import tkinter as tk


root = tk.Tk()
root.title("Student List")


frame = tk.Frame(root)
frame.pack()


x_scroll = tk.Scrollbar(frame, orient="horizontal")
y_scroll = tk.Scrollbar(frame, orient="vertical")


text_area = tk.Text(
    frame,
    wrap="none",
    xscrollcommand=x_scroll.set,
    yscrollcommand=y_scroll.set,
    width=20,
    height=15,
    bg="black",
    fg="white",
    font=("Arial", 12),


)


x_scroll.config(command=text_area.xview)
y_scroll.config(command=text_area.yview)


x_scroll.pack(side="bottom", fill="x")
y_scroll.pack(side="right", fill="y")
text_area.pack(side="left", fill="both", expand=True)


students = [
    (101, "Aman"), (102, "Riya"), (103, "Rahul"), (104, "Sneha"),
    (105, "Arjun"), (106, "Priya"), (107, "Karan"), (108, "Neha"),
    (109, "Vikram"), (110, "Anjali"), (111, "Rohit"), (112, "Simran"),
    (113, "Aditi"), (114, "Varun"), (115, "Meena"),
]


students.sort()


for reg, name in students:
    text_area.insert(tk.END, f"Reg No: {reg}   Name: {name}\n")


root.mainloop()

#wap that can display 3 lebels with the name text area ,input box and the scroll bar.infront of each label,display the object i.e written in the caption
