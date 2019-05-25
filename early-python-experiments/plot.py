
import os
import tempfile
temp = tempfile.mktemp()
sample = "/Users/doug/Sources/Python/sample.txt"
cmd = "ls -l -g " + sample + "> " + temp
os.system(cmd) 
fd = open(temp,"r")
buf = fd.readline()
stuff = "Analysis of " + buf + "<p>"
fd2 = open(sample,"r")
for buf in fd2.readlines():
	index = 0
	sTime = buf[index:index+15]
	index += 16
	endex = buf.find(" ",index)
	sFrame = buf[index:endex]
	index = endex + 1
	endex = buf.find(".",index)
	sOctet1 = buf[index:endex]
	index = endex + 1
	endex = buf.find(".",index)
	sOctet2 = buf[index:endex]
	index = endex + 1
	endex = buf.find(".",index)
	sOctet3 = buf[index:endex]
	index = endex + 1
	endex = buf.find(".",index)
	sOctet4 = buf[index:endex]
	index = endex + 1
	endex = buf.find(" ",index)
	sPort = buf[index:endex]
	index = endex + 3
	endex = buf.find(".",index)
	dOctet1 = buf[index:endex]
	index = endex + 1
	endex = buf.find(".",index)
	dOctet2 = buf[index:endex]
	index = endex + 1
	endex = buf.find(".",index)
	dOctet3 = buf[index:endex]
	index = endex + 1
	endex = buf.find(".",index)
	dOctet4 = buf[index:endex]
	index = endex + 1
	endex = buf.find(":",index)
	dPort = buf[index:endex]
	SourceIP  = sOctet1  + "." + sOctet2 + "." + sOctet3 + "." + sOctet4 
	DestIP    = dOctet1  + "." + sOctet2 + "." + dOctet3 + "." + dOctet4
	SourceIPp = SourceIP + "." + sPort
	DestIPp   = DestIP   + "." + dPort
fd2.close()


