import pandas as pd
from utils.solution_pandas import extract, filter_date, sort_date, count_continuous_date

if __name__ == "__main__":
    raw_data = [
        "asdasd",
        "2023-09-12 01:07:23",
        "asdasd",
        "asdasd",
        "2023-08-27 23:07:23",
        "asdasd",
        "asdasd",
        "asdasd",
        "2023-08-13 15:07:23",
        "asdasd",
        "asdasd",
        "2023-09-09 07:07:23",
        "2023-09-16 09:07:23",
        "asdasd",
        "asdasd",
        "2023-08-15 13:07:23",
        "2023-08-19 03:07:23",
        "asdasd",
        "2023-08-14 13:07:23",
        "2023-08-08 15:07:23",
        "2023-09-14 09:07:23",
        "asdasd",
        "asdasd",
        "2023-09-10 21:07:23",
        "2023-08-31 17:07:23",
        "asdasd",
        "2023-08-24 11:07:23",
        "asdasd",
        "2023-08-18 04:07:23",
        "2023-08-12 22:07:23",
        "2023-08-23 15:07:23",
        "2023-07-25 18:07:23",
        "2023-09-01 02:07:23",
        "2023-09-08 00:07:23",
        "2023-07-23 09:07:23",
        "asdasd",
        "asdasd",
        "2023-08-25 08:07:23",
        "asdasd",
        "2023-08-28 16:07:23",
        "2023-07-25 01:07:23",
        "2023-09-05 00:07:23",
        "2023-09-03 05:07:23",
        "2023-08-01 16:07:23",
        "2023-08-26 03:07:23",
        "2023-08-04 12:07:23",
        "2023-07-27 00:07:23",
        "asdasd",
    ]

    # If you want to input raw data manualy, uncomment the following line and comment out df_raw = extract(). Note it's the same data from database.db
    # df_raw = pd.DataFrame({"login_time": raw_data})

    # To pull raw data from database
    df_raw = extract()

    df = filter_date(df_raw)
    df = sort_date(df)
    df = count_continuous_date(df)
    print(f"Raw Data\n {df_raw}")
    print(f"Cleaned Data\n {df}")
