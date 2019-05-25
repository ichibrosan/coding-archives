#!/usr/local/bin/python
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
		safe = 4 ; W = 500 ; H =  330
		self.w = Canvas( self , height=H, width=W)
		
		T = 40 ; B = 302 ; L = 35 ; R = 460 ; P = 24 ; C = "gray"	
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

		T = 60 ; B = 120 ; L = 80 ; R = 420 ; P = 16 ; C = "lightgray"	
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
		
		self.w.grid()
		
		self.quitButton = Button ( self, text="Quit", command=self.quit )
		self.quitButton.grid()

app = Application() ; app.master.title("smooth.py - Smooth Widgets") ; app.mainloop()
