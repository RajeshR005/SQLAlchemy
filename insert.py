from sqlalchemy.orm import sessionmaker
from models import Student,engine

Session=sessionmaker(bind=engine)
session=Session()
user=Student(name = "Prince", age=23)
user_1=Student(name="RJ",age=20)
user_2=Student(name="Katara",age=21)
session.add_all([user_1,user_2])
session.commit()





    



