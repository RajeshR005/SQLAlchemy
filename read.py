#There are multiple ways to query the data here we use one_or_none, .first, .one, .all

from sqlalchemy.orm import sessionmaker
from models import Student,engine

Session=sessionmaker(bind=engine)
session=Session()

users=session.query(Student).filter(Student.name=="Prince Zuko").one_or_none()
print(f"ID: {users.id} Name: {users.name} Age: {users.age}")
users=session.query(Student).filter(Student.name=="Katara").first()
print(f"ID: {users.id} Name: {users.name} Age: {users.age}")
users=session.query(Student).all()
for i in users:
    print(f"ID: {i.id} Name: {i.name} Age: {i.age}")


#Here we use the order by to get the data in ascending order and descending order

from sqlalchemy.orm import sessionmaker
from models import Student,engine

Session=sessionmaker(bind=engine)
session=Session()

users=session.query(Student).order_by(Student.name.desc()).all()
for i in users:
    print(i.name)

