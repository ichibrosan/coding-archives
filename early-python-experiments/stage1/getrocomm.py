#!/usr/bin/python
# getrocomm.py 1/7/2008 COPR doug@goodall.com

# extract the rocommunity name from the /etc/snmp/snmpd.conf

import os
import tempfile

temp = tempfile.mktemp()
cmd = "grep rocommunity /etc/snmp/snmpd.conf > " + temp
os.system(cmd)
fd = open(temp,"r")
buf = fd.readline()
if "#" == buf[0]:
	buf = fd.readline()
if "rocommunity" == buf[0:11]:
	index = 11
	while " " == buf[index]  or "\t" == buf[index]:
		index += 1
	buf2 = buf[index:]
	s = buf2.find(" ")
	rocom = buf2[0:s]
	print rocom
