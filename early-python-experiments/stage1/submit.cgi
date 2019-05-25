#!/usr/bin/python
# submit 1/8/2008 COPR doug@goodall.com. All Rights Reserved.
# called by /Users/doug/Sources/pages/query.cgi with a browser

import cgi; form = cgi.FieldStorage()
print "Content-type:	text/html\r\r"

html = """
	<h2>/Users/doug/Sources/pages/submit.cgi</h2>
	<h2>http://MacBookPro.local/submit.cgi</h2>
	<html><head><title>
	/Users/doug/Sources/pages/submit.cgi
	</title></head><body><h2>
	<p> Name    is %(name)s 
	<p> Rank     is %(rank)s
	<p> Sernum is %(sernum)s
	</h2></body></html>
	"""

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
print html % data
