from sqlalchemy import DateTime, create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from models import Base, Bestfriend
import datetime
import pandas as pd
import json

def database_connect():
    # Opening JSON file
    f = open('database.json')
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    engine = create_engine(data['database'])
    DBSession = sessionmaker(bind=engine)
    print(engine.table_names())
    session = DBSession()
    
    meta = MetaData()

    besties = Table(
    "('bestfriend',)", meta, 
    Column('id', Integer, primary_key=True),
        Column('username', String(250)),
        Column('interaction_type', String(250)),
        Column('date', DateTime)
)

    conn = engine.connect()

    return session, conn, besties


def add_interaction(username, interaction_type):
    print(username, interaction_type)

    session, conn, besties = database_connect()
    new_bestie = Bestfriend(username=username, interaction_type=interaction_type, date= datetime.datetime.now())
    session.add(new_bestie)
    session.commit()

def analysis():
    session, conn, besties = database_connect()
     
    b = besties.select()
    result = conn.execute(b)
    df = pd.DataFrame([(d.id, d.username, d.interaction_type, d.date) for d in result], 
                  columns=['id', 'username', 'interaction_type', 'date'])

    print(df)
    return df




