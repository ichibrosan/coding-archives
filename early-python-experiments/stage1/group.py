#!/usr/bin/python
# groups.cgi 1/8/2008 COPR doug@goodall.com. All Rights Reserved.

import os
import system

fp = open(“/etc/group”,”r”)
for buf in fp.readlines():
	if “#” != buf[0]:
		index = 0
		endex = buf.find(“:”)
		sGroup = buf[index:endex]
		print sGroup
fp.close()
