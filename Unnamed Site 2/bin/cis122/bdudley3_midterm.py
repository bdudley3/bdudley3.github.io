def bdudley3_midterm():   
  file = pickAFile()  
  source = makePicture(file)  
  mirrorPoint = getHeight(source) / 2  
  midPoint = getWidth(source) / 2  
  width = getWidth(source)  
  height = getHeight(source)  
  for x in range(0,getWidth(source)):  
    for y in range(0,mirrorPoint):  
      topPixel = getPixel(source,x,y)  
      bottomPixel = getPixel(source,x,height - y - 1)  
      color = getColor(topPixel)  
      setColor(bottomPixel,color) 
  for p in getPixels(source): 
    intensity = (getRed(p)+getGreen(p)+getBlue(p)) / 3 
    x = getX(p) 
    y = getY(p) 
    if x < midPoint and y < mirrorPoint: 
      setColor(p,makeColor(intensity,intensity,intensity)) 
    if x > midPoint and y < mirrorPoint: 
      setColor(p,makeColor(getRed(p)*1.25,getBlue(p)*1.25,getGreen(p)))
    if y > mirrorPoint and intensity < 50:
      setColor(p,black)
    elif y > mirrorPoint and intensity < 100:
      setColor(p,white)
    elif y > mirrorPoint and intensity > 100:
      setColor(p,red)
  explore(source)  
 