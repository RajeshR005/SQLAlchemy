from sqlalchemy import create_engine,Column,Integer,String,inspect,Date,Time,ForeignKey,DateTime
from sqlalchemy.orm import declarative_base,relationship

db_url="mysql+pymysql://root:2741@localhost:3307/employee"
engine=create_engine(db_url)
Base = declarative_base()

class Employee(Base):
    __tablename__="employees"
    employee_id=Column(Integer,autoincrement=True,primary_key=True)
    name=Column(String)
    department=Column(String)
    rfid=Column(String)
    status=Column(Integer)
    created_at=Column(DateTime)
    attendance=relationship("Daily_attendance", back_populates="employee")
    door_logs=relationship("Door_access_logs", back_populates="employee")

class Daily_attendance(Base):
    __tablename__="daily_attendance"
    attendance_id=Column(Integer,autoincrement=True,primary_key=True)
    employee_id=Column(Integer,ForeignKey(Employee.employee_id))
    attendance_date=Column(Date)
    Check_in_time=Column(Time)
    Check_out_time=Column(Time)
    status=Column(String)
    attendance_status=Column(Integer)
    employee=relationship("Employee",back_populates="attendance" )
    
class Door_access_logs(Base):
    __tablename__="door_access_logs"
    log_id=Column(Integer,autoincrement=True,primary_key=True)
    employee_id=Column(Integer,ForeignKey(Employee.employee_id))
    access_time=Column(DateTime)
    door_location=Column(String)
    access_granted=Column(Integer)
    employee=relationship("Employee", back_populates="door_logs")
    



