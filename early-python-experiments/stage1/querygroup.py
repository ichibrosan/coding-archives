#!/usr/bin/python
# querygroup.py 1/8/2008 COPR doug@goodall.com

# The purpose of this program is to test the ConfigParser
# database containing the contents of the /etc/group file
# available both by name and by number.

import ConfigParser

cfg = ConfigParser.ConfigParser()
cfg.read("group.cfg")

print "admin is " + cfg.get("byname","admin")

print "69    is " + cfg.get("bynumber","69")

