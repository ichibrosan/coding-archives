#!/usr/bin/python
# mib2cfg.py 1/7/2008 COPR doug@goodall.com

import ConfigParser

cfg = ConfigParser.ConfigParser()
cfg.add_section("mib")

fd = open("mib.txt","r")
for buf in fd.readlines():
	endex = buf.find(" ")
	oid = buf[0:endex]
	#print "oid is "+oid+"|"
	index = endex + 3
	#print "val is "+buf[index:]+"|"
	value = buf[index:]
	size = len(value)
	val = value[0:size-1]
	flag = val.find('"')
	if -1 != flag:
		value = val[8:]
	else:
		value = "\""+val+"\""	
	cfg.set("mib",oid,value)
fd2 = open("mib.cfg","w")
cfg.write(fd2)
fd2.close()

	
	