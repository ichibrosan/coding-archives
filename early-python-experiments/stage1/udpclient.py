#!/usr/bin/python
# udpclient 1/6/2008 COPR doug@goodall.com

import socket
import xdrlib
import zlib

HOST = "localhost"
PORT = 2293

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
p = xdrlib.Packer()
p.pack_string(zlib.compress("From: com.goodall.mbp.udpclient"))
p.pack_string(zlib.compress("To:   com.goodall.mbp.udpserver"))
p.pack_string(zlib.compress("Subj: Debug Packet from Client to NPDBGMNGR"))
p.pack_string(zlib.compress("Data: shdlfjkhsdl kjfhadls jkfha sldkjf ")) 
data = p.get_buffer()
s.sendto(data,(HOST,PORT))

