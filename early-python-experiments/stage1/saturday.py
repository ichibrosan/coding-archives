#!/usr/bin/python
# saturday.py 1/12/2008 COPR doug@goodall.com
from Tkinter import * 
import webbrowser

class localvars():
	sProgram = "friday"
	url = "http:/localhost/index.html"
	#
	m1 = "Project"
	m1c1 = "New"
	m1c1_url = "http://localhost/m1c1.html"
	m1c2 = "Add"
	m1c2_url = "http://localhost/m1c2.html"
	m1c3 = "Delete"
	m1c3_url = "http://localhost/m1c3.html"
	m1c4 = "View"
	m1c4_url = "http://localhost/m1c4.html"
	m1c5 = "Print"
	m1c5_url = "http://localhost/m1c5.html"
	#
	m2 = "Requirements"
	m2c1 = "New"
	m2c1_url = "http://localhost/m2c1.html"
	m2c2 = "Add"
	m2c2_url = "http://localhost/m2c2.html"
	m2c3 = "Delete"
	m2c3_url = "http://localhost/m2c3.html"
	m2c4 = "View"
	m2c4_url = "http://localhost/m2c4.html"
	m2c5 = "Print"
	m2c5_url = "http://localhost/m2c5.html"
	#
	m3 = "Design"
	m3c1 = "New"
	m3c1_url = "http://localhost/m3c1.html"
	m3c2 = "Add"
	m3c2_url = "http://localhost/m3c2.html"
	m3c3 = "Delete"
	m3c3_url = "http://localhost/m3c3.html"
	m3c4 = "View"
	m3c4_url = "http://localhost/m3c4.html"
	m3c5 = "Print"
	m3c5_url = "http://localhost/m3c5.html"
	#
	m4 = "Modularization"
	m4c1 = "New"
	m4c1_url = "http://localhost/m4c1.html"
	m4c2 = "Add"
	m4c2_url = "http://localhost/m4c2.html"
	m4c3 = "Delete"
	m4c3_url = "http://localhost/m4c3.html"
	m4c4 = "View"
	m4c4_url = "http://localhost/m4c4.html"
	m4c5 = "Print"
	m4c5_url = "http://localhost/m4c5.html"
	#
	water = "Copyright 2008 doug@goodall.com All Rights Reserved."
	color = "lightblue"
	width = 80
	height = 16

def m1c1():
	# Project->New
	#
	# The purpose of the new project function is to gather information about
	# the task at hand. The overall function of the Virtual Protocol Adapter is
	# to aid in the analysis of a stream of data in motion. During this function,
	# the user is asked to choose a specific pre-existing project type, or to 
	# begin creating a new one. As the development of the Virtual Protocol
	# adapter continues, more detail will come into existance about exactly what
	# a project is. A project can vary depending on what the meaning os "is" is.
	#
	form = """
		<h2>/Users/doug/Sources/pages/m1c1.cgi</h2>
		<h2>http://MacBookPro.local/m1c1.cgi</h2>
        <html><head><title>
        /Users/doug/Sources/pages/m1c1 .cgi
        </title></head><body>
        <form method=post action="m1c1.cgi">
        <p><table><tr><th align=right>Name:
        <td><input type=text name=name>
        <tr><th align=right>Rank:<td><select name=rank>
        <option>General<option>Captain<option>Private
        </select><tr><th align=right>Serial Number:
        <td><input type=text name=sernum>
        <tr><td colspan=2 align=center>
        <input type=submit value="Send">
        </table></form></body></html>
	"""
	fd = open("pages/m1c1.html","w")
	fd.write(form)
	fd.close()
	webbrowser.open(local.m1c1_url)

def m1c2():
	# Project->Add
	#
	webbrowser.open(local.m1c2_url)
	
def m1c3():
	# Project->Delete
	#
	webbrowser.open(local.m1c3_url)

def m1c4():
	# Project->View
	#
	webbrowser.open(local.m1c4_url)

def m1c5():
	# Project->Print
	#
	webbrowser.open(local.m1c5_url)

def m2c1():
	# Requirements->New
	#
	webbrowser.open(local.m2c1_url)

