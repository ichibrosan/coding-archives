#!/usr/bin/python
# query.py 2008/02/12 COPR douglas_goodall@mac.com

fp = open("/Users/doug/Sources/Python/tkinter/mib.txt","r")
for buf in fp.readlines():
	endex = buf.find(" ")
	sOid = buf[:endex]
	if sOid == "sysLocation.0":
		print sOid
		print "tail --> ",buf[endex:]
		print "--------------------------------"

