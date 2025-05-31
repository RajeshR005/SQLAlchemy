from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import declarative_base,Mapped,mapped_column,relationship,sessionmaker
db_url="mysql+pymysql://root:2741@localhost:3307/selfrelationship"
engine=create_engine(db_url)
Base=declarative_base()


class Selfreal(Base):
    __tablename__="selfreal"
    __allow_unmapped__=True

    id=Column(Integer,autoincrement=True,primary_key=True)
    name=Column(String(50))
    task_by=Column(Integer,ForeignKey('selfreal.id'))
    follow=relationship("Selfreal", remote_side=[id],uselist=True)



Session=sessionmaker(bind=engine)
session=Session()

users=Selfreal(name="Prince")
users_1=Selfreal(name="RJ")
users_2=Selfreal(name="Katara")
users_3=Selfreal(name="Aang")
users_4=Selfreal(name="Mai")

session.add_all([users,users_1,users_2,users_3,users_4])

session.commit()
users     = session.query(Selfreal).filter_by(name="Prince").first()
users_1   = session.query(Selfreal).filter_by(name="RJ").first()
users_2   = session.query(Selfreal).filter_by(name="Katara").first()
users_3   = session.query(Selfreal).filter_by(name="Aang").first()
users_4   = session.query(Selfreal).filter_by(name="Mai").first()

users.task_by=users_3.id
users_1.task_by=users_4.id
users_2.task_by=users_1.id
users_3.task_by=users.id
users_4.task_by=users_2.id

session.commit()

class Selfreal_1(Base):
    __tablename__="selfreal_1"
    __allow_unmapped__=True

    id=Column(Integer,primary_key=True)
    name=Column(String(50))
    task_by=Column(Integer,ForeignKey('selfreal_1.id'))
    follow=relationship("Selfreal_1", remote_side=[id],uselist=True)
Base.metadata.create_all(engine)

users=Selfreal_1(id=1,name="Ten")
users_1=Selfreal_1(id=2,name="Hem")
users_2=Selfreal_1(id=3,name="RJ")
users_3=Selfreal_1(id=4,name="Ashok")
users_4=Selfreal_1(id=5,name="MJ")

session.add_all([users,users_1,users_2,users_3,users_4])

session.commit()

users.task_by=users_1.id
users_1.task_by=users_3.id
users_2.task_by=users_4.id
users_3.task_by=users.id
users_4.task_by=users_2.id

session.commit()

# #The below query is used to fetch the results of the self relationship
users=session.query(Selfreal_1).all()

for i in users:
    assigned_by=session.get(Selfreal_1,i.task_by)
    print(f"User id: {i.id} Name: {i.name} Assigned By: {assigned_by.name}")

users=session.query(Selfreal).all()
for i in users:
    print(f"Name: {i.name} assigned by: {i.task_by}")
   
        