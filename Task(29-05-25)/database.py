from sqlalchemy import create_engine,text


db_url="mysql+pymysql://root:2741@localhost:3307"

engine=create_engine(db_url)

db_name="studentmanagement"

with engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
    print(f"Database Created Sucessfully {db_name}")

