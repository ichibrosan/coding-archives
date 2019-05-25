#!/usr/bin/python
# getgroup.py 1/8/2008 COPR doug@goodall.com 

import ConfigParser
import os
import sys

cfg = ConfigParser.ConfigParser()
cfg.add_section("byname")
cfg.add_section("bynumber")

fp = open("/etc/group","r")
for buf in fp.readlines():
	if "#" != buf[0]:
		index = 0
		endex = buf.find(":")
		sName = buf[index:endex]
		index = endex + 3
		endex = buf.find(":",index)
		sNumber = buf[index:endex]
		cfg.set("byname",sName,sNumber)
		cfg.set("bynumber",sNumber,sName)		
fp.close()

fp = open("group.cfg","w")
cfg.write(fp)
fp.close()


