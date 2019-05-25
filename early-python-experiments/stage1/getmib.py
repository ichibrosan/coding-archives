#!/usr/bin/python 
############################################ 
# getmib.py 1/6/2008 COPR doug@goodall.com # 
############################################ 

import os
#import tempfile
#temp = tempfile.mktemp()
temp = "mib.txt"
cmd = "snmpwalk -Os -c public -v 1 localhost > " + temp
os.system(cmd)
#fd = open(temp,"r")
#data = fd.read(150000)
#print "Response is ",data

