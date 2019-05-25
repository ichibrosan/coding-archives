#!/usr/bin/python
# query.cgi 1/8/2008 COPR doug@goodall.com. All Rights Reserved.

import sys; sys.stdout.write("Content-type:	text/html\n\n")

print "<h2>/Users/doug/Sources/pages/query.cgi</h2>"
print "<h2>http://MacBookPro.local/query2.cgi</h2>"

print "<form method=post action=\"submit.cgi\">"
print "<p><table>"

print "<tr>"
print "<th align=right>Name:"
print "<td><input type=text name=name>"

print "<tr>"
print "<th align=right>Rank:"
print "<td><select name=rank>"
print "	<option>General"
print	"	<option>Captain"
print "	<option>Private"
print "	</select>"

print "<tr>"
print "<th align=right>Serial Number:"
print "<td><input type=text name=sernum>"

print "<tr>"
print "<td colspan=2 align=center>"
print "<input type=submit value=\"Send\">"

print "</table>"
print "</form>"
print "</pre><body></html>"
