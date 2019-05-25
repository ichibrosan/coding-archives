#!/usr/bin/python
# smooth.py 2008/02/10 GPL doug@goodall.com

import random
import time
import tkFont
from Tkinter import *

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		safe = 4
		fComic18 = tkFont.Font(family="Comic sans MS",size="18")
		fComic24 = tkFont.Font(family="Comic sans MS",size="24")
		fComic36 = tkFont.Font(family="Comic sans MS",size="36")
		fComic48 = tkFont.Font(family="Comic sans MS",size="48")
		
		W = 500
		H =  280
		self.w = Canvas( self , height=H, width=W)
		
		T = 40			# Top
		B = 240			# Bottom
		L = 40			# Left
		R = 460			# Right
		P = 24			# Padsize
		C = "gray"		# General Color
		self.w.create_oval(L,T,L+P-1,T+P-1,fill=C)					# UL
		self.w.create_oval(R,T,R+P-1,T+P-1,fill=C)				# UR
		self.w.create_oval(L,B,L+P-1,B+P-1,fill=C) 				# LL
		self.w.create_oval(R,B,R+P-1,B+P-1,fill=C)					# LR		
		self.w.create_rectangle(L+P/2,T,R+P/2,B+P,width=0, fill=C)
		self.w.create_rectangle(L,T+P/2,R+P-1,B+P/2-1,width=0, fill=C)
		self.w.create_line(L+P/2,T,R+P/2-1,T)			            # UL to UR
		self.w.create_line(L+P/2,B+P-1,R+P/2-1,B+P-1)			# LL to LR
		self.w.create_line(L,T+P/2,L,B+P/2-1)			            # UL to LL
		self.w.create_line(R+P-1,T+P/2,R+P-1,B+P/2-1)			# UR to LR

		T = 60			# Top
		B = 120			# Bottom
		L = 80			# Left
		R = 420			# Right
		P = 16			# Padsize
		C = "lightgray"		# General Color
		self.w.create_oval(L,T,L+P-1,T+P-1,fill=C)					# UL
		self.w.create_oval(R,T,R+P-1,T+P-1,fill=C)				# UR
		self.w.create_oval(L,B,L+P-1,B+P-1,fill=C) 				# LL
		self.w.create_oval(R,B,R+P-1,B+P-1,fill=C)					# LR		
		self.w.create_rectangle(L+P/2,T,R+P/2,B+P,width=0, fill=C)
		self.w.create_rectangle(L,T+P/2,R+P-1,B+P/2-1,width=0, fill=C)
		self.w.create_line(L+P/2,T,R+P/2-1,T)			            # UL to UR
		self.w.create_line(L+P/2,B+P-1,R+P/2-1,B+P-1)			# LL to LR
		self.w.create_line(L,T+P/2,L,B+P/2-1)			            # UL to LL
		self.w.create_line(R+P-1,T+P/2,R+P-1,B+P/2-1)			# UR to LR
		
		n1 = random.randint(0,15) ; n2 = random.randint(0,15)
		n3 = random.randint(0,15) ; n4 = random.randint(0,15)
		n5 = random.randint(0,15) ; n6 = random.randint(0,15)		
		sColor = "#%x%x%x%x%x%x" % (n1,n2,n3,n4,n5,n6)
#		self.w.create_arc(safe,safe,safe+diameter,safe+diameter,
#					extent=1, start = random.randint(0,359), fill=sColor)				
		
#		boxwidth = 340 ; boxtop = 68 ;	 boxheight = 54
#		self.w.create_rectangle(  
#			center - ( boxwidth / 2 ), boxtop,
#			center + ( boxwidth / 2 ), boxtop + boxheight, fill="white")
#		self.w.create_text(center,boxtop + 24,font=fComic48,text="Precious Data")
 		
		self.w.grid()
		
		self.quitButton = Button ( self, text="Quit", command=self.quit )
		self.quitButton.grid()

app = Application()
app.master.title("smooth.py - Smooth Widget Test")
app.mainloop()
