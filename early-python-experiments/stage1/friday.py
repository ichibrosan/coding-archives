#!/usr/bin/python
# friday.py 1/9/2008 COPR doug@goodall.com
from Tkinter import * 
import webbrowser

class localvars():
	sProgram = "friday"
	url = "http:/localhost/index.html"
	m1 = "view"
	m1c1 = "exit"
	m2 = "help"
	m2c1 = "about"
	water = "This space available"
	color = "lightblue"
	width = 80
	height = 16

def duh():
	webbrowser.open(local.url)
	
def makemenu(parent):
	menubar = Frame(parent)
	menubar.pack(side=TOP, fill=X)
	fbutton = Menubutton(menubar, text=local.m1, underline=0)
	fbutton.pack(side=LEFT)
	m1 = Menu(fbutton)
	m1.add_command(label=local.m1c1, command=duh, underline=0)
	fbutton.config(menu=m1)
	fbutton = Menubutton(menubar, text=local.m2, underline=0)
	fbutton.pack(side=LEFT)
	m2 = Menu(fbutton)
	m2.add_command(label=local.m2c1, command=duh, underline=0)
	fbutton.config(menu=m2)
	return menubar

local = 	localvars
root = Tk()
root.title(local.sProgram)
makemenu(root)
msg = Label(root, text=local.water)
msg.pack(expand=YES, fill=BOTH)
msg.config(relief=SUNKEN, width=local.width, height=local.height, bg=local.color)
root.mainloop()
