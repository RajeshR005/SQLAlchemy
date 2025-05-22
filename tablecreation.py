from models import Base,engine,Employee,Staffs,Student

Base.metadata.create_all(engine,tables=[Staffs.__table__])