#!/usr/bin/python
################################################
# interfaces.py 1/6/2008 COPR doug@goodall.com #
################################################

import os
import string
import sys
import tempfile

temp1 = tempfile.mktemp()
temp2 = tempfile.mktemp()

cmd = "grep ifNumber.0 mib.txt > " + temp1
os.system(cmd)
fd = open(temp1,"r")
data = fd.readline()
fd.close()
typeend = data.find(":")
ifnumstr = data[typeend+2:]
ifnum = string.atoi(ifnumstr[0:2])
for i in range(ifnum):

	cmd = "grep ifDescr." + str(i+1) + " mib.txt > " + temp2
	os.system(cmd)
	fd = open(temp2,"r")
	data = fd.readline()
	fd.close()
	index = data.find(":")
	iftemp = data[index+2:]
	ifname = iftemp[:len(iftemp)-1]
	#print ifname
	
	cmd = "grep ifType." + str(i+1) + " mib.txt > " + temp2
	os.system(cmd)
	fd = open(temp2,"r")
	data = fd.readline()
	fd.close()
	index = data.find(":")
	iftemp = data[index+2:]
	iftype = iftemp[:len(iftemp)-1]
	#print "iftype is ",iftype 

	cmd = "grep ifMtu." + str(i+1) + " mib.txt > " + temp2
	os.system(cmd)
	fd = open(temp2,"r")
	data = fd.readline()
	fd.close()
	index = data.find(":")
	iftemp = data[index+2:]
	ifmtu = iftemp[:len(iftemp)-1]
	#print "ifmtu is ",ifmtu 

	cmd = "grep ifPhysAddress." + str(i+1) + " mib.txt > " + temp2
	os.system(cmd)
	fd = open(temp2,"r")
	data = fd.readline()
	fd.close()
	index = data.find(":")
	iftemp = data[index+2:]
	ifaddr = iftemp[:len(iftemp)-1]
	#print "ifaddr is ",ifaddr 

	cmd = "grep ifAdminStatus." + str(i+1) + " mib.txt > " + temp2
	os.system(cmd)
	fd = open(temp2,"r")
	data = fd.readline()
	fd.close()
	index = data.find(":")
	iftemp = data[index+2:]
	ifstatus = iftemp[:len(iftemp)-1]
	#print "ifadminstatus is ",ifstatus
	
	print "name is ",ifname," type is ",iftype," mtu is ",ifmtu," addr is ",ifaddr," status is ",ifstatus
	

