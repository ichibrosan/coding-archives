#!/usr/bin/python
# thursday 1/10/2008 COPR doug@goodall.com

import ConfigParser
import os
from ScrolledText import ScrolledText
from Tkinter import *
from tkFileDialog import *
from tkMessageBox import *
from tkSimpleDialog import askstring
import webbrowser

def notdone():
        webbrowser.open("http://localhost/index.html")
        x = 1

def makemenu(parent):
        menubar = Frame(parent)
        menubar.pack(side=TOP, fill=X)

        fbutton = Menubutton(menubar, text='sys', underline=0)
        fbutton.pack(side=LEFT)
        sys = Menu(fbutton)
        sys.add_command(label="sysORUpTime.5", command=notdone, underline=0)
import
        fbutton = Menubutton(menubar, text='Search', underline=0)
        fbutton.pack(side=LEFT)
        search = Menu(fbutton)
        search.add_command(label="New...", command=notdone, underline=0)
        fbutton.config(menu=search)

        return menubar

cfg = ConfigParser.ConfigParser()
cfg.add_section("identification")
cfg.set("identification","program","thursday")
cfg.add_section("procedure")
cfg.set("procedure","debug","false")
cfg.add_section("data")
fd = open("thursday.cfg","w")
cfg.write(fd)
fd.close()

print cfg.get("identification","program")
debug = cfg.get("procedure","debug")

if "true" == debug:
	print "debug is enabled"
else:
	print "debug is not enabled"

root = Tk()
root.title('Guitest')
makemenu(root)
msg = Label(root, text='This space available')
msg.pack(expand=YES, fill=BOTH)
msg.config(relief=SUNKEN, width=80, height=16, bg='beige')
root.mainloop()

