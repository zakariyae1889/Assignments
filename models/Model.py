from WebSite.Data.data import DataConnect 
class DataModel():
   DataConnect()
   global DataModel
   #insert Courses
   def insertCourses(self,CourseName):
    DataModel=DataConnect()
    DataModel.my_cur.execute("insert into Courses(CourseName) values('"+CourseName+"')")
    DataModel.mydb.commit()
    return DataModel
   # select courses
   def selectCourses():
      DataModel=DataConnect()
      DataModel.my_cur.execute("select CourseID,CourseName from courses")
      Data= DataModel.my_cur.fetchall()
      return Data
   #delete courses
   def DeleteCourses(self,IDCourse):
      DataModel=DataConnect()
      DataModel.my_cur.execute("delete from courses where CourseID='"+IDCourse+"' ")
      DataModel.mydb.commit()
      return DataModel
   #DesplayCoures
   def DesplayCourse():
      DataModel=DataConnect()
      DataModel.my_cur.execute("select * from courses")
      Data= DataModel.my_cur.fetchall()
      return Data
   #Dropdownlist
   def Dropdownlist(id):
      DataModel=DataConnect()
      DataModel.my_cur.execute("select * from courses where CourseID=%s",[id])
      Data= DataModel.my_cur.fetchall()
      return Data
   #insertAssignment
   def insertAssignments(self,Description,CourseID):
      DataModel=DataConnect()
      
      DataModel.my_cur.execute("insert into assignments(Description,CourseID) values('"+Description+"','"+CourseID+"') ")
      DataModel.mydb.commit()
      return DataModel
   #selectAssignment
   def selectAssignment():
    DataModel=DataConnect()
    DataModel.my_cur.execute("select assignments.AssignmentID, courses.CourseName,assignments.Description from courses inner join assignments on assignments.CourseID=courses.CourseID")
    Data= DataModel.my_cur.fetchall()
    return Data
   #delete assignments
   def DeleteAssignments(self,AssignmentID):
      DataModel=DataConnect()
      DataModel.my_cur.execute("delete from assignments where AssignmentID='"+AssignmentID+"' ")
      DataModel.mydb.commit()
      return DataModel
   
  
      
      
   
    

       
       
       
   
    
