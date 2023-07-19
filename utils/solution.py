import os
from dotenv import load_dotenv
import sqlalchemy
import pandas as pd
from datetime import datetime
import logging
from typing import List

# Logger initialization
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.DEBUG)

# Recover env variables
load_dotenv()
DATABASE_NAME = os.getenv("DATABASE_NAME")


def extract() -> List[str]:
    """Extract data from sqlite db"""

    current_dir = os.getcwd()
    database_file = os.path.join(current_dir, DATABASE_NAME)

    # Connect to the database
    engine = sqlalchemy.create_engine(f"sqlite:///{database_file}")

    df = pd.read_sql("select * from user_login", engine)
    logging.info(f"Complete extract")
    return df["login_time"].tolist()


def filter_date(data: List[str]) -> List[datetime]:
    """Filter to only accept date with format YYYY-MM-DD HH:MM:SS"""
    result = []
    for date_string in data:
        try:
            result.append(datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S").date())
        except:
            pass
    logging.info(
        f"Complete filter_date, date reduced from {len(data)} to {len(result)}"
    )
    return result


def sort_date(data: List[datetime]) -> List[datetime]:
    """Sort date"""
    sorted_data = sorted(data)

    logging.info(f"Complete sort_date")
    return sorted_data


def count_continuous_date(data: List[datetime]):
    """Count continuous date"""
    consecutive_dates = []
    start_date = 0
    count = 1
    # condition
    # 1. if (data[i] - data[i - 1]).days == 1, this means two dates are consecutive
    # 2. if (data[i] - data[i - 1]).days > 1, this means two dates are not consecutive
    # 3. if (data[i] - data[i - 1]).days <1 , this means two dates are the same date
    for i in range(1, len(data)):
        if (data[i] - data[i - 1]).days == 1:
            count += 1
            pass

        elif (data[i] - data[i - 1]).days > 1:
            consecutive_dates.append([data[start_date], data[i - 1], count])
            start_date = i
            count = 1

        elif (data[i] - data[i - 1]).days < 1:
            pass

        # Last date has two conditions
        if i == len(data) - 1:
            if start_date == i:
                consecutive_dates.append([data[i], data[i], count])
            else:
                consecutive_dates.append([data[start_date], data[i], count])

    consecutive_dates = sorted(consecutive_dates, key=lambda x: x[2], reverse=True)
    logging.info(f"Complete count_continuous_date")
    return consecutive_dates
