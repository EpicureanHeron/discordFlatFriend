from sqlalchemy import DateTime, create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models import Base, Bestfriend
import datetime
import pandas as pd

time = datetime.datetime.now()



# engine = create_engine("sqlite:///flatfriend.db")
engine = create_engine('sqlite:///C:\\sqlite3\\flatfriend.db')
DBSession = sessionmaker(bind=engine)
print(engine.table_names())

session = DBSession()


# new_bestie = Bestfriend(username='TheGreatBorotan', interaction_type='at replys', date=time)
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

conn = engine.connect()
 
b = besties.select()
result = conn.execute(b)
# c = besties.count()

# result = conn.execute(c)

# print (session.query(besties).count())
# print(conn.execute(b).keys())

df = pd.DataFrame([(d.id, d.username, d.interaction_type, d.date) for d in result], 
                  columns=['id', 'username', 'interaction_type', 'date'])

df2 = df.where(df['date'] < datetime.datetime.today())

print(df2)
df2 = df2.groupby(['username']).count()


print(df)

for row in result:
   print (row)

results = session.query(besties).filter(besties.c.username=='EpicureanHeron').count()

print(results)

# for row in results:
#    print (row)
# results = session.query(besties).count(besties.c.username)
# https://stackoverflow.com/questions/46978199/select-the-count-and-value-of-a-sqlalchemy-column-using-having

# q = session.query(
#     Bestfriend.func.count(besties.c.username),
#     besties.c.username
# ).group_by(
#     besties.c.username
# ).having(
#     Bestfriend.func.count(besties.c.username) > 1
# )
# print(q)
