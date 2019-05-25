#!/usr/bin/python
# portal.py 2008/02/12 COPR douglas_goodall@mac.com

import ConfigParser
import os
import random
import string
import sys
import tempfile
import Tkinter

def random_color():
	nib1 = random.randint(0,15) ; nib2 = random.randint(0,15) 
	nib3 = random.randint(0,15) ; nib4 = random.randint(0,15)
	nib5 = random.randint(0,15) ; nib6 = random.randint(0,15)
	return "#%x%x%x%x%x%x" % (nib1,nib2,nib3,nib4,nib5,nib6)

def file_quit():
	canvas.create_rectangle(0,0,CW,CH,width=0,fill=random_color())
	cfg.set("display","geometry",root.geometry())
	fp = open("portal.ini","w") ; cfg.write(fp) ; fp.close()
	sys.exit()

def edit_clear():
	canvas.create_rectangle(0,0,CW,CH,width=0,fill=random_color())	
	
def view_lines():
	canvas.create_rectangle(0,0,CW,CH,width=0,fill=random_color())
	count = random.randint(16,256)
	while count > 0:
		count = count - 1
		canvas.create_line(
			random.randint(0,int(CW)),random.randint(0,int(CH)),
			random.randint(0,int(CH)),random.randint(0,int(CH)) ,
			width=4,fill=random_color())

def plot_line(x1,y1,x2,y2,color):
	canvas.create_line(x1,y2,x2,y1,width=3,fill=color)
	
def plot_circle(x1,y1,x2,y2,color):
	canvas.create_oval(x1,y1,x2,y2,width=3,fill=color)

def plot_quadrants(x1,y1,x2,y2,color):
	b = int(cfg.get("canvas","border")) 
	qw = ( CW - b - b - b - b ) / 2
	qh = ( CH  - b - b - b - b ) / 2

	# create large oval, lines, and connection points
	canvas.create_oval( 
		x1 + ( qw / 2 ) + ( qw / 4), y1 + ( qh / 4 ),
		x2, y1 + ( qh / 2 ), fill=random_color())
	canvas.create_line( 	
		x1, y1, x1 + ( qw / 2 ) + (qw / 4) - (qw / 8) - (qw / 32 ), 
		y1 + ( qh / 2) - (qh / 16 ), fill=color)
	canvas.create_oval(
		x1 + ( qw / 2 ) + (qw / 4) - (qw / 8) - (qw / 32 ) - 3, 
		y1 + ( qh / 2) - (qh / 16 ) - 3,
		x1 + ( qw / 2 ) + (qw / 4) - (qw / 8) - (qw / 32 ) + 3, 
		y1 + ( qh / 2) - (qh / 16 ) + 3, fill=color)
	canvas.create_line( 	
		x2, y2, x1 + ( qw / 2 ) + (qw / 4) - (qw / 8) - (qw / 32 ), 
		y1 + ( qh / 2), fill=color)
	canvas.create_oval(	
		x1 + ( qw / 2 ) + (qw / 4) - (qw / 8) - (qw / 32 ) - 3, 
		y1 + ( qh / 2) - 3,
		x1 + ( qw / 2 ) + (qw / 4) - (qw / 8) - (qw / 32 ) + 3, 
		y1 + ( qh / 2) + 3,fill=color)

	# create medium oval, lines, and connection points
	canvas.create_oval( 
		x1 + ( qw / 2 ) + ( qw / 4 ) - ( qw / 8 ), 
		y1 + ( qh / 2 ) -  ( qh / 8),
		x1 + ( qw / 2 ) + ( qw / 4 ), 
		y1 + ( qh / 2 ), fill=random_color())	
	canvas.create_line( 	
		x1, y1, x1 + ( qw / 2 ) + (qw / 4) - (qw / 16), 
		y1 + ( qh / 2) - (qh / 8 ), fill=color)
	canvas.create_oval( 
		x1 + ( qw / 2 ) + (qw / 4) - (qw / 16) - 3, 
		y1 + ( qh / 2) - (qh / 8 ) - 3, 
		x1 + ( qw / 2 ) + (qw / 4) - (qw / 16) + 3, 
		y1 + ( qh / 2) - (qh / 8 ) + 3, fill=color)
	canvas.create_line( 	
		x2, y2, x1 + ( qw / 2 ) + (qw / 4) - (qw / 16), 
		y1 + ( qh / 2), fill=color)
	canvas.create_oval(	
		x1 + ( qw / 2 ) + (qw / 4) - (qw / 16) - 3, 
		y1 + ( qh / 2) - 3,
		x1 + ( qw / 2 ) + (qw / 4) - (qw / 16) + 3, 
		y1 + ( qh / 2) + 3,fill=color)
	
	# create small oval, lines, and connection points			
	canvas.create_oval( 
		x1 + ( qw / 2 ) + ( qw / 4 ) - ( qw / 8 ) - ( qw / 16 ), 
		y1 + ( qh / 2 ) -  ( qh / 16),
		x1 + ( qw / 2 ) + ( qw / 4 ) - ( qw / 8 ), 
		y1 + ( qh / 2 ), fill=random_color())
	canvas.create_line( 	
		x1, y1, x1 + ( qw / 2 ) + (qw / 4) + ( qw / 8) , 
		y1 + ( qh / 2) - (qh / 4 ), fill=color)
	canvas.create_oval(	
		x1 + ( qw / 2 ) + (qw / 4) + ( qw / 8) - 3 , 
		y1 + ( qh / 2) - (qh / 4 ) - 3,
		x1 + ( qw / 2 ) + (qw / 4) + ( qw / 8) + 3 , 
		y1 + ( qh / 2) - (qh / 4 ) + 3,fill=color)
	canvas.create_line( 	
		x2, y2, x1 + ( qw / 2 ) + (qw / 4) + ( qw / 8) , 
		y1 + ( qh / 2), fill=color)
	canvas.create_oval(	
		x1 + ( qw / 2 ) + (qw / 4) + ( qw / 8) - 3 , 
		y1 + ( qh / 2) - 3,
		x1 + ( qw / 2 ) + (qw / 4) + ( qw / 8) + 3, 
		y1 + ( qh / 2) + 3,fill=color)
									
