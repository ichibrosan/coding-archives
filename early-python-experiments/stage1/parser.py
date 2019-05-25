#!/usr/bin/python
# parser.py 1/6/2008 COPR doug@goodall.com
# The purpose of this program is to read a file created by tcpdump
# and generate a variety of local web pages which can be browsed to
# examine network traffic. This version of the code is used when the
# tcpdump was done without the -f flag. Non-local IP numbers may be
# represented by fully qualified domain names as opposed to dotted 
# octets.

import os
#os.system("rm -f /Users/doug/Sources/pages/*")
fd1 = open("/Users/doug/Sources/pages/index.html","w")
fd1.write("<html><head><title>")
fd1.write("Index to parser.py generated dump pages")
fd1.write("</title></head><body>")
fd2 = open("/Users/doug/Sources/sample.txt","r")
for buf in fd2.readlines():
	index = 0
	sTime = buf[index:index+15]
	index += 16
	endex = buf.find(" ",index)
	sFrame = buf[index:endex]
	index = endex + 1
	endex = buf.find(">",index)
	SourceIP = buf[index:endex-1]
	index = endex + 2
	endex = buf.find(":",index)
	DestIP = buf[index:endex]
	filename = "W" + SourceIP + "-" + DestIP + ".html"
	fd3 = open(filename,"a")
	data = "<p>" + buf
	fd3.write(data)
	fd3.close()
	tag = "<p><a href=" + '"' + filename + '"' + "> " + SourceIP + " -> " + DestIP + "></a>"
	fd1.write(tag)
fd2.close()
fd1.write("</body>")
fd1.write("</html>")
fd1.close()


