#!/usr/bin/python
# motb.py 2008/02/10 GPL doug@goodall.com
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
		fComic = tkFont.Font(family="Zapfino",size="130")
		fScript = tkFont.Font(family="Zapfino",size="24")
		fNormal = tkFont.Font(family="Arial",size="14")
		fNumber = tkFont.Font(family="Arial",size="34")
		fTitle = tkFont.Font(family="Arial",size="48")
		
		T = 40 ; B = 302 ; L = 35 ; R = 460 ; P = 24 ; C = "lightgray"	
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

		self.w.create_text(200,290,font=fComic,text="motb",fill="gray")
		self.w.create_text(260,75,font=fTitle,text="One World Platinum",fill="blue")
		self.w.create_text(220,135,font=fScript,text="A Mark of Distinction",fill="black")
		
		self.w.create_text(260,210,font=fNumber,text="6 6 6   1 2 3   2 3   3 4 5 6")
		
		self.w.create_oval(390,270,440,320,fill="red")
		self.w.create_oval(420,270,470,320,fill="purple")
		self.w.create_text(430,295,font=fNormal,text="BeastCard")
		
		self.w.grid()
		self.quitButton = Button ( self, text="Quit", command=self.quit )
		self.quitButton.grid()

app = Application() ; app.master.title("smooth.py - Smooth Widgets") ; app.mainloop()
