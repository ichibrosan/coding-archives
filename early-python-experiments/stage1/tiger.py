#!/usr/bin/python
# tiger 1/18/2008 COPR doug@goodall.com

import ConfigParser
import os

create = 1
webroot = ""

cfg = ConfigParser.ConfigParser()
if 1 == create:
	cfg.add_section("output")
	cfg.set("output","webroot",os.getenv("HOME")+"/Sites/")
	cfg.set("output","bgcolor","lightblue")
	cfg.set("output","filespec","index.html")
	cfg.set("output","text","darkblue")
	cfg.set("output","title","Tiger.Py Autogenerating Web Pages")
	fd = open("tiger.cfg","w")
	cfg.write(fd)
	fd.close()
bgcolor = cfg.get("output","bgcolor")
text = cfg.get("output","text")
title = cfg.get("output","title")
webroot = cfg.get("output","webroot")

fd = open(webroot + "index.html","w")
fd.write("<html>")
fd.write("<head>")
fd.write("<title>" + title + "</title>")
fd.write("</head>")
fd.write("<body text=\"" + text + "\" bgcolor=\"" + bgcolor  + "\">")
fd.write("this is the body")
fd.write("<p>Copyright &#169; 2008 " + \
			"doug@goodall.com. All Rights Reserved.");
fd.write("</body>")
fd.write("</html>")
fd.close()