def view_portal():	
	canvas.create_rectangle(0,0,1920,1200,width=0,fill="white")
	
	# calculate quadrant coordinates for subsequent use
	b = int(cfg.get("canvas","border")) 
	qw = ( CW - b - b - b - b )  / 2
	qh = ( CH  - b - b - b - b ) / 2
	q1x1 = b ;               q1y1 = b ;              q1x2 = b + qw ;               q1y2 = b + qh
	q2x1 = b + qw + b ; q2y1 = b ;              q2x2 = b + qw + b + qw ; q2y2 = b + qh
	q3x1 = b ;              q3y1 = b + qh + b ; q3x2 = b + qw ;               q3y2 = b + qh + b + qh
	q4x1 = b + qw + b ; q4y1 = b + qh + b ; q4x2 = b + qw + b + qw ; q4y2 = b + qh + b + qh
	
	# create outer border with smooth corners
	# Top, Bottom, Left, Right, Padsize, and Color
	T = 4 ; B = q3y2 ; L = 4 ; R = q4x2 ; P = 24 ; C = cfg.get("smooth","color")
	canvas.create_oval(L,T,L+P-1,T+P-1,fill=C)			# UL
	canvas.create_oval(R,T,R+P-1,T+P-1,fill=C)		# UR
	canvas.create_oval(L,B,L+P-1,B+P-1,fill=C) 		# LL
	canvas.create_oval(R,B,R+P-1,B+P-1,fill=C)			# LR		
	canvas.create_rectangle(L+P/2,T,R+P/2,B+P,width=0, fill=C)
	canvas.create_rectangle(L,T+P/2,R+P-1,B+P/2-1,width=0, fill=C)
	canvas.create_line(L+P/2,T,R+P/2-1,T)			    # UL to UR
	canvas.create_line(L+P/2,B+P-1,R+P/2-1,B+P-1)	# LL to LR
	canvas.create_line(L,T+P/2,L,B+P/2-1)			    # UL to LL
	canvas.create_line(R+P-1,T+P/2,R+P-1,B+P/2-1)	# UR to LR
	
	# outline each quadrant
	canvas.create_rectangle(q1x1, q1y1, q1x2, q1y2,fill="gray")
	canvas.create_rectangle(q2x1, q2y1,q2x2,q2y2,fill="gray")
	canvas.create_rectangle(q3x1, q3y1,q3x2,q3y2,fill="gray")
	canvas.create_rectangle(q4x1, q4y1,q4x2,q4y2,fill="gray")
	
	# fill each quadrant with something interesting
	plot_line(q1x1,q1y1,q1x2,q1y2,random_color())	
	plot_circle(q2x1,q2y1,q2x2,q2y2,random_color())
	plot_circle(q3x1,q3y1,q3x2,q3y2,random_color())
	plot_quadrants(q4x1,q4y1,q4x2,q4y2,"purple")
	
