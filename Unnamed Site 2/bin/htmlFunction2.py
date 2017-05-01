def makeCatalog(product, image, price):
  file=open("C:\\Users\\B114.CAMPUS.004\\ch 13 stuff\\catalog.html","wt")
  body = """<!DOCTYPE html>
  
<html>
<head>
<title>Catalog Page for:"""+ product+'''</title>
</head>
<body>

<h1>'''+product+""" is the greatest!</h1>
<p>You are so lucky to have found this page! You have the opportunity to buy """+product+""" for the low, low price of $"""+str(price)+'''.</p>
<p><em>Emphasized text</em> Just take a look at this beauty!</p>
<img src="'''+image+'''" height = 100></p>
<p>Get one today!</p>
</body>
</html>'''
  file.write(body)
  file.close()