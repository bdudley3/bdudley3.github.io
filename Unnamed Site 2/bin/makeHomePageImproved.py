def makeHomePage(name, interest):
  file=open("C:\\Users\\B114.CAMPUS.004\\ch 13 stuff\\ImprovedHomePage.html","wt")
  file.write(doctype())
  file.write(title(name+"'s Home Page"))
  file.write(body("""
<h1>Welcome to """+name+"""'s Home Page</h1>
<p>Hi! I am """+name+""".  This is my Home Page! I like """+interest+"""</p>f"""))
  file.close()
  
  
def doctype():
  return '<!DOCTYPE html>'
  
def title(titlestring):
  return "<html><head><title>"+titlestring+"</title></head>"
  
def body(bodystring):
  return "<body>"+bodystring+"</body></html>"
  
  
  
#ch. 13 - p. 367