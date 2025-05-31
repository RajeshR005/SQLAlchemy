from sqlalchemy import create_engine,Integer,String,Column,ForeignKey
from sqlalchemy.orm import declarative_base,relationship,sessionmaker
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

stu_1=Students(name="Prince",dept="MCA")
stu_2=Students(name="RJ",dept="CSE")
stu_3=Students(name="MJ",dept="BCA")

c1=Courses(subj="Python",staff="Dr. Nandhini")
c2=Courses(subj="Networking",staff="Vimala Mam")
c3=Courses(subj="AI & ML",staff="Dr. Gopikannan")

session.add_all([stu_1,stu_2,stu_3,c1,c2,c3])
session.commit()

stu_1=session.query(Students).filter(Students.name=="Prince").first()
stu_2=session.query(Students).filter(Students.name=="RJ").first()
stu_3=session.query(Students).filter(Students.name=="MJ").first()


c1=session.query(Courses).filter(Courses.subj=="Python").first()
c2=session.query(Courses).filter(Courses.subj=="Networking").first()
c3=session.query(Courses).filter(Courses.subj=="AI & ML").first()

St_co_1=Stu_course(student=stu_1,course=c1)
St_co_2=Stu_course(student=stu_1,course=c2)
St_co_3=Stu_course(student=stu_1,course=c3)
St_co_4=Stu_course(student=stu_2,course=c2)
St_co_5=Stu_course(student=stu_2,course=c3)
St_co_6=Stu_course(student=stu_1,course=c3)

session.add_all([St_co_1,St_co_2,St_co_3,St_co_4,St_co_5,St_co_6])
session.commit()

users=session.query(Stu_course).all()
for i in users:
    
    print(f"Name: {i.student.name} Course: {i.course.subj}")
    
users=session.query(Students).all()
for i in users:
    print(i.name)
    for j in i.student_course:
        print(f"Course: {j.course.subj}")





   
