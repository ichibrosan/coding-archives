#!/usr/bin/python
#

import ConfigParser
import os

cfg = ConfigParser.ConfigParser()
cfg.read("passwd.cfg")

uid = os.getuid()
gid = os.getgid()

try:
	user =  cfg.get("userbyuid",str(uid))
except:
	user = "(unknown)"

print "I am " + user
