#!/usr/bin/python
# services 1/7/2008 COPR doug@goodall.com

# The purpose of this program is traverse the services file and to create
# two ConfigParser compliant files to be used to look up services by name
# or by number. Two example programs are used to test this, queryname.py
# and querysvc.py.

import ConfigParser
import string

cfg1 = ConfigParser.ConfigParser()
cfg1.add_section("ddp")
cfg1.add_section("udp")
cfg1.add_section("tcp")
cfg1.add_section("sct")
cfg1.add_section("div")

cfg2 = ConfigParser.ConfigParser()
cfg2.add_section("ddp")
cfg2.add_section("udp")
cfg2.add_section("tcp")
cfg2.add_section("sct")
cfg2.add_section("div")

fd = open("/etc/services","r")
for buf in fd.readlines():
	if "#" != buf[0]:
		if " " != buf[0]:
			if "\t" != buf[0]:
				index = 0
				size = len(buf)
				buf2 = buf[0:size-1]
				endex = 0
				while buf2[endex] != " " and buf2[endex] != "\t":
					endex += 1
				name = buf2[0:endex]
				index = endex			
				while r"\t" == buf2[index]  or " " == buf2[index]:
					index += 1
				endex = buf2.find("/",index)
				svcstr = buf2[index:endex]
				svcnum = string.atoi(svcstr)
				svcstr = str(svcnum )
				index = endex + 1
				frmstr = buf2[index:index+3]
				#print "frmstr is ",frmstr," name is ",name," svcstr is ",svcstr
				cfg1.set(frmstr,name,svcstr)
				cfg2.set(frmstr,svcstr,name)
				
fd2 = open("name2svc.cfg","w")
cfg1.write(fd2)
fd2.close()

fd3 = open("svc2name.cfg","w")
cfg2.write(fd3)
fd3.close()

			
			