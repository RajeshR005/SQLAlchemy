from sqlalchemy.orm import sessionmaker
from models import engine,Staffs
from sqlalchemy import func

Session=sessionmaker(bind=engine)
session=Session()

#this is used to group by name and age with count of the same grouping 
users=session.query(Staffs.age,Staffs.name,func.count(Staffs.id)).group_by(Staffs.age,Staffs.name).all()
for age,name,count in users:
    print(f"Name: {name} Age: {age} Count: {count}")

#this is used to group by name and returns with the name along with count 
users = session.query(Staffs.name,func.count(Staffs.id)).group_by(Staffs.name).all()

for name,count in users:
    print(f"Name: {name} Count: {count}")   

#Chaining
users = session.query(Staffs.age,Staffs.name,func.count(Staffs.id)).filter(Staffs.age>=25,Staffs.age<=45).group_by(Staffs.name,Staffs.age).order_by(Staffs.name).all()
for age,name,count in users:
    print(f"Name: {name} Age: {age} Count: {count}")



