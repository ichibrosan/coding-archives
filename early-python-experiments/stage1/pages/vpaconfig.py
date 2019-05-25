#!/usr/bin/python
# vpaconfig.py

import ConfigParser
import os

cfg = ConfigParser.ConfigParser()
cfg.add_section ("global")
cfg.add_section("local")
cfg.add_section("user")
fd = open("~.vparc","w")
cfg.write(fd)
fd.close()


