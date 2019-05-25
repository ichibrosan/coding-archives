#!/usr/bin/python
# project Monday, January 14, 2008 COPR doug@goodall.com

# The purpose of this program is to encapsulate the functionality
# required to manage a three level authorization structure to 
# control access to the Virtual Protocol Adapter data.

import ConfigParser
import os

cfg = ConfigParser.ConfigParser()
cfg.read("/Users/doug/.vparc")
webroot = cfg.get("doug","public_html")

