from sqlalchemy import Column, Integer, String, DateTime, Table

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///C:\\sqlite3\\flatfriend.db')


class Bestfriend(Base): 

    __tablename__ = "bestfriend",
   
    id=Column(Integer, primary_key=True)
    username=Column(String(250))
    interaction_type=Column(String(250))
    date=Column(DateTime)

Base.metadata.create_all(engine)
# base = declarative_base()
 
# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)