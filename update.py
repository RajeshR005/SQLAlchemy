from sqlalchemy.orm import sessionmaker
from models import Student,engine

Session=sessionmaker(bind=engine)
session=Session()

users=session.query(Student).filter(Student.id==1).one_or_none()
print(users.name)
users.name="Prince Rajesh"
print(users.name)
session.commit()

