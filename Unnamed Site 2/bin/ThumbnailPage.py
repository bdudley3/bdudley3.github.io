import os

def makeSamplePage(directory):
  samplesFile=open("C:\\Users\\B114.CAMPUS.004\\ch 13 stuff\\SamplePage.html","wt")
  samplesFile.write(doctype())
  samplesFile.write(title("Samples from "+directory))
  
  samples="<h1>Welcome to the Samples from "+directory+" </h1>"
  for file in os.listdir(directory):
    if file.endswith(".jpg"):
      samples=samples+"<p>Filename: "+file
      samples=samples+'<image src="'+file+'"height="100"></p>'
  samplesFile.write(body(samples))
  samplesFile.close()

  
  
  
#ch. 13 - p. 368