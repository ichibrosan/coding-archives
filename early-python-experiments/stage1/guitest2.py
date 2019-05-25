#!/usr/bin/python 
# guitest.py 1/9/2008 COPR doug@goodall.com
# See Programming Python page 500

import ConfigParser
import os
from ScrolledText import ScrolledText
from Tkinter import *
from tkFileDialog import *
from tkMessageBox import *
from tkSimpleDialog import askstring
import webbrowser

def capturepackets():
	os.system("sudo tcpdump -f - en0 -c 1024 > sample.txt")
	
def notdone():
	webbrowser.open("http://localhost/index.html")
	x = 1

def makemenu(parent):
	menubar = Frame(parent)
	menubar.pack(side=TOP, fill=X)

	fbutton = Menubutton(menubar, text='sys', underline=0)
	fbutton.pack(side=LEFT)
	sys = Menu(fbutton)
	sys.add_command(label="sysDescr.0", command=notdone, underline=0)
	sys.add_command(label="sysObjectID.0", command=notdone, underline=0)
	sys.add_command(label="sysUpTimeInstance.0", command=notdone, underline=0)
	sys.add_command(label="sysContact.0", command=notdone, underline=0)
	sys.add_command(label="sysName.0", command=notdone, underline=0)
	sys.add_command(label="sysLocation.0", command=notdone, underline=0)
	sys.add_command(label="sysServices.0", command=notdone, underline=0)
	sys.add_command(label="sysORLastChange.0", command=notdone, underline=0)
	sys.add_command(label="sysORID.1", command=notdone, underline=0)
	sys.add_command(label="sysORID.2", command=notdone, underline=0)
	sys.add_command(label="sysORID3", command=notdone, underline=0)
	sys.add_command(label="sysORID.4", command=notdone, underline=0)
	sys.add_command(label="sysORID.5", command=notdone, underline=0)
	sys.add_command(label="sysORID.6", command=notdone, underline=0)
	sys.add_command(label="sysORID.7", command=notdone, underline=0)
	sys.add_command(label="sysORID.8", command=notdone, underline=0)
	sys.add_command(label="sysORDescr.1", command=notdone, underline=0)
	sys.add_command(label="sysORDescr.2", command=notdone, underline=0)
	sys.add_command(label="sysORDescr.3", command=notdone, underline=0)
	sys.add_command(label="sysORDescr.4", command=notdone, underline=0)
	sys.add_command(label="sysORDescr.5", command=notdone, underline=0)
	sys.add_command(label="sysORDescr.6", command=notdone, underline=0)
	sys.add_command(label="sysORDescr.7", command=notdone, underline=0)
	sys.add_command(label="sysORDescr.8", command=notdone, underline=0)
	sys.add_command(label="sysORUpTime.1", command=notdone, underline=0)
	sys.add_command(label="sysORUpTime.2", command=notdone, underline=0)
	sys.add_command(label="sysORUpTime.3", command=notdone, underline=0)
	sys.add_command(label="sysORUpTime.4", command=notdone, underline=0)
	sys.add_command(label="sysORUpTime.5", command=notdone, underline=0)
	sys.add_command(label="sysORUpTime.6", command=notdone, underline=0)
	sys.add_command(label="sysORUpTime.7", command=notdone, underline=0)
	sys.add_command(label="sysORUpTime.8", command=notdone, underline=0)
	fbutton.config(menu=sys)

	fbutton = Menubutton(menubar, text='Edit', underline=0)
	fbutton.pack(side=LEFT)
	edit = Menu(fbutton)
	edit.add_command(label="Undo paste...", command=notdone, underline=0)
	edit.add_command(label="Clear undo hostory...", command=notdone, underline=0)
	edit.add_command(label="Paste...", command=notdone, underline=0)
	edit.add_command(label="Paste column...", command=notdone, underline=0)
	edit.add_command(label="Select all...", command=notdone, underline=0)
	edit.add_command(label="Select line...", command=notdone, underline=0)
	edit.add_command(label="Select paragraph...", command=notdone, underline=0)
	edit.add_command(label="Insert...", command=notdone, underline=0)
	edit.add_command(label="Copy path...", command=notdone, underline=0)
	fbutton.config(menu=edit)

	fbutton = Menubutton(menubar, text='Capture', underline=0)
	fbutton.pack(side=LEFT)
	capture = Menu(fbutton)
	capture.add_command(label="New...", command=capturepackets, underline=0)
	fbutton.config(menu=capture)

	fbutton = Menubutton(menubar, text='View', underline=0)
	fbutton.pack(side=LEFT)
	view = Menu(fbutton)
	view.add_command(label="New...", command=notdone, underline=0)
	fbutton.config(menu=view)

	fbutton = Menubutton(menubar, text='Search', underline=0)
	fbutton.pack(side=LEFT)
	search = Menu(fbutton)
	search.add_command(label="New...", command=notdone, underline=0)
	fbutton.config(menu=search)

	fbutton = Menubutton(menubar, text='Markup', underline=0)
	fbutton.pack(side=LEFT)
	markup = Menu(fbutton)
	markup.add_command(label="New...", command=notdone, underline=0)
	fbutton.config(menu=markup)

	fbutton = Menubutton(menubar, text='Window', underline=0)
	fbutton.pack(side=LEFT)
	window = Menu(fbutton)
	window.add_command(label="New...", command=notdone, underline=0)
	fbutton.config(menu=window)

	fbutton = Menubutton(menubar, text='Help', underline=0)
	fbutton.pack(side=LEFT)
	help = Menu(fbutton)
	help.add_command(label="New...", command=notdone, underline=0)
	fbutton.config(menu=help)

	return menubar
	
root = Tk()
root.title('Guitest')
makemenu(root)
msg = Label(root, text='This space available')
msg.pack(expand=YES, fill=BOTH)
msg.config(relief=SUNKEN, width=80, height=16, bg='beige')
root.mainloop()
