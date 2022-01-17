from sqlalchemy import Column, Integer, String, DateTime, Table

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()
f = open('database.json')
# returns JSON object as
# a dictionary
data = json.load(f)
engine = create_engine(data['database'])

class Bestfriend(Base): 

    __tablename__ = "bestfriend",
   
    id=Column(Integer, primary_key=True)
    username=Column(String(250))
    interaction_type=Column(String(250))
    date=Column(DateTime)

Base.metadata.create_all(engine)
