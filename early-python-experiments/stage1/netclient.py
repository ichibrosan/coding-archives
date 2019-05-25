#!/usr/bin/python
# netclient.py

import ConfigParser
import netdebug
from socket import *
import stdlib
import sys
import xdrlib
import rfc1833
program = "netclient2"
config    = program + ".cfg"

if 1:
	ident = program + " 1/6/2008 COPR doug@goodall.com "	
	cfg = ConfigParser.ConfigParser()
	cfg.add_section(program)
	cfg.set(program,"program",ident)
	cfg.set(program,"debug","true")
	file = open(config,"w")
	cfg.write(file)
	file.close()

cfg = ConfigParser.ConfigParser()
cfg.read(config)

if "true" == cfg.get(program,"debug"):
	netdebug.puts(cfg.get(program,"program"))

data = "Platform is " + sys.platform
netdebug.puts(data)

data = "Version is " + sys.version
netdebug.puts(data)

netdebug.puts("The program completed successfully")
