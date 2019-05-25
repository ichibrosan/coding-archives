# netdebug 1/6/2008 COPR doug@goodall.com

import socket
import time
import xdrlib
import zlib

def puts(data):
	HOST = "localhost"
	PORT = 2293
	now = time.time()
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	p = xdrlib.Packer()
	p.pack_string(zlib.compress("From: com.goodall.mbp.udpclient"))
	p.pack_string(zlib.compress("To:   com.goodall.mbp.udpserver"))
	date = "Date: " + time.asctime(time.localtime(now)) 
	p.pack_string(zlib.compress(date))
	p.pack_string(zlib.compress("Subj: Debug Packet from Client to NPDBGMNGR"))
	p.pack_string(zlib.compress(data)) 	
	packet = p.get_buffer()
	s.sendto(packet,(HOST,PORT))

