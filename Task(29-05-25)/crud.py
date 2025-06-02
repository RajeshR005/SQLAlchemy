from sqlalchemy.orm import sessionmaker
from models import Base,engine,People
from datetime import date, datetime
from sqlalchemy import Date,func

Session=sessionmaker(bind=engine)
session=Session()

def insert():
    name1=(input("Enter the Student name: ")).capitalize()
    gender1=input("Gender (M/F): ").capitalize()
    department1=input("Department Name: ").capitalize()
    email1=input("Email: ")
    phone1=input("Phone Number: ")
    address1=input("Address: ").capitalize()
    dateofjoin_in=input("Enter your Date of Join: (YYYY-MM-DD): ")
    dateofjoin1 = datetime.strptime(dateofjoin_in, "%Y-%m-%d").date()
    users=session.query(People).filter(People.email==email1).first()
    if not users:
        users=People(name=name1,gender=gender1,department=department1,email=email1,phone=phone1,address=address1,dateofjoin=dateofjoin1,status=1)
        session.add(users)
        session.commit()
        print(f"{name1} Data Inserted Sucessfully")
        print(f"{name1} | {gender1} | {department1} | {email1} | {phone1} | {address1} | {dateofjoin1}")
        
    else:
        print(f"{name1} Data already Exists in Database\n If you want to Update the Data Choose the Update Menu")
    
    
    

def view():
    print("Your are Now in Display Dashboard")
    user_choice=int(input("\nAll users = 1\nSpecific user = 2\nEnter your option: "))
    if user_choice==1:
        users=session.query(People).all()
        for i in users:
            print(f" Name: {i.name}\n Gender: {i.gender}\n Department: {i.department}\n Email: {i.email}\n Phone: {i.phone}\n Address: {i.address}\n Role: {i.role}\n Date of Join: {i.dateofjoin}")
    elif user_choice==2:
        specific_user=(input("Enter the Name of the User: ")).lower()
        users=session.query(People).filter(People.name.ilike(specific_user)).first()
        i=users
        if users:
                print(f" Name: {i.name}\n Gender: {i.gender}\n Department: {i.department}\n Email: {i.email}\n Phone: {i.phone}\n Address: {i.address}\n Role: {i.role}\n Date of Join: {i.dateofjoin}")
        else:
            print("The Student Name Not Exists")
    else:
        print("Invalid Choice")

def update():
    print("Now Your are in Update Dashboard")
    update_user=input("Enter the Student Name: ").lower()
    users=session.query(People).filter(People.name.ilike(update_user)).first()
    if users:
        print("What are the Fields you want to update")
        field_choice=int(input("Select your fields: \n Email = 1 \n Phone number = 2\n Address =3\n Whether you want to update all fields = 4\nEnter Your Choice: "))
        if field_choice==1:
            users.email=input("New Email: ")
            print("Email Updated Successfully")
        elif field_choice==2:
             users.phone=input("New Phone Number: ")
             print("Phone Number Updated Successfully")
        elif field_choice==3:
             users.address=input("New Address: ")
             print("Address Updated Successfully")
        elif field_choice==4:
             users.email=input("New Email: ")
             users.phone=input("New Phone Number: ")
             users.address=input("New Address: ")
             print("Updated Successfully")
        else:
             print("Invalid Choice")
        session.commit()

    else:
        print(f" Student Name: {update_user.capitalize()} Doesn't Exist In the Database")

def delete():
        print("Your are Now in the Delete Dashboard")
        del_id=(input("Enter the name of the user: ")).lower()
        users=session.query(People).filter(func.lower(People.name)==del_id).first()
        if users:
            session.delete(users)
            session.commit()
            print(f"{del_id} Data Deleted Successfully")
        else:
             print(f"{del_id} Not Exists in the Database")

def view_all():
     users=session.query(People).all()
     data=[]
     for i in users:
          
          new_data=i.name,i.gender,i.department,i.email,i.address,i.dateofjoin
          data.append(new_data)
     print(data)
