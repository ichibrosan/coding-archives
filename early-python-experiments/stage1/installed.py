#!/usr/bin/python
###############################################
# installed.py 1/4/2008 COPR doug@goodall.com #
###############################################
# The purpose of this program is to extract the names abd installation 
# dates for installed programs from the snmp mib into two files and then
# to extract from these files the string tokens contained therein. As a 
# proof of concept the tokens are then printed for observation.
# p.s. The snmpd must be running for this to work: "sudo snmpd" will do it
#########################################

import os
import sys
import tempfile

# extract installed program names from mib and write into installednames.txt
query = "hrSWInstalledName"
temp = tempfile.mktemp()
temp = "installednames.txt"
cmd = "snmpwalk -Os -c public -v 1 localhost " + query + " > " + temp 
os.system(cmd)
fd = open(temp,"r")
data = fd.read(16384)
fd.close()

# extract installed program dates from mib and write into installeddates.txt
query = "hrSWInstalledDate"
temp = tempfile.mktemp()
temp = "installeddates.txt"
cmd = "snmpwalk -Os -c public -v 1 localhost " + query + " > " + temp 
os.system(cmd)
fd = open(temp,"r")
data = fd.read(16384)
fd.close()

# reopen name and date files
fdn = open("installednames.txt","r")
fdd = open("installeddates.txt","r")

# for each installed program name
# hrSWInstalledName.1 = STRING: "Address Book 4.1"
for name in fdn.readlines():
	# also read installed program date info
	# hrSWInstalledDate.1 = STRING: 2007-12-3,19:22:14.0,-8:0
	date = fdd.readline()
	# parse up name and date lines in to desired tokens
	index = name.find(".",)
	indexbeg = index+1
	indexend = name.find(" ",indexbeg)
	indnumstr =  name[indexbeg:indexend]
	typebeg = indexend + 3
	typeend = name.find(":",indexend)
	typestr = name[typebeg:typeend]
	progbeg = typeend + 2
	prog = name[progbeg:]
	progend = prog.find('"',1)
	progstr = prog[1:progend]
	typeend = date.find(":")
	datebeg = typeend +2
	dateend = date.find(",",datebeg)
	datestr = date[datebeg:dateend]
	timebeg = dateend + 1
	timeend = date.find(",",timebeg)
	timestr = date[timebeg:timeend]
	tailbeg = timeend + 1
	tailstr = date[tailbeg:]
	# Prog:  Address Book 4.1  Date:  2007-12-3  Time:  19:22:14.0  Tail:  -8:0
	print "Prog: ",progstr," Date: ",datestr," Time: ",timestr," Tail: ",tailstr
	


	



