from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float
Base =declarative_base()

class Student(Base):
    __tablename__= 'students'
    id=Column (Integer,primary_key=True)
    name=Column (String(50))
    klass=Column(Integer)

engine= create_engine("sqlite:///school.sqlite")
Base.metadata.create_all(engine)