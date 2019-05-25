#!/usr/bin/python
# getprotocols.py 1/8/2008 COPR doug@goodall.com

# The purpose of this program is to parse the /etc/protocols
# file into the protocols.cfg file alloowing the lookup of any
# protocol on the basis of any field. This is big fun :-)

import ConfigParser

cfg = ConfigParser.ConfigParser()
cfg.add_section("numberbyprot")
cfg.add_section("pseudobyprot")
cfg.add_section("remarkbyprot")
cfg.add_section("protbynumber")
cfg.add_section("pseudobynumber")
cfg.add_section("remarkbynumber")
cfg.add_section("protbypseudo")
cfg.add_section("numberbypseudo")
cfg.add_section("remarkbypseudo")
cfg.add_section("protbyremark")
cfg.add_section("numberbyremark")
cfg.add_section("pseudobyremark")

fp = open("/etc/protocols","r")
for tmp in fp.readlines():
	if "#" != tmp[0]:
		size = len(tmp)
		buf = tmp[0:size-1]
		print "---------------------"
		print  buf
		index = 0
		endex = buf.find("\t")
		if -1 == endex:
			endex = buf.find(" ")
		sProt = buf[:endex]		
		index = endex		
		while " " == buf[index]:
			index += 1
		while "\t" == buf[index]:
			index += 1
		endex = buf.find("\t",index)
		if -1 == endex:
			endex = buf.find(" ")
		sProtNum = buf[index:endex]
		index = endex
		while "\t" == buf[index]:
			index += 1
		endex = buf.find("\t",index)
		if -1 == endex:
			endex = buf.find(" ",index)
		sPseudo = buf[index:endex]
		index = endex
		# several protocols don't have a remark
		sRemark = "(none)"
		index = buf.find("#")
		if -1 != index:
			sRemarks = buf[index+2:]
		print "sProt    is " + sProt
		print "sProtNum is " + sProtNum
		print "sPseudo  is " + sPseudo
		print "sRemarks is " + sRemarks

 		cfg.set("numberbyprot",sProt,sProtNum)
		cfg.set("pseudobyprot",sProt,sPseudo)
		cfg.set("remarkbyprot",sProt,sRemarks)
		cfg.set("protbynumber",sProtNum,sProt)
		cfg.set("pseudobynumber",sProtNum,sPseudo)
		cfg.set("remarkbynumber",sProtNum,sRemarks)
		cfg.set("protbypseudo",sPseudo,sProt)
		cfg.set("numberbypseudo",sPseudo,sProtNum)
		cfg.set("remarkbypseudo",sPseudo,sRemarks)
		cfg.set("protbyremark",sRemarks,sProt)
		cfg.set("numberbyremark",sRemarks,sProtNum)
		cfg.set("pseudobyremark",sRemarks,sPseudo)

fp.close()

fp = open("protocols.cfg","w")
cfg.write(fp)
fp.close()
