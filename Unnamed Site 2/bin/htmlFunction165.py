#program 165 - p. 372

import shelve
def createDatabases():
  students=shelve.open(getMediaPath("\\students.db"),"c")
  row = {'StudentName':'Katie','StudentID':'S1'}
  students['S1']=row
  row = {'StudentName':'Brittany','StudentID':'S2'}
  students['S2']=row
  row = {'StudentName':'Carrie','StudentID':'S3'}
  students['S3']=row
  students.close()
  
  pictures=shelve.open(getMediaPath("\\pictures.db"),"c")
  row = {'Picture':'Class1.jpg','PictureID':'P1'}
  pictures['P1']=row
  row = {'Picture':'Class2.jpg','PictureID':'P2'}
  pictures['P2']=row
  pictures.close()
  
  pictures=shelve.open(getMediaPath("\\pict-students.db"),"c")
  row = {'PictureID':'P1','StudentID':'S1'}
  pictures ['P1S1']=row
  row = {'PictureID':'P1','StudentID':'S2'}
  pictures['P1S2']=row
  row = {'PictureID':'P2','StudentID':'S3'}
  pictures['P2S3']=row
  pictures.close()