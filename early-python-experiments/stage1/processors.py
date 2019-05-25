#!/usr/bin/python
############################
# processors.py 1/6/2008 COPR doug@goodall.com #
############################

# The purpose of this program is to look up the number
# of processor cores in the mib and extract the description
# of each one to be displayed. Core 2 Duo looks like 2 486's

import os
import string
import sys
import tempfile

temp1 = tempfile.mktemp()
temp2 = tempfile.mktemp()

cmd = "grep hrDeviceProcessor mib.txt > " + temp1
os.system(cmd)
fd = open(temp1,"r")
for proc in fd.readlines():
	indexbeg = proc.find(".")+1
	indexend = proc.find(" ",indexbeg)
	indexstr = proc[indexbeg:indexend]
	cmd = "grep hrDeviceDescr." + indexstr + " mib.txt > " + temp2
	os.system(cmd)
	fd2 = open(temp2,"r")
	data = fd2.readline()
	fd2.close()
	indexbeg = data.find(":")+2
	tempstr = data[indexbeg:]
	descr = tempstr[:len(tempstr)-1]
	print "Processor Description is ",descr
fd.close()

