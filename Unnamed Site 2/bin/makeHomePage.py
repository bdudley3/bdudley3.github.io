def makeHomePage(name, interest):
  file=open("C:\\Users\\B114.CAMPUS.004\\ch 13 stuff\\HomePage.html","wt")
  file.write("""<!DOCTYPE html>
  
<html>
<head>
<title>"""+name+"""'s Home Page</title>
</head>
<body>

<h1>Welcome to """+name+"""'s Home Page</h1>
<p>Hi! I am """+name+""".  This is my Home Page! I like """+interest+"""</p>
</body>
</html>""")
  file.close()
  
  
  
#ch. 13 - p. 366