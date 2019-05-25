#!/usr/bin/python
# udpserver.py 1/6/2008 COPR doug@goodall.com

# The purpose of this module is to send a UDP packet to the udpserver
# containing debug information from a program under test. We are using
# the network platform debug manager port since it is already defined.

import socket
import xdrlib
import zlib

HOST = "localhost"
PORT = 2293
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while 1:
	data, client = s.recvfrom(1024)
	print "packet received from ",client
	p = xdrlib.Unpacker(data)
	fromstr = p.unpack_string()
	tostr     = p.unpack_string()
	datestr = p.unpack_string()
	subjstr   = p.unpack_string()
	datastr   = p.unpack_string()
	print zlib.decompress(fromstr)
	print zlib.decompress(tostr)
	print zlib.decompress(datestr)
	print zlib.decompress(subjstr)
	print zlib.decompress(datastr)
	print "-------------------------------------------"


