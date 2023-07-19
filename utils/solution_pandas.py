import os
from dotenv import load_dotenv
import sqlalchemy
import pandas as pd
import logging

# Logger initialization
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.DEBUG)

# Recover env variables
load_dotenv()
DATABASE_NAME = os.getenv("DATABASE_NAME", "database.db")


def extract():
    """Extract data from sqlite db"""

    current_dir = os.getcwd()
    database_file = os.path.join(current_dir, DATABASE_NAME)

    # Create the database
    engine = sqlalchemy.create_engine(f"sqlite:///{database_file}")

    df = pd.read_sql("select * from user_login", engine)
    logging.info(f"Complete extract")
    return df


def filter_date(data: pd.DataFrame):
    """Filter to only accept date with format YYYY-MM-DD HH:MM:SS"""
    # Use pandas to_datetime to convert the 'login_time' column to datetime objects
    # Invalid dates will be converted to NaT
    data["login_time"] = pd.to_datetime(
        data["login_time"], format="%Y-%m-%d %H:%M:%S", errors="coerce"
    ).dt.normalize()
    # Remove NaT rows
    result = data[data["login_time"].notnull()].reset_index(drop=True)
    logging.info(
        f"Complete filter_date, date reduced from {len(data)} to {len(result)}"
    )
    return result


def sort_date(data: pd.DataFrame):
    """Sort date"""
    data = data.sort_values(by="login_time").reset_index(drop=True)
    logging.info(f"Complete sort_date")
    return data


def count_continuous_date(data: pd.DataFrame):
    """Count continuous date"""

    if data.empty:
        return pd.DataFrame()

    # Remove duplicate dates
    data = data.drop_duplicates().reset_index(drop=True)

    # Calculate the difference between each row
    data["diff"] = data["login_time"].diff().dt.days

    # Create a boolean mask for the start of consecutive logins, which is the row where diff is > 1
    start_mask = data["diff"] > 1.0

    # Assign consecutive login period IDs to each row
    data["period_id"] = start_mask.cumsum()

    # Use agg
    result = data.groupby("period_id").agg(
        START=("login_time", "first"),
        END=("login_time", "last"),
        LENGTH=("login_time", "size"),
    )

    result = result.sort_values(by="LENGTH", ascending=False)
    result.reset_index(drop=True, inplace=True)
    logging.info(f"Complete count_continuous_date")
    return result
