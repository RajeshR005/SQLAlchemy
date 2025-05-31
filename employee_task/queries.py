from sqlalchemy.orm import sessionmaker
from models import engine,Daily_attendance,Employee,Door_access_logs
from sqlalchemy import func,case,Date,DateTime,and_,cast
from datetime import date

Session=sessionmaker(bind=engine)
session=Session()

users=session.query(Daily_attendance).filter(Daily_attendance.employee_id).all()

for i in users:
    print(f"Employee_id: {i.employee_id} Check in time: {i.Check_in_time} Check out time: {i.Check_out_time}")

users=session.query(Daily_attendance.employee_id,func.count(Daily_attendance.employee_id)).filter(Daily_attendance.attendance_status==1).group_by(Daily_attendance.employee_id).all()

for employee_id,present in users:
    print(f"Employee ID: {employee_id} Count of present: {present} ")

users=session.query(Daily_attendance.employee_id,func.count(Daily_attendance.attendance_status==1)).group_by(Daily_attendance.employee_id).all()

for employee_id,present in users:
    print(f"Employee ID: {employee_id} Count of present: {present} ")

users=session.query(Employee).filter(Employee.door_location,Employee.access_time).all()

for i in users:
    print(f"Employee ID {i.employee_id} Access_time: {i.access_time} Access_location: {i.door_location} ")



users = session.query(Daily_attendance.employee_id,func.sum(case((Daily_attendance.attendance_status == 1, 1), else_=0)),func.sum(case((Daily_attendance.attendance_status == 3, 1), else_=0)),func.sum(case((Daily_attendance.attendance_status==2, 1),else_=0))).group_by(Daily_attendance.employee_id).all()

for employee_id, present, absent, holidays in users:
    print(f"Employee ID: {employee_id}  Present: {present}  Absent: {absent} Holidays: {holidays}")



users = session.query(Door_access_logs,Daily_attendance).join(Employee, Door_access_logs.employee_id == Employee.employee_id).join(Daily_attendance, and_(Daily_attendance.employee_id == Employee.employee_id,Daily_attendance.attendance_date == func.date(Door_access_logs.access_time))).all()

i=1
for log,attend in users:
    print(i)
    i+=1
    print(f"Employee ID: {log.employee.employee_id}, Name: {log.employee.name}, Department: {log.employee.department} "
          f"Access Time: {log.access_time}, Access Location: {log.door_location} Check_in_time: {attend.Check_in_time} Check_out_time: {attend.Check_out_time}")

users=session.query(Employee.employee_id,Employee.name,Employee.department,Door_access_logs.access_time,Door_access_logs.door_location,Daily_attendance.Check_in_time,Daily_attendance.Check_out_time).join(Daily_attendance).join(Door_access_logs).filter(cast(Door_access_logs.access_time, Date) == Daily_attendance.attendance_date).all()
for i in users:
    print(f"Employee ID: {i.employee_id}, Name: {i.name}, Department: {i.department} "
          f"Access Time: {i.access_time}, Access Location: {i.door_location} Check_in_time: {i.Check_in_time} Check_out_time: {i.Check_out_time}")
    

users = session.query(
    Employee.employee_id,
    Employee.name,
    Employee.department,
    Door_access_logs.access_time,
    Door_access_logs.door_location,
    Daily_attendance.Check_in_time,
    Daily_attendance.Check_out_time
).join(Daily_attendance).join(Door_access_logs)\
    .filter(func.date(Door_access_logs.access_time) == Daily_attendance.attendance_date).all()
for i in users:
    print(f"Employee ID: {i.employee_id}, Name: {i.name}, Department: {i.department} "
          f"Access Time: {i.access_time}, Access Location: {i.door_location} Check_in_time: {i.Check_in_time} Check_out_time: {i.Check_out_time}")

users=session.query(Employee).join(Daily_attendance).join(Door_access_logs).all()
for i in users:
    print(f"Name: {i.name}  ")