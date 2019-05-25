#!/usr/bin/python
# ifconfig.py 2008/02/13 COPR douglas_goodall@mac.com

import os
import sys
import tempfile

iface = "en1"
tempfile =tempfile.mktemp()
print "tempfile is " + tempfile
cmd = "ifconfig " + iface + " > " + tempfile
os.system(cmd)
fd = open(tempfile,"r")
data = fd.read(1024)
#---------------------
index = 0 ; endex = data.find(":")
sIface = data[0:endex] ; index = endex + 8
sKey = "flags" ; print "sKey is " + sKey
endex = data.find("<",index)
sValue = data[index:endex] ; print "sValue is " + sValue
#---------------------------
index = endex + 1 ; endex = data.find(">",index)
#-----------------------------
index = endex + 2 ; endex = data.find(" ",index)
sKey = data[index:endex] ; print "sKey is ",sKey
index = endex + 1 ; endex = data.find("\t",index)
sValue = data[index:endex-1] ; print "sValue is ",sValue
#------------------------------
index = endex + 1 ; endex = data.find(" ",index)
sKey = data[index:endex] ; print "sKey is " + sKey
index = endex + 1 ; endex = data.find(" ",index)
sValue = data[index:endex] ; print "sValue is " + sValue
#-----------------------------
index = endex + 1 ; endex = data.find(" ",index)
sKey = data[index:endex] ; print "sKey is " + sKey
index = endex + 1 ; endex = data.find(" ",index)
sValue = data[index:endex] ; print "sValue is " + sValue
#----------------------------
index = endex + 1 ; endex = data.find(" ",index)
sKey = data[index:endex] ; print "sKey is " + sKey
index = endex + 1 ; endex = data.find(" ",index)
sValue = data[index:endex] ; print "sValue is " + sValue
#----------------------------
index = endex + 3 ; endex = data.find(" ",index)
sKey = data[index:endex] ; print "sKey is " + sKey
index = endex + 1 ; endex = data.find(" ",index)
sValue = data[index:endex] ; print "sValue is " + sValue
#-----------------------------
index = endex + 1 ; endex = data.find(" ",index)
sKey = data[index:endex] ; print "sKey is " + sKey
index = endex + 1 ; endex = data.find(" ",index)
sValue = data[index:endex] ; print "sValue is " + sValue
#------------------------------
index = endex + 1 ; endex = data.find(" ",index)
sOption = data[index:endex] ; print "sOption is " + sOption 
#------------------------------
index = endex + 3 ; endex = data.find(" ",index)
sKey = data[index:endex] ; print "sKey is " + sKey
index = endex + 1 ; endex = data.find(" ",index)
sValue = data[index:endex] ; print "sValue is " + sValue
#-----------------------------
index = endex + 1 ; endex = data.find(" ",index)
sKey = data[index:endex] ; print "sKey is " + sKey
index = endex + 1 ; endex = data.find(" ",index)
sValue = data[index:endex] ; print "sValue is " + sValue
#------------------------------
index = endex + 1 ; endex = data.find(" ",index)
sKey = data[index:endex] ; print "sKey is " + sKey
index = endex + 1 ; endex = data.find("\t",index)
sValue = data[index:endex-1] ; print "sValue is " + sValue
#-------------------------------
index = endex + 1 ; endex = data.find(" ",index)
sKey = data[index:endex] ; print "sKey is " + sKey
index = endex + 1 ; endex = data.find(" ",index)
sValue = data[index:endex] ; print "sValue is " + sValue
#-----------------------------
index = endex + 3 ; endex = data.find(":",index)
sKey = data[index:endex] ; print "sKey is " + sKey
index = endex + 2 ; endex = data.find(" ",index)
sValue = data[index:endex] ; print "sValue is " + sValue
#-----------------------------
index = endex + 1 ; endex = data.find(":",index)
sKey = data[index:endex] ; print "sKey is " + sKey
index = endex + 2 ; endex = data.find("\t",index)
sValue = data[index:endex-1] ; print "sValue is " + sValue
#-------------------------------
index = endex + 1 ; endex = data.find(":",index)
sKey = data[index:endex] ; print "sKey is " + sKey
index = endex + 2 ; endex = data.find(" ",index)
sValue = data[index:endex] ; print "sValue is " + sValue
#-------------------------------
