from sqlalchemy import create_engine,Integer,String,Column,ForeignKey
from sqlalchemy.orm import declarative_base,relationship,sessionmaker,joinedload,subqueryload
db_url="mysql+pymysql://root:2741@localhost:3307/manytomany"

engine=create_engine(db_url)
Base=declarative_base()

Session=sessionmaker(bind=engine)
session=Session()


#Association Table:
class Stu_course(Base):
    __tablename__="stu_course"
    id=Column(Integer,primary_key=True,autoincrement=True)
    stu_id=Column(Integer,ForeignKey('students.id'))
    course_id=Column(Integer,ForeignKey('courses.id'))
    student=relationship("Students",back_populates="student_course", lazy="joined")
    course=relationship("Courses",back_populates="student_course", lazy= "joined")
    


class Students(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50))
    dept=Column(String(50))
    student_course=relationship("Stu_course",back_populates="student", lazy="joined")


class Courses(Base):
    __tablename__="courses"
    id=Column(Integer,primary_key=True,autoincrement=True)
    subj=Column(String(50))
    staff=Column(String(50))
    student_course=relationship("Stu_course",back_populates="course", lazy = "joined")

# lazy = Default
users=session.query(Stu_course).all()
for i in users:
    
    print(f"Name: {i.student.name} Course: {i.course.subj}")

#lazy = Default  
users=session.query(Students).all()
for i in users:
    print(i.name)
    for j in i.student_course:
        print(f"Course: {j.course.subj}")

#lazy = Joined faster than previous two select 
users=session.query(Students).options(
    joinedload(Students.student_course).joinedload(Stu_course.course)
).all()

for i in users:
    print(i.name)
    for j in i.student_course:
        print(f"Course: {j.course.subj}")


# subquery 
users = session.query(Students).options(
    subqueryload(Students.student_course).subqueryload(Stu_course.course)
).all()

for i in users:
    print(i.name)
    for j in i.student_course:
        print(f"Course: {j.course.subj}")





   
