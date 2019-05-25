#!/usr/bin/python
# scrollbar-example-1.py

from Tkinter import *

root = Tk()
print root.geometry()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)
listbox.bell()
scrollbar.config(command=listbox.yview)

mainloop()
print root.geometry()
