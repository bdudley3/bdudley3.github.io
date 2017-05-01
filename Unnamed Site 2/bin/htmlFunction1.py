def makePage():
  file=open("C:\\Users\\B114.CAMPUS.004\\ch 13 stuff\\htmlThing1.html","wt")
  file.write("""<!DOCTYPE html>
  
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>A simple heading</h1>
<p>This is a paragraph in the simplest possible Web page.</p>
<p><em>Emphasized text</em> This is a paragraph in the simplest possible Web page.</p>
<ul>
<li>this is item 1</li>
<li>this is item 2</li>
<li>this is item 3</li>
</ul>
<ol>
<li>1</li>
<li>2</li>
<li>3</li>
</ol>
</body>
</html>""")
  file.close()