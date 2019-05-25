#!/usr/bin/python
# m1c1.cgi 1/12/2008 COPR doug@goodall.com. All Rights Reserved.
# called by /Users/doug/Sources/saturday.py from command line.

# The purpose of this program is to receive variables from a 
# web page and use them to define a "new project". When we
# discuss the concept of "a project" in the VPA, we are 
# addressing the selection of a set of configuration items
# that define the purpose and parameters of an analysis
# activity.

# A project consists of a collection of data which is stored
# on the hard disk in a directory. This directory is usually
# within the home directory of a specific user, root or
# otherwise. Because for the tme being, the application is
# implemented in Python, the configuration variables are
# stored and accessed using the ConfigParser style files
# within the project directory.
# Let us start with the concept of Application and User
# configurations.

# Application Configuration --
#
# The VPA Application may be customized by creating and editing
# application configuration files in /Library/Application Support/VPA.
#
# The VPA User configuration is configured through the creation 
# and editing of a link file, and application subdirectory. 
# To begin with, an application directory is created in 
# /Users/doug/Library/Application Support/VPA.
# Once the application directory has been created, a local link
# file is created that specifies the location of the application 
# directory. Although the application directory is in 
# /Users/.../Library/Application Support by default, it can be
# somewhere else as long as the ~/.vparc file contains a pointer
# to the actual location. The application can be on a remote file
# system although there would be a performance penalty.

# The format of the global configuration file is 
#
#	[localconfig]
#	filespec= "/Library/Application Support/VPA/local.cfg"

# The format of the local configuration file is
#
#	[userconfig]
# 	filespec = "~/Library/Application Support/VPA/user.cfg
#
# or
#
# [userconfig]
#	filespec = "~/.vparc
#

# As you can see, the global configuration is not in the home
# directory of the user and can therefore be secured. The
# global configuration can either be an enterprise level 
# configuration or a site level configuration. 

# The global configuration specifies the location of the local 
# configuration which may also be outside the user's home 
# directory as well as any variables that need to be globally 
# specified.

# The local configuration file specifies the location of the 
# user configuration as well as any variable that need to be
# locally specified.

# The user configuration file contains and remaining items
# that have not been previously specified at higher levels.
# Due to this layered configuration architecture, there is
# a high degree of administrative control over the capabilities
# and functionality of the program and the location of its
# inputs and outputs.


# The Virtual Protocol Adapter (VPA) consists of a body of
# program code, the application  configuration , and the user
# configuration. When these three items are present, the 
# application knows how to do, and what and where to do it.
# The program

# In order to emphasize the global and local configuration
# values over the user configuration, the program reads the
# global configuration first This global configuration includes
# a pointer to the local configuration which may either exist 
# physically on the local machine or on a local network file
# system. The local configuration file specifies the naming
# convention for the user specific configuration file.

import cgi; form = cgi.FieldStorage()
print "Content-type:	text/html\r\r"

class localvars():
	samplevar = 1
	
html = """
	<h2>/Users/doug/Sources/pages/m1c1.cgi</h2>
	<h2>http://MacBookPro.local/m1c1.cgi</h2>
	<html><head><title>
	/Users/doug/Sources/pages/m1c1.cgi
	</title></head><body><h2>
	<p> Name    is %(name)s 
	<p> Rank     is %(rank)s
	<p> Sernum is %(sernum)s
	</h2></body></html>
	"""

local = localvars

data = {}
for field in ('name', 'rank', 'sernum'):
	if not form.has_key(field):
		data[field] = '(unknown)'
	else:
		if type(form[field]) != list:
			data[field] = form[field].value
		else:
			values = [x.value for x in form[field]]
			data[field] = ' and '.join(values)
			
local.projname = form['name'].value	
local.myrank    = form['rank'].value
local.sernum    = form['sernum'].value

print html % data
