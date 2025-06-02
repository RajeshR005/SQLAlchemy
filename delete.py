from sqlalchemy.orm import sessionmaker
from models import Student,engine

Session=sessionmaker(bind=engine)
session=Session()

users=session.query(Student).filter(Student.id==3).one_or_none()
print(users.name)
session.delete(users)
print(users.name)
session.commit()