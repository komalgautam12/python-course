from email.policy import default
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float,DateTime
from datetime import datatime, datetime
Base =declarative_base()

class Student(Base):
    __tablename__= 'students'
    id=Column (Integer,primary_key=True)
    name=Column (String(50))
    klass=Column(Integer)

class Product(Base):
    __tablename__='products'
    id=Column (Integer,primary_key=True)
    title=Column(String,unique=True)
    mrp=Column(Float,default=0.0)
    quantity=Column(Integer,default=0)
    brand=-Column(String(50))
    detail=Column (String ,default='')
    mfg=Column(datetime,default=datetime.now)
    added_on=Column(datetime,default=datetime.now)

engine= create_engine("sqlite:///school.sqlite")
Base.metadata.create_all(engine)


