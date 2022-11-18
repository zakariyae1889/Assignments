from flask import Blueprint,render_template,request,redirect,flash,url_for,jsonify
from WebSite.models.Model import DataModel
Data= DataModel()
view=Blueprint("view",__name__)
@view.route("/")
def PageAssignments():
    
    data=DataModel.DesplayCourse()
    data1=DataModel.selectAssignment()
   
    return render_template("Assignments.html",data=data,data1=data1)


@view.route("/Course")
def PageHome():
    data=DataModel.selectCourses()
    return render_template("Courses.html",data=data)



@view.route("/AddCourse",methods=["POST","GET"])
def AddCourse():
    if request.method=="POST":
        nameCoures=request.form["Course"]
        Data.insertCourses(nameCoures)
        flash("element Add Successfulye",category="Successfully")
        return redirect(url_for("view.PageHome"))
    return redirect(url_for("view.PageHome"))


@view.route("/DeleteCourses/<CourseID>")
def DeleteCourses(CourseID):
    Data.DeleteCourses(CourseID)
    flash("element Delete Successfulye",category="Successfully")
    return redirect(url_for("view.PageHome"))

@view.route("/CourseID/<get_CourseID>")
def CourseID(get_CourseID):
    
    datamodel=DataModel.Dropdownlist(get_CourseID)
    
    ID_Array=[]
    for row in datamodel:
        ID_OBject={
            'id':row[0],
            "name":row[1]
        }
    ID_Array.append(ID_OBject)
    return jsonify({"Course_ID":ID_Array})

@view.route("/AddAssignments",methods=["POST","GET"])
def AddAssignments():
    if request.method=="POST":
        Description=request.form["Description"]
        CourseName=request.form.get("CourseName")
        
        
       
        Data.insertAssignments(Description,CourseName)
        flash("element Add Successfulye",category="Successfully")
        return redirect(url_for("view.PageAssignments"))
    return redirect(url_for("view.PageAssignments"))
    
@view.route("DeleteAssignments/<IDAssignments>")
def DeleteAssignments(IDAssignments):
    Data.DeleteAssignments(IDAssignments)
    flash("element Delete Successfulye",category="Successfully")
    return redirect(url_for("view.PageAssignments"))


