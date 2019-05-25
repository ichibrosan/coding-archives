#!/usr/bin/python
# show.py 2008/02/07 COPR doug@goodall.com

import math
import os
import random 
import tempfile
import tkFont
from Tkinter import *

AKAI_X = 1830
AKAI_Y = 940

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		num_x_pixels = 640
		num_y_pixels = 640
		border = 4
		radius = 320.0
		twopi = 3.141592535 * 2.0
		radperdeg = 360.0 / twopi
		spread = 1
			
		self.w = Canvas( self , height=num_y_pixels+(border*2), width=num_x_pixels+(border*2))
		self.w.grid()
		

		temp = tempfile.mktemp()
		sample = "/Users/doug/Sources/Python/sample.txt"
		cmd = "ls -l -g " + sample + "> " + temp
		os.system(cmd) 
		fd = open(temp,"r")
		buf = fd.readline()
		stuff = "Analysis of " + buf + "<p>"
		fd2 = open(sample,"r")
		for buf in fd2.readlines():
			index = 0 ;                                                           sTime    = buf[index:index+15]
			index += 16 ;            endex = buf.find(" ",index) ; sFrame  = buf[index:endex]
			index = endex +  1 ; endex = buf.find(".",index) ; sOctet1 = buf[index:endex]
			index = endex +  1 ; endex = buf.find(".",index) ; sOctet2 = buf[index:endex]
			index = endex +  1 ; endex = buf.find(".",index) ; sOctet3 = buf[index:endex]
			index = endex +  1 ; endex = buf.find(".",index) ; sOctet4 = buf[index:endex]
			index = endex +  1 ; endex = buf.find(" ",index) ; sPort      = buf[index:endex]
			index = endex + 3 ; endex = buf.find(".",index) ; dOctet1  = buf[index:endex]
			index = endex +  1 ; endex = buf.find(".",index) ; dOctet2 = buf[index:endex]
			index = endex +  1 ; endex = buf.find(".",index) ; dOctet3 = buf[index:endex]
			index = endex +  1 ; endex = buf.find(".",index) ; dOctet4 = buf[index:endex]
			index = endex +  1 ; endex = buf.find(":",index) ; dPort      = buf[index:endex]
			SourceIP  = sOctet1  + "." + sOctet2 + "." + sOctet3 + "." + sOctet4 
			DestIP    = dOctet1  + "." + sOctet2 + "." + dOctet3 + "." + dOctet4
			SourceIPp = SourceIP + "." + sPort ; DestIPp   = DestIP   + "." + dPort
			
			degrees = float(sOctet4) ; radians  = degrees / radperdeg	
			x1 =  radius * math.cos(radians) ; y1 = radius * math.sin(radians)
			degrees = float(dOctet4) ; 
			radians  = degrees / radperdeg	
			x2 =  radius * math.cos(radians) ; y2 = radius * math.sin(radians)			


			x1 = 0            ; y1 = int(sOctet4)-150
			x2 = 50+int(dOctet4)*2 ; y2 = 630
			
			if dPort == "http":     
				sColor = "green"
				self.w.create_line(border+x1,border+y1,border+x2,border+y2,fill=sColor)
			
			if dPort == "domain": 
				sColor = "red"
				self.w.create_line(border+x1,border+y1,border+x2,border+y2,fill=sColor)

			if dPort == "ftp": 
				sColor = "purple"
				self.w.create_line(border+x1,border+y1,border+x2,border+y2,fill=sColor)



			# n1 = random.randint(0,15) ; n2 = random.randint(0,15) ; n3 = random.randint(0,15) 
			# n4 = random.randint(0,15) ; n5 = random.randint(0,15) ; n6 = random.randint(0,15)		
			# sColor = "#%x%x%x%x%x%x" % (n1,n2,n3,n4,n5,n6)
			# sColor = "darkgray"
			
#			if dPort == "http":     
#				sColor = "green"
#				self.w.create_line(border+320+x1,border+320+y1,border+320+x2,border+320+y2,fill=sColor)
#			
#			if dPort == "domain": 
#				sColor = "red"
#				self.w.create_line(border+320+x1,border+320+y1,border+320+x2,border+320+y2,fill=sColor)
#
#			if dPort == "ftp": 
#				sColor = "purple"
#int(				self.w.create_line(border+320+x1,border+320+y1,border+320+x2,border+320+y2,fill=sColor)


			#self.w.create_line(border+320+x1,border+320+y1,border+320+x2,border+320+y2,fill=sColor)
		fd2.close()

		fComic18 = tkFont.Font(family="Comic sans MS",size="18")
		fComic24 = tkFont.Font(family="Comic sans MS",size="24")
		fComic36 = tkFont.Font(family="Comic sans MS",size="36")
		fComic48 = tkFont.Font(family="Comic sans MS",size="48")

		self.w.create_text(60,40, font=fComic24, text="domain",fill="red")
		self.w.create_text(60,65, font=fComic24, text="http",fill="green")
		self.w.create_text(60,90, font=fComic24, text="ftp",fill="purple")

		self.w.create_text(80,          635, font=fComic24, text="map by IP",fill="black")
		self.w.create_text(640 - 80,635, font=fComic24, text="COPR Goodall",fill="black")


		self.quitButton = Button ( self, text="Quit", command=self.quit )
		self.quitButton.grid()

app = Application()
app.master.title("show.py - Packet Trace by IP")
app.mainloop()
