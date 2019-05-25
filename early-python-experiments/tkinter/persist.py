#!/usr/bin/python
# portal.py 2008/02/12 COPR douglas_goodall@mac.com

import ConfigParser
import os
import sys
import Tkinter

def quit():
	cfg = ConfigParser.ConfigParser()
	cfg.add_section("display")
	cfg.set("display","geometry",root.geometry())
	fp = open("portal.ini","w")
	cfg.write(fp)
	fp.close()
	sys.exit()

root = Tkinter.Tk()

cfg = ConfigParser.ConfigParser()
if False == os.access("portal.ini",os.R_OK):
	cfg.add_section("display")
	cfg.set("display","geometry","640x480+100+100")
	fp = open("portal.ini","w")
	cfg.write(fp)
	fp.close()
cfg.read("portal.ini")
geo = cfg.get("display","geometry")
root.geometry(geo)

widget = Tkinter.Button(None,text="Quit",command=quit)

widget.pack()
widget.mainloop()

	