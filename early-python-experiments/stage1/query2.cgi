#!/usr/bin/python
# query2 1/8/2008 COPR doug@goodall.com. All Rights Reserved.

print "Content-type:	text/html\r\r"

html = """
<form action="http://www.biblegateway.com/quicksearch/" method="post">
<table border="1" cellspacing="0" cellpadding="2" style="border-color: #600;">
<tr><th style="background-color: #600; color:#fff; text-align: center; padding: 0 10px;">Lookup a word or passage in the Bible</th></tr>
<tr><td style="background-color: #fff; text-align: center; padding: 0 10px;">
<p style="margin-bottom: 0;">
<input type="text" name="quicksearch" /><br />
<input type="submit" value="Search BibleGateway.com" /><br />
</p>
<a href="http://www.biblegateway.com/" title="The Bible in multiple languages, versions, and formats">
<img src="http://www.biblegateway.com/images/logos/bglogo_sm.gif" width="146" height="44" alt="BibleGateway.com" border="0" /></a><br />
<small>
<a href="http://www.biblegateway.com/usage/form/">Include this form on your page</a><br />
</small>
</td></tr>
</table>
</form>
	"""

print html 

stuff = """
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
