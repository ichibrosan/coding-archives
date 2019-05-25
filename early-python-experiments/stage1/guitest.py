#!/usr/bin/python 
# guitest.py 1/9/2008 COPR doug@goodall.com
# See Programming Python page 500

import ConfigParser
from ScrolledText import ScrolledText
from Tkinter import *
from tkFileDialog import *
from tkMessageBox import *
from tkSimpleDialog import askstring

cfg = ConfigParser.ConfigParser()
filespec = ""
data = ""

def about():
	showerror('Oops','Guitest version 1.0.0.0 Copyright (c) doug@goodall.com ')

def viewfile():
	new = Toplevel()
	text = ScrolledText(new,height=30,width=90)
	text.config(font=('Comic Sans MS',14,'normal'))
	text.pack()
	text.insert('0.0', askopenfile().read(16384))
	
def notdone():
	showerror('Not imp','Not avail')
	
def makemenu(win):
	top = Menu(win)
	win.config(menu=top)
	guitest = Menu(top)
	guitest.add_command(label='About Guitest', command=about, underline=0)
	top.add_cascade(label='Guitest',menu=guitest, underline=0)
	view = Menu(top)
	view.add_command(label='File', command=viewfile, underline=0)
	top.add_cascade(label='View',menu=view,underline=0)
	
root = Tk()
root.title('Guitest')
makemenu(root)
msg = Label(root, text='This space available')
msg.pack(expand=YES, fill=BOTH)
msg.config(relief=SUNKEN, width=80, height=16, bg='beige')
root.mainloop()
