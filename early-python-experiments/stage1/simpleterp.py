#!/usr/bin/python
# simpleterp.py 1/8/2008 COPR doug@goodall.com

import ConfigParser
import string
import sys

cfg = ConfigParser.ConfigParser()
cfg.add_section("program")

fp = open("program.bas","r")
for buf in fp.readlines():
	#print buf
	endex = buf.find(" ")
	lineno = buf[:endex]
	#print "lineno is " + lineno
	temp = buf[endex+1:]
	size = len(temp)
	state = temp[:size-1]
	#print "state is "+state
	cfg.set("program",lineno,state)
fp.close()
fp = open("program.ini","w")
cfg.write(fp)
fp.close()

ig = 0
pc = 1
running = 1
while 1 == running:
	try:
		#print "trying pc as ",pc
		buf = cfg.get("program",str(pc))
	except:
		buf = "r"
	print pc,buf
	#print "trying " + buf[0:3]
	if "r" == buf[0]:
		ig += 1
	if "p" == buf[0]:
		print buf[2:]
	if "g" == buf[0]:
		pc = string.atoi(buf[2:])-1
	if "e" == buf[0]:	
		running = 0
	if "a" == buf[0]:
		str = sys.stdin.readline()
	if "w" == buf[0]:
		print str
	pc += 1



	
