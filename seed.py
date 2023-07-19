from datetime import datetime
from datetime import timedelta
from random import randint
from random import sample
from random import random

start = datetime.now()
end = start + timedelta(days=60)

result = []

while start < end:
    if random() > 0.5:
        result.append(start.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        result.append(start.strftime("asdasd"))

    high_rand = randint(24, 72)
    low_rand = randint(5, 18)
    value = randint(low_rand, high_rand)
    step = timedelta(hours=value)
    start += step

res = sample(result, len(result))

print(res)

import os
from dotenv import load_dotenv
import sqlalchemy
import pandas as pd

load_dotenv()
DATABASE_NAME = os.getenv("DATABASE_NAME", "database.db")


def seed_db():
    """Function that seeds a sqlite db with the generated data"""
    # Get the current directory path
    current_dir = os.getcwd()

    # Replace 'DATABASE_NAME' with the actual name of your database file
    database_file = os.path.join(current_dir, DATABASE_NAME)

    # Create the database
    engine = sqlalchemy.create_engine(f"sqlite:///{database_file}")

    try:
        login_df = pd.DataFrame({"login_time": res})
        # create table
        login_df.to_sql("user_login", engine, index=False, if_exists="replace")
        print(login_df)
    except:
        print("Data already exists in the database")


seed_db()
