#!"C:\Python27\python.exe"
#!!!!!!!!!!!!!!!!!!!Anywhere it says "database insert" is for you to fill in. There also might be some database stuff that needs to be added to make this work.-SKML!!!!!!!!!!!!!!!!!!!!
#Note: This should be in the cgi-bin folder, and the name of the file is SignIn.py

import cgitb
cgitb.enable()

import cgi
form = cgi.#I'm not sure if this is supposed to be the name of the form (So: "SignIn()") or FieldStorage or some other code-SKML

user = form['username'].value
pw = form['pw'].value

usercheck = #database instert: set this to the username. It'll be the same thing if it exists.
pwcheck = #database insert: set this to the password from the database.

import sqlite3

conn = sqlite3.connect(#DatabaseName)
c = conn.cursor()

if (user == usercheck)
	if(pw == pwcheck)
		print "Content-Type: text/html"
		print # don't forget the extra newline
		
		print '''<html>
		<head>
			<title> Welcome!''' + 'form[username].value'  + '''</title>
		</head>
		
		<body>
			<h1> DATABASEINSERT USERNAME </h1>					<!-- We could add each element of the profile, but in the final product this is probably all we need. --->
			<h2> DATABASEINSERT FAVORITE TEAM </h2>
		</body>
		
		</html>'''
	else
		print 'Content-Type: text/html'
		print
	
		print '''<html>
		<head>
			<script> Window.alert(Incorrect password!') </script>		<!-- I don't actually know if these need a body or anything in order to execute the alert, or if the Javascript is enough. --->
		</head>
		<body>
		</body>
		</html>'''
else
	print 'Content-Type: text/html'
	print
	
	print '''<html>
	<head>
		<script> Window.alert(We have no profile with that username!) </script>
	</head>
	<body>
	</body>
	</html>