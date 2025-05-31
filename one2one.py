from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import declarative_base,relationship,sessionmaker


db_url="mysql+pymysql://root:2741@localhost:3307/Onetoone"
engine=create_engine(db_url)
Base=declarative_base()

class User(Base):
    __tablename__="user"
    id=Column(Integer,autoincrement=True,primary_key=True)
    name=Column(String(50))
    dept=Column(String(50))
    user_det=relationship('User_details',back_populates='user',uselist=False)

class User_details(Base):
    __tablename__="user_details"
    id=Column(Integer,primary_key=True,autoincrement=True)
    stu_id=Column(Integer,ForeignKey('user.id'))
    address=Column(String(100))
    email=Column(String(50))
    user=relationship('User',back_populates='user_det')

Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

user_1=User(name="Prince",dept="MCA")
user_2=User(name="RJ",dept="MCA")
user_3=User(name="Azula",dept="MBA")
user_4=User(name="Mai",dept="BCA")
user_5=User(name="MJ",dept="BBA")

User_details_1=User_details(address="CBE",email="prince@gmail.com")
User_details_2=User_details(address="KVP",email="rj@gmail.com")
User_details_3=User_details(address="HY",email="azula@gmail.com")
User_details_4=User_details(address="KL",email="mai@gmail.com")
User_details_5=User_details(address="TVL",email="mj@gmail.com")

session.add_all([user_1,user_2,user_3,user_4,user_5,User_details_1,User_details_2,User_details_3,User_details_4,User_details_5])

session.commit()
User_details_1=session.query(User_details).filter(User_details.id==1).first()
User_details_2=session.query(User_details).filter(User_details.id==2).first()
User_details_3=session.query(User_details).filter(User_details.id==3).first()
User_details_4=session.query(User_details).filter(User_details.id==4).first()
User_details_5=session.query(User_details).filter(User_details.id==5).first()

user_1=session.query(User).filter(User.id==1).first()
user_2=session.query(User).filter(User.id==2).first()
user_3=session.query(User).filter(User.id==3).first()
user_4=session.query(User).filter(User.id==4).first()
user_5=session.query(User).filter(User.id==5).first()

User_details_1.stu_id=user_1.id
User_details_2.stu_id=user_2.id
User_details_3.stu_id=user_3.id
User_details_4.stu_id=user_4.id
User_details_5.stu_id=user_5.id

session.commit()

users=session.query(User).all()
for i in users:
    print(f"User ID: {i.id} Name: {i.name} dept: {i.dept} Email: {i.user_det.email} Address: {i.user_det.address}  ")



    