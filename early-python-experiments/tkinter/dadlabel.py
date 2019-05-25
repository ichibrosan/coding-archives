#!/usr/bin/python
# dadlabel.py 2008/02/07 GPL doug@goodall.com

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
		diameter = 640
		radius = diameter /2
		safe = 6
		center = radius + safe
		sizex = diameter + ( 2 * safe )
		sizey = diameter + ( 2 * safe )
		width = 100
		
		fComic18 = tkFont.Font(family="Comic sans MS",size="18")
		fComic36 = tkFont.Font(family="Comic sans MS",size="36")
		fComic48 = tkFont.Font(family="Comic sans MS",size="48")
		self.w = Canvas( self , height=sizey, width=sizex)
		self.w.create_oval(safe,safe,safe+diameter,safe+diameter)
		
		x = 2048
		while x:
			x = x - 1			
			n1 = random.randint(0,15) ; n2 = random.randint(0,15)
			n3 = random.randint(0,15) ; n4 = random.randint(0,15)
			n5 = random.randint(0,15) ; n6 = random.randint(0,15)		
			sColor = "#%x%x%x%x%x%x" % (n1,n2,n3,n4,n5,n6)
			self.w.create_arc(safe,safe,safe+diameter,safe+diameter,
					extent=1, start = random.randint(0,359), fill=sColor)				
		
		# 48 point text situation
		boxwidth = 360 ; boxtop = 68 ;	 boxheight = 54
		self.w.create_rectangle(  
			center - ( boxwidth / 2 ), boxtop,
			center + ( boxwidth / 2 ), boxtop + boxheight, fill="white")
		self.w.create_text(center,boxtop + 24,font=fComic48,text="David A. Goodall")
 
 		# 36 point text situation
		boxwidth = 300 ; boxtop = 135 ; boxheight = 35
		self.w.create_rectangle( 
			center - ( boxwidth / 2 ), boxtop,
			center + ( boxwidth / 2 ), boxtop + boxheight, fill="white")									  
		self.w.create_text(center,boxtop + 15,font=fComic36,text="MMEC Room 410")

		# create date and time for label
		now = time.localtime(time.time())
		sTime = time.asctime(now)
		
		# 18 point text situation Date
		boxwidth = 220 ; 	boxtop  = 185 ; boxheight = 30
		self.w.create_rectangle( 
			center - ( boxwidth / 2 ), boxtop,
			center + ( boxwidth / 2 ), boxtop + boxheight, fill="white")
		self.w.create_text(center,boxtop + 12, font=fComic18,
											text=sTime)

		# 18 point text situation Blank Space
		boxwidth = 470 ; 	boxtop = radius + 115 ;	boxheight = 100
		self.w.create_rectangle( 
			center - ( boxwidth / 2 ), boxtop,
			center + ( boxwidth / 2 ), boxtop + boxheight, fill="white")

		# 18 point text situation
		boxwidth = 340 ; 	boxtop = diameter - 95 ; boxheight = 30
		self.w.create_rectangle( 
			center - ( boxwidth / 2 ), boxtop,
			center + ( boxwidth / 2 ), boxtop + boxheight, fill="white")
		self.w.create_text(
			center,boxtop + 12, font=fComic18, 
			text="The Secret Agent by Joseph Conrad")

		# Add spindle hole to make more wysiwyg
		self.w.create_oval(
			safe+220,safe+220,
			safe+diameter-220,safe+diameter-220,
			fill="#FFFFFF")
		
		self.w.grid()
		
		self.quitButton = Button ( self, text="Quit", command=self.quit )
		self.quitButton.grid()

app = Application()
app.master.title("show.py - Optical Media Label Creator")
app.mainloop()
