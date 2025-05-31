from sqlalchemy import create_engine,Integer,String,Column,ForeignKey
from sqlalchemy.orm import declarative_base,relationship,sessionmaker,joinedload
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
        student=relationship("Students",back_populates="student_course")
        course=relationship("Courses",back_populates="student_course")
        


class Students(Base):
        __tablename__="students"
        id=Column(Integer,primary_key=True,autoincrement=True)
        name=Column(String(50))
        dept=Column(String(50))
        student_course=relationship("Stu_course",back_populates="student")


class Courses(Base):
        __tablename__="courses"
        id=Column(Integer,primary_key=True,autoincrement=True)
        subj=Column(String(50))
        staff=Column(String(50))
        student_course=relationship("Stu_course",back_populates="course")

Base.metadata.create_all(engine)

#Normal Join along with Relationships
users=session.query(Students).join(Stu_course).join(Courses).all()
for i in users:
    print(f"Student Name: {i.name}")
    for j in i.student_course:
        print(f"Courses {j.course.subj}")

#here it only works with the relationships
users=session.query(Students).all()
for i in users:
    print(f"Name: {i.name}")
    
    for j in i.student_course:
        print(f"Courses: {j.course.subj}")

#with Join
print("With join:")
users = session.query(Students).join(Stu_course).all()
for i in users:
    print(f"{i.name}")

#without Join
print("Without join:")
users_all = session.query(Students).all()
for i in users_all:
    print(f"{i.name}")

users=session.query(Students.name,Courses.subj).join(Stu_course,Stu_course.stu_id==Students.id).join(Courses,Courses.id==Stu_course.course_id).group_by(Students.name,Courses.subj).all()
for name,subj in users:
    print(f"{name} {subj}")
    
#Full Outer join
left=session.query(Students,Courses).outerjoin(Stu_course,Stu_course.stu_id==Students.id).outerjoin(Courses,Courses.id==Stu_course.course_id).filter(Courses.id == None)
right=session.query(Students,Courses).outerjoin(Stu_course,Stu_course.course_id==Courses.id).outerjoin(Students,Students.id==Stu_course.stu_id).filter(Students.id == None)
users=left.union(right)
for student1,course1 in users.all():
    print(student1.name if student1 else 'none')
    print(course1.subj if course1 else 'none')
    
    
    
    