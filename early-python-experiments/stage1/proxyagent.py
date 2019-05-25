vi #!/usr/bin/python
################################################
# proxyagent.py 1/6/2008 COPR doug@goodall.com #
################################################

from socket import *
import os
import stdlib
import sys
import tempfile
import xdrlib
import rfc1833
shost = "localhost"
sport = 2777
so = socket(AF_INET,SOCK_STREAM) 
so.bind((shost,sport)) 
so.listen(1) 
co, ad = so.accept() 
data = co.recv(1024) 
req = xdrlib.Unpacker(data) 
trans = req.unpack_uint() 
func  = req.unpack_uint() 
rpcv  = req.unpack_uint() 
prog  = req.unpack_uint() 
vers  = req.unpack_uint() 
proc  = req.unpack_uint() 
auth1 = req.unpack_uint() 
auth2 = req.unpack_uint() 
auth3 = req.unpack_uint() 
auth4 = req.unpack_uint()
query = req.unpack_string()	
temp = tempfile.mktemp()
cmd = "snmpget -c public localhost " + query + " > " + temp 
os.system(cmd)
fd = open(temp,"r")
data = fd.read(1024)
fd.close()
auth1 = stdlib.EXIT_SUCCESS
rsp = xdrlib.Packer() 
rsp.pack_uint(trans) 
rsp.pack_uint(func) 
rsp.pack_uint(rpcv) 
rsp.pack_uint(prog) 
rsp.pack_uint(vers) 
rsp.pack_uint(proc) 
rsp.pack_uint(auth1) 
rsp.pack_uint(auth2) 
rsp.pack_uint(auth3) 
rsp.pack_uint(auth4) 
rsp.pack_string(data)
response = rsp.get_buffer() 
co.send(response) 
co.close() 
