from cProfile import label
from tkinter import *

from numpy.random.mtrand import geometric

"""
top=Tk()

M=Menu(top)
M.add_command(label="breakfast")
M.add_command(label="lunch")
M.add_command(label="dinner")

top.config(menu=M)
top.mainloop()
"""

top=Tk()
M=Menu(top)
BOTTOM=Tk()

M=Menu(BOTTOM)
M.add_command(label="home")
M.add_command(label="edit")
M.add_command(label="design")
M.add_command(label="file")
M.add_separator()
M.add_command(label="quit")
BOTTOM.config(menu=M)
M.add_cascade(label="File", menu=M)
"""edit.add_command(label="undo")
edit.add_separator()
edit.add_command(label="cut")
edit.add_command(label="copy")
edit.add_command(label="paste")
edit.add_command(label="delete")
edit.add_command(label="select all")

M.add_cascade(label="edit",menu=edit)
help=M(M,tearoff=0)
help.add_cascade(label="help",menu=help)"""


BOTTOM.config(menu=M)
BOTTOM.mainloop()


