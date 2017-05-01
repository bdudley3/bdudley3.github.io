#program 166 - p. 373/374

def whoInClass():
  pictures=shelve.open(getMediaPath("\\pictures.db"),"r")
  for key in pictures.keys():
    row = pictures[key]
    if row['Picture'] == 'Class1.jpg':
      id = row['PictureID']
  pictures.close()
  
  studentslist=[]
  pictures=shelve.open(getMediaPath("\\pict-students.db"),"c")
  for key in pictures.keys():
    row = pictures[key]
    if row['PictureID']==id:
      studentslist.append(row['StudentID'])
  pictures.close()
  print "We're looking for:",studentslist
    
  students = shelve.open(getMediaPath("\\students.db"),"r")
  for key in students.keys():
    row = students[key]
    if row['StudentID'] in studentslist:
      print row['StudentName'],"is in the picture"
  students.close()