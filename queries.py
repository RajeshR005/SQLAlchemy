import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_,and_,not_
from models import Staffs,engine

Session=sessionmaker(bind=engine)

session=Session()
names=['prince','Aang','Azula','Katara','Mai','Sokka','Korra']
age=[21,33,24,29,35,19,20,27]
dept=['AI & ML','CSE','ECE','EEE','MCA']

for i in range(10):
    stf=Staffs(name=random.choice(names),age=random.choice(age),dept=random.choice(dept))
    session.add(stf)
    session.commit()

staffs=session.query(Staffs).order_by(Staffs.age).all()

for i in staffs:
    print(f" Name: {i.name}, Dept: {i.dept}")

#using the filter to get the data we can use logical and conditions here
f_name=session.query(Staffs).filter(Staffs.age>=24).all()
for i in f_name:
    print(i.name)

#using the filter_by to get the data for the specific keyword arguments and check conditions only
f_name=session.query(Staffs).filter_by(name='Prince').all()
for i in f_name:
    print(i.name)

# using the or operator to check any one condition is true
f_name=session.query(Staffs).filter(or_(Staffs.name=='Prince',Staffs.age==21)).all()
for i in f_name:
    print(f"Name: {i.name} Age: {i.age}")

#using the and operator to check both condition is true

f_name=session.query(Staffs).filter(and_(Staffs.name=='Azula',Staffs.age==21)).all()
f_name_1=session.query(Staffs).filter(and_(Staffs.name=='Azula',Staffs.age==21))
print(f"The total number of staffs: {(f_name_1)}")
for i in f_name_1:
    
    print(f"Name: {i.name} Age: {i.age}")

# Using the not operator to not get the data from the row

f_name=session.query(Staffs).filter(not_(Staffs.name=='Azula')).all()
for i in  f_name:
    print(f"{i.name}")

#Combinig the AND OR NOT in single query
f_name=session.query(Staffs).filter(or_(not_(Staffs.name=='Mai'),and_(Staffs.age==24,Staffs.dept=='CSE'))).all()
for i in f_name:
    print(f"{i.name} had a age of {i.age} in the dept of {i.dept}")