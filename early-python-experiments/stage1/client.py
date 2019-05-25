#!/usr/bin/python
#############################################
# client.py 6/25/2009 COPR doug@goodall.com #
#############################################

from socket import *
import stdlib
import sys
import xdrlib
import rfc1833
query = "system.sysDescr.0"
shost = "localhost"
sport = 2777
transaction = 1
req = xdrlib.Packer()
req.pack_uint(transaction)
req.pack_uint(rfc1833.RPC_CALL)
req.pack_uint(rfc1833.RPC_VERSION)
req.pack_uint(rfc1833.MY_PROGRAM_ID)
req.pack_uint(rfc1833.MY_VERSION_ID)
req.pack_uint(rfc1833.PROC_ONE)
req.pack_uint(rfc1833.AUTH_NULL)
req.pack_uint(rfc1833.AUTH_NULL)
req.pack_uint(rfc1833.AUTH_NULL)
req.pack_uint(rfc1833.AUTH_NULL)
req.pack_string(query)
request = req.get_buffer()
so = socket(AF_INET,SOCK_STREAM) 
so.connect((shost,sport)) 
so.send(request)
response = so.recv(1024)
so.close()
rsp = xdrlib.Unpacker(response)
trans  = rsp.unpack_uint()
func   = rsp.unpack_uint()
rpcv   = rsp.unpack_uint()
prog   = rsp.unpack_uint()
vers   = rsp.unpack_uint()
proc   = rsp.unpack_uint()
auth1 = rsp.unpack_uint()
auth2 = rsp.unpack_uint()
auth3 = rsp.unpack_uint()
auth4 = rsp.unpack_uint()
data = rsp.unpack_string()
print data
if auth1 == stdlib.EXIT_SUCCESS:
	print "EXIT_SUCCESS"
if auth1 == stdlib.EXIT_FAILURE:
	print "EXIT_FAILURE"

