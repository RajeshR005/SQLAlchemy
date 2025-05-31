from sqlalchemy import create_engine,Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

db_url="mysql+pymysql://root:2741@localhost:3307/studentdb"

engine=create_engine(db_url)
Base=declarative_base()

class Mixin(Base):
    __tablename__="mixin"
    id=Column(Integer,primary_key=True,autoincrement=True)
    created_by=Column(String(50),default="Admin")
    created_at=Column(DateTime,default=lambda: datetime.now(timezone.utc)) 
    updated_by=Column(String(50),default="Admin")
    updated_at=Column(DateTime,default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc))

class Students(Mixin,Base):
    __tablename__="students"
    student_id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50))
    department=Column(String(50))

class Staffs(Mixin,Base):
    __tablename__="staffs"
    staff_id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50))
    designation=Column(String(50))

class Courses(Mixin,Base):
    __tablename__="courses"
    course_id=Column(Integer,primary_key=True,autoincrement=True)
    course_name=Column(String(100))
    semester=Column(Integer) 

class Marks(Mixin,Base):
    __tablename__="marks"
    mark_id=Column(Integer,primary_key=True,autoincrement=True)
    student_id=Column(Integer,ForeignKey(Students.student_id))
    course_id=Column(Integer,ForeignKey(Courses.course_id))
    marks=Column(Integer)

class Course_allocation(Mixin,Base):
    __tablename__="course_allocation"
    allocation_id=Column(Integer,primary_key=True,autoincrement=True)
    staff_id=Column(Integer,ForeignKey(Staffs.staff_id))
    course_id=Column(Integer,ForeignKey(Courses.course_id))

