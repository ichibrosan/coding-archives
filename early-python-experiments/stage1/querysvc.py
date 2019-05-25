#!/usr/bin/python
# querysvc 1/7/2008 COPR doug@goodall.com

# The purpose of this program is to look up the service name starting
# with the frame type and service number using the svc2name.cfg file
# that was created by the services.py program in a previous operation. 

import ConfigParser

cfg = ConfigParser.ConfigParser()
cfg.read("svc2name.cfg")

print cfg.get("udp","264")
