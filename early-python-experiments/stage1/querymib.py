#!/usr/bin/python

# The purpose of this program is to extract a mib value from a ConfigParser
# database created by the mib2cfg.py program.

import ConfigParser
import os
import tempfile

cfg = ConfigParser.ConfigParser()
cfg.read("mib.cfg")
print
buf = cfg.get("mib","sysName.0")
tmp = buf[9:]
size = len(tmp)
name = tmp[:size-1]
print "Management Information for ",name
print
buf = cfg.get("mib","sysDescr.0")
index = buf.find(":") + 1
index = buf.find(":",index)
endex = buf.find(":",index)
des1 = buf[9:index]
tmp2 = buf[endex+1:]
len2 = len(tmp2) - 1
des2 = tmp2[:len2]
print des1
print des2
print
buf = cfg.get("mib","sysContact.0")
tmp = buf[9:]
size = len(tmp)
pers = tmp[:size-1]
print pers
buf = cfg.get("mib","sysLocation.0")
tmp = buf[9:]
size = len(tmp)
loca = tmp[:size-1]
print loca
print
buf = cfg.get("mib","ifDescr.6")
tmp = buf[9:]
size = len(tmp)
iface = tmp[:size-1]
buf = cfg.get("mib","ifPhysAddress.6")
tmp = buf[9:]
size = len(tmp)
mac = tmp[:size-1]
temp = tempfile.mktemp()
cmd = "ifconfig " + iface + " | grep netmask > " + temp
os.system(cmd)
fd = open(temp,"r")
tmp = fd.readline()
index = tmp.find("t")+2
endex = tmp.find(" ",index)
ip = tmp[index:endex]
print iface,ip,"("+mac+")"
print
