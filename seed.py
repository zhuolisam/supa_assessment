from datetime import datetime
from datetime import timedelta
from random import randint
from random import sample
from random import random

start = datetime.now()
end = start+timedelta(days=60)

result = []

while start < end:
  if random() > 0.5:
    result.append(start.strftime('%Y-%m-%d %H:%M:%S'))
  else:
    result.append(start.strftime('asdasd'))

  high_rand = randint(24, 72)
  low_rand = randint(5,18)
  value = randint(low_rand, high_rand) 
  step = timedelta(hours=value)
  start += step

res = sample(result,len(result))

print(res)

import os
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy import Table, Column, String, MetaData
import sqlite3
import pandas as pd

load_dotenv()

DATABASE_LOCATION = os.getenv('DATABASE_LOCATION')

def seed_db():
    """
    Function that seeds a sqlite db with the generated data
    """
    # create database folder if not exists
    if not os.path.exists(DATABASE_LOCATION):
        os.makedirs(DATABASE_LOCATION)
    
    # get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # join current directory with database folder and database file
    database_file = os.path.join(current_dir, DATABASE_LOCATION, 'database.db')
       
    # Create the database
    engine = sqlalchemy.create_engine(f'sqlite:///{database_file}')

    # Create the connection
    conn = sqlite3.connect('myplayedtracks.sqlite')
    # Metadata object that will hold the table
    meta = MetaData(engine)

    if not engine.dialect.has_table(conn, 'user_login'):
        # Create the table
        user_login_table = Table(
            'user_login',
            meta,
            Column('login_time', String),
        )
    meta.create_all()

    try:
        login_df = pd.DataFrame({'login_time': res})
        login_df.to_sql('user_login', engine, index=False, if_exists='replace')
        print(login_df)
    except:
        print('Data already exists in the database')
    
    conn.close()

seed_db()