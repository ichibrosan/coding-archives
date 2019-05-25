#!/usr/bin/python
# tester.cgi 1/8/2008 COPR doug@goodall.com. All Rights Reserved.

print "Content-type:	text/html\r\r"

html = """
	<h2>/Users/doug/Sources/pages/query2.cgi</h2>
	<h2>http://MacBookPro.local/query2.cgi</h2>
	<html><head><title>
	/Users/doug/Sources/pages/submit.cgi
	</title></head><body>
	<form method=post action="submit.cgi">
	<p><table><tr><th align=right>Name:
	<td><input type=text name=name>
	<tr><th align=right>Rank:<td><select name=rank>
	<option>General<option>Captain<option>Private
	</select><tr><th align=right>Serial Number:
	<td><input type=text name=sernum>
	<tr><td colspan=2 align=center>
	<input type=submit value="Send">
	</table></form></body></html>
	"""

print html 
