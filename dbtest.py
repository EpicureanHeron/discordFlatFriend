from sqlalchemy import DateTime, create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from models import Base, Bestfriend
import datetime

time = datetime.datetime.now()
user = 'EpicureanHeron'
interaction = 'good bot'
#import models


# engine = create_engine("sqlite:///flatfriend.db")
engine = create_engine('sqlite:///C:\\sqlite3\\flatfriend.db')
DBSession = sessionmaker(bind=engine)
print(engine.table_names())

session = DBSession()


# new_bestie = Bestfriend(username='EpicureanHeron', interaction_type='good bot', date=time)
# session.add(new_bestie)
# session.commit()



meta = MetaData()

besties = Table(
  "('bestfriend',)", meta, 
   Column('id', Integer, primary_key=True),
    Column('username', String(250)),
    Column('interaction_type', String(250)),
    Column('date', DateTime)
)

# engine = create_engine('sqlite:///C:\\sqlite3\\flatfriend.db')


conn = engine.connect()
 
b = besties.select()

result = conn.execute(b)

for row in result:
   print (row)