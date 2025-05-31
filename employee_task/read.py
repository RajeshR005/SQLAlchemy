from sqlalchemy import func,case
from datetime import datetime,date,time
from sqlalchemy.orm import sessionmaker
from models import Base,engine,Employee,Daily_attendance,Door_access_logs

Session=sessionmaker(bind=engine)
session=Session()

users=session.query(Employee,func.sum(case((Daily_attendance.attendance_status==1,1),else_=0))).join(Daily_attendance).join(Door_access_logs).group_by(Employee.employee_id).all()
for i,count in users:
    for j in i.attendance:
        if j.attendance_status==1:
            print(f"Name: {i.name} Departement: {i.department} Status: {j.status} Count: {count}")


users=session.query(Employee,func.sum(case((Daily_attendance.attendance_status==1,1),else_=0))).join(Daily_attendance).join(Door_access_logs).group_by(Employee.employee_id).all()
for i,count in users:
    print(f"Name: {i.name} Departement: {i.department} Status: present Count: {count}")

