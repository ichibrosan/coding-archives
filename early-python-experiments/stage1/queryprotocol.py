#!/usr/bin/python
# queryprotocol.py 1/8/2008 COPR doug@goodall.com

# The purpose of this program is to test the protocols database
# by looking up the icmp protocol using all of the various keys.
# The protocols.cfg file contains a section for each key type.

import ConfigParser

cfg = ConfigParser.ConfigParser()
cfg.read("protocols.cfg")

print
print "numberbyprot(icmp)     = ",cfg.get("numberbyprot","icmp")
print "pseudobyprot (icmp)    = ",cfg.get("pseudobyprot","icmp")
print "remarkbyprot (icmp)    = ",cfg.get("remarkbyprot","icmp")

print "protbynumber(1)        = ",  cfg.get("protbynumber","1")
print "pseudobynumber(1)      = ",cfg.get("pseudobynumber","1")
print "remarkbynumber(1)      = ",cfg.get("remarkbynumber","1")

print "protbypseudo(ICMP)     = ",   cfg.get("protbypseudo","ICMP")
print "numberbypseudo(ICMP)   = ",cfg.get("numberbypseudo","ICMP")
print "remarkbypseudo(ICMP)   = ",cfg.get("remarkbypseudo","ICMP")

print               "protbyremark(internet control message protocol)   = ", \
	    cfg.get("protbyremark","internet control message protocol")
print           "numberbyremark(internet control message protocol) = ", \
	cfg.get("numberbyremark","internet control message protocol")
print            "pseudobyremark(internet control message protocol) = ", \
	 cfg.get("pseudobyremark","internet control message protocol")
print

