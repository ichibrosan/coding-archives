#!/usr/bin/python
# getpasswd.py 1/8/2008 COPR doug@goodall.com 

# The purpose of this program is to parse the /etc/passwd file
# and place the resilts in a ConfigParse compatible database
# that can be queried either by name or by userid.

import ConfigParser
import os
import sys

cfg = ConfigParser.ConfigParser()
cfg.add_section("userbyuid")
cfg.add_section("uidbyuser")
cfg.add_section("gidbyuser")
cfg.add_section("descrbyuser")
cfg.add_section("homebyuser")
cfg.add_section("shellbyuser")
fp = open("/etc/passwd","r")
for buf in fp.readlines():
	if "#" != buf[0]:
		index = 0
		endex = buf.find(":")
		sUser = buf[index:endex]
		index = endex + 3
		endex = buf.find(":",index)
		sUID = buf[index:endex]
		index = endex + 1
		endex = buf.find(":",index)
		sGID = buf[index:endex]
		index = endex + 1
		endex = buf.find(":",index)
		sDescr = buf[index:endex]
		index = endex + 1
		endex = buf.find(":",index)
		sHome = buf[index:endex]
		index = endex + 1
		endex = buf.find(":",index)
		sShell = buf[index:endex]				
		cfg.set("userbyuid",sUID,sUser)
		cfg.set("uidbyuser",sUser,sUID)
		cfg.set("gidbyuser",sUser,sGID)
		cfg.set("descrbyuser",sUser,sDescr)
		cfg.set("homebyuser",sUser,sHome)
		cfg.set("shellbyuser",sUser,sShell)
fp.close()
fp = open("passwd.cfg","w")
cfg.write(fp)
fp.close()