def help_about():
	canvas.create_rectangle(0,0,CW,CH,width=0,fill=random_color())
	canvas.create_text(200,200,
		fill=cfg.get("help","color"),text=cfg.get("help","about"))

def makemenu(parent):
	menubar = Tkinter.Frame(parent)
	menubar.pack(side=Tkinter.TOP, fill=Tkinter.X)
	fbutton = Tkinter.Menubutton(menubar,text='File',underline=0)
	fbutton.pack(side=Tkinter.LEFT) ; file = Tkinter.Menu(fbutton)
	file.add_command(label='Quit',command=file_quit,underline=0)
	fbutton.config(menu=file)
	ebutton = Tkinter.Menubutton(menubar,text='Edit',underline=0)
	ebutton.pack(side=Tkinter.LEFT) ; edit = Tkinter.Menu(ebutton)
	edit.add_command(label='Clear',command=edit_clear,underline=0)
	ebutton.config(menu=edit)
	vbutton = Tkinter.Menubutton(menubar,text='View',underline=0)
	vbutton.pack(side=Tkinter.LEFT) ; view = Tkinter.Menu(vbutton)
	view.add_command(label='Lines',command=view_lines,underline=0)
	view.add_command(label='Portal',command=view_portal,underline=0)
	vbutton.config(menu=view)
	hbutton = Tkinter.Menubutton(menubar,text='Help',underline=0)
	hbutton.pack(side=Tkinter.LEFT) ; help = Tkinter.Menu(hbutton)
	help.add_command(label='About',command=help_about,underline=0)
	hbutton.config(menu=help)
	return menubar

root = Tkinter.Tk()
makemenu(root)

cfg = ConfigParser.ConfigParser()
if False == os.access("portal.ini",os.R_OK):
	cfg.add_section("display")
	cfg.set("display","geometry","1024x768+100+100")
	cfg.set("display","initw","1024")
	cfg.set("display","inith","768")
	cfg.add_section("smooth")
	cfg.set("smooth","color",random_color())
	cfg.add_section("canvas")	
	cfg.set("canvas","width","1014")
	cfg.set("canvas","height","758")
	cfg.set("canvas","border","20")
	cfg.add_section("help")
	cfg.set("help","color",random_color())
	cfg.add_section("debug")
	cfg.set("help","about",
		"portal.py 2008/02/17 COPR douglas_goodall@mac.com")
	fp = open("portal.ini","w") ; cfg.write(fp) ; fp.close()
	
cfg.read("portal.ini") ; geo = cfg.get("display","geometry")
root.geometry(geo)

CW = int(cfg.get("canvas","width"))  ; CH = int(cfg.get("canvas","height"))
canvas = Tkinter.Canvas(width=CW,height=CH,bg="lightblue") ; canvas.pack()

root.mainloop()	

# end of file