def m2c2():
	# Requirements->Add
	#
	webbrowser.open(local.m2c2_url)

def m2c3():
	# Requirements->Delete
	#
	webbrowser.open(local.m2c3_url)

def m2c4():
	# Requirements->View
	#
	webbrowser.open(local.m2c4_url)

def m2c5():
	# Requirements->Print
	#
	webbrowser.open(local.m2c5_url)

def m3c1():
	# Design->New
	#
	webbrowser.open(local.m3c1_url)

def m3c2():
	# Design->Add
	#
	webbrowser.open(local.m3c2_url)

def m3c3():
	# Design->Delete
	#
	webbrowser.open(local.m3c3_url)

def m3c4():
	# Design->View
	#
	webbrowser.open(local.m3c4_url)

def m3c5():
	# Design ->Print
	#
	webbrowser.open(local.m3c5_url)

def m4c1():
	# Modularization->New
	#
	webbrowser.open(local.m4c1_url)

def m4c2():
	# Modularization->Add
	#
	webbrowser.open(local.m4c2_url)

def m4c3():
	# Modularization ->Delete
	#
	webbrowser.open(local.m4c3_url)

def m4c4():
	# Modularization ->View
	#
	webbrowser.open(local.m45c4_url)

def m4c5():
	# Modularization->Prin t
	#
	webbrowser.open(local.m4c5_url)

def duh():
	webbrowser.open(local.m1c1_url)
	
def makemenu(parent):
	menubar = Frame(parent)
	menubar.pack(side=TOP, fill=X)
	#
	fbutton = Menubutton(menubar, text=local.m1, underline=0)
	fbutton.pack(side=LEFT)
	m1 = Menu(fbutton)
	m1.add_command(label=local.m1c1, command=m1c1, underline=0)
	m1.add_command(label=local.m1c2, command=m1c2, underline=0)
	m1.add_command(label=local.m1c3, command=m1c3, underline=0)
	m1.add_command(label=local.m1c4, command=m1c4, underline=0)
	m1.add_command(label=local.m1c5, command=m1c5, underline=0)
	fbutton.config(menu=m1)
	#
	fbutton = Menubutton(menubar, text=local.m2, underline=0)
	fbutton.pack(side=LEFT)
	m2 = Menu(fbutton)
	m2.add_command(label=local.m2c1, command=m2c1, underline=0)
	m2.add_command(label=local.m2c2, command=m2c2, underline=0)
	m2.add_command(label=local.m2c3, command=m2c3, underline=0)
	m2.add_command(label=local.m2c4, command=m2c4, underline=0)
	m2.add_command(label=local.m2c5, command=m2c5, underline=0)
	fbutton.config(menu=m2)
	#
	fbutton = Menubutton(menubar, text=local.m3, underline=0)
	fbutton.pack(side=LEFT)
	m3 = Menu(fbutton)
	m3.add_command(label=local.m3c1, command=m3c1, underline=0)
	m3.add_command(label=local.m3c2, command=m3c2, underline=0)
	m3.add_command(label=local.m3c3, command=m3c3, underline=0)
	m3.add_command(label=local.m3c4, command=m3c4, underline=0)
	m3.add_command(label=local.m3c5, command=m3c5, underline=0)
	fbutton.config(menu=m3)
	#
	fbutton = Menubutton(menubar, text=local.m4, underline=0)
	fbutton.pack(side=LEFT)
	m4 = Menu(fbutton)
	m4.add_command(label=local.m4c1, command=m4c1, underline=0)
	m4.add_command(label=local.m4c2, command=m4c2, underline=0)
	m4.add_command(label=local.m4c3, command=m4c3, underline=0)
	m4.add_command(label=local.m4c4, command=m4c4, underline=0)
	m4.add_command(label=local.m4c5, command=m4c5, underline=0)
	fbutton.config(menu=m4)
	#

	return menubar

local = 	localvars
root = Tk()
root.title(local.sProgram)
makemenu(root)
msg = Label(root, text=local.water)
msg.pack(expand=YES, fill=BOTH)
msg.config(relief=SUNKEN, width=local.width, height=local.height, bg=local.color)
root.mainloop()
