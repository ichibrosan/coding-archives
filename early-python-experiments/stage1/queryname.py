#!/usr/bin/python
# queryname 1/7/2008 COPR doug@goodall.com

# The purpose of this program is to look up the service number starting
# with the frame type and service name using the name2svc.cfg file
# that was created by the services.py program in a previous operation. 

import ConfigParser

cfg = ConfigParser.ConfigParser()
cfg.read("name2svc.cfg")

print cfg.get("udp","bgmp")
