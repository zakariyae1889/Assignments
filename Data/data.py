import mysql.connector
class DataConnect():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1889",
        database="assignments_tracker"
    )
    my_cur=mydb.cursor()
    my_cur.execute("create database if not exists assignments_tracker ")
    my_cur.execute("create table if not exists Courses(CourseID int primary key NOT NULL AUTO_INCREMENT,CourseName text) ")
    my_cur.execute("create table if not exists assignments(AssignmentID int primary key NOT NULL AUTO_INCREMENT ,Description text,CourseID int,foreign key(CourseID) references Courses(CourseID))")
    