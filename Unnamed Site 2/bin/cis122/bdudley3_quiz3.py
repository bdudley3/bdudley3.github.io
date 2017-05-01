def bdudley3_quiz3(color):
  file = pickAFile()
  picture = makePicture(file)
  for p in getPixels(picture):
    if color == "red":
      value = getRed(p)
      setRed(p,value*1.5)
    elif color == "blue":
      value2 = getBlue(p)
      setBlue(p,value2*1.5)
    elif color == "green":
      value3 = getGreen(p)
      setGreen(p,value3*1.5)
    else:
      print "loser"
  explore(picture)
  writePictureTo(picture,"S:\_Braydon\pics\copyHarambe.jpg")
  