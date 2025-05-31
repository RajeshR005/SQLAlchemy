from sqlalchemy import create_engine,Column,String,ForeignKey,Integer,DateTime,Date
from sqlalchemy.orm import declarative_base,relationship
from datetime import datetime,date,time

db_url="mysql+pymysql://root:2741@localhost:3307/studentmanagement"

engine=create_engine(db_url)

Base=declarative_base()



class People(Base):
    __tablename__="people"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50),nullable=False)
    gender=Column(String(50))
    department=Column(String(50),nullable=False)
    email=Column(String(50),unique=True,nullable=False)
    phone=Column(String(50),nullable=False)
    address=Column(String(100))
    role=Column(String(50),default="student")
    dateofjoin=Column(Date,default=date.today)
    status=Column(Integer)
    created_by=Column(String(50),default="student")
    created_at=Column(DateTime,default=datetime.now)
    updated_by=Column(String(50))
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    enrollments=relationship('Students_courses',back_populates='student')
    marks=relationship('Marks',back_populates='student')
    course_allocations=relationship('Course_allocation',back_populates='staff')



class Courses(Base):
    __tablename__="courses"
    id=Column(Integer,primary_key=True,autoincrement=True)
    course_name=Column(String(50),unique=True,nullable=False)
    semester=Column(Integer,nullable=False)
    status=Column(Integer)
    created_by=Column(String(50),default="Admin")
    created_at=Column(DateTime,default=datetime.now)
    updated_by=Column(String(50),default="Admin")
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    enrollments=relationship('Students_courses',back_populates='course')
    

class Course_allocation(Base):
    __tablename__="course_allocation"
    id=Column(Integer,primary_key=True,autoincrement=True)
    course_id=Column(Integer,ForeignKey(Courses.id))
    staff_id=Column(Integer,ForeignKey(People.id))
    status=Column(Integer)
    created_by=Column(String(50),default="Admin")
    created_at=Column(DateTime,default=datetime.now)
    updated_by=Column(String(50))
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    staff=relationship('People',back_populates='course_allocations')
    
    
    
    


class Marks(Base):
    __tablename__="marks"
    id=Column(Integer,primary_key=True,autoincrement=True)
    student_id=Column(Integer,ForeignKey(People.id))
    course_id=Column(Integer,ForeignKey(Courses.id))
    marks=Column(Integer,nullable=False)
    status=Column(Integer)
    created_by=Column(String(50),default="Admin")
    created_at=Column(DateTime,default=datetime.now)
    updated_by=Column(String(50))
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    student=relationship('People',back_populates='marks')
    

#Association table:
class Students_courses(Base):
    __tablename__="students_courses"
    id=Column(Integer,autoincrement=True,primary_key=True)
    student_id=Column(Integer,ForeignKey(People.id))
    course_id=Column(Integer,ForeignKey(Courses.id))
    student=relationship('People',back_populates='enrollments')
    course=relationship('Courses',back_populates='enrollments')
    status=Column(Integer)
    created_by=Column(String(50),default="Admin")
    created_at=Column(DateTime,default=datetime.now)
    updated_by=Column(String(50))
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)


Base.metadata.create_all(engine)

    







