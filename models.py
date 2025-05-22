
from sqlalchemy import create_engine,Column,Integer,String,inspect
from sqlalchemy.orm import declarative_base

db_url="mysql+pymysql://root:2741@localhost:3307/hello_world"
engine=create_engine(db_url)
Base = declarative_base()

class Student(Base):
        __tablename__="student"
        id =Column(Integer, primary_key=True)
        name = Column(String(50))
        age = Column(Integer)

class Employee(Base):
        __tablename__="employee"
        id =Column(Integer, primary_key=True)
        name = Column(String(50))
        age = Column(Integer)
        dept = Column(String(50))
class Staffs(Base):
        __tablename__="staffs"
        id = Column(Integer,primary_key=True)
        name = Column(String(50))
        age = Column(Integer)
        dept = Column(String(50))
        subj_id= Column(String(50))


        

# inspector=inspect(engine)
# if "employee" in inspector.get_table_names():
#         print("The table is exists")
# else:
#         base.metadata.create_all(engine)
#         print('The table created sucessfully')
