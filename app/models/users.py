from  sqlalchemy import Column, Integer, String
from app.database.bd import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String,index=True)
    age = Column(Integer)
    adress = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    