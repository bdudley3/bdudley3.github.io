#Program 169 - p. 377

import urllib
import random
import anydbm

def makeHomePage1(name,interests):
  file=open(pickAFile("C:\\Users\\B114.CAMPUS.004\\ch 13 stuff\\homepage1.html"),"wt")
  file.write(doctype())
  file.write(title(name+"'s Home Page"))
  text = "<h1>Welcome to "+name+"'s Home Page</h1> "
  text += " I am interested in "+interests+"</p>"
  text += "<p>Random thought for the day: "+tagline()+"</p>"
    
  db=anydbm.open(getMediaPath("\\news"),"r")
  text += "<h2>Latest news:"+db["headline"]+"</h2>"
  text += "<p>"+db["story"]+"</p>"
  file.write(body(text))
  file.close()
  
def doctype():
  return '<!DOCTYPE html>'
    
def title(titlestring):
  return "<html><head><title>"+titlestring+"</title></head>"
    
def body(bodystring):
  return "<body>"+bodystring+"</body></html>"    
    
def tagline():
  tags = []
  tags += ["After all is said... bla lb bla."]
  tags += ["When you do this, you did this..."]
  tags += ["Willyoupleaseasfeshgdskjgahdskjahgs."]
  return random.choice(tags)