#!/usr/bin/python
# vpaconfig.py

import ConfigParser
import os

cfg = ConfigParser.ConfigParser()
cfg.add_section ("user")
cfg.add_section("group")
cfg.add_section("world")
fd = open("/Users/doug/.vparc","w")
cfg.write(fd)
fd.close()


