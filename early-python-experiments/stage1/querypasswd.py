#!/usr/bin/python
# querypasswd.py 1/8/2008 COPR doug@goodall.com

# The purpose of this program is to test the passwd database
# created by the getpasswd.py program in an earlier step.
# This script uses various lookup methods (see below).

import ConfigParser

cfg = ConfigParser.ConfigParser()
cfg.read("passwd.cfg")

print "user  is "   + cfg.get("userbyuid","0")
print "uid   is "   + cfg.get("uidbyuser","root")
print "gid   is "   + cfg.get("gidbyuser","root")
print "descr is " + cfg.get("descrbyuser","root")
print "home  is " + cfg.get("homebyuser","root")
print "shell is " + cfg.get("shellbyuser","root")

