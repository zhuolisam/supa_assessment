import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from utils.solution_pandas import filter_date, sort_date, count_continuous_date


@pytest.fixture
def sample_data_datetime():
    data = {
        "login_time": [
            "2023-08-25 08:00:00",
            "2023-08-24 10:00:00",
            "2023-09-01 15:00:00",
            "2023-08-23 11:00:00",
            "2023-08-24 12:00:00",
            "2023-08-31 14:00:00",
            "Invalid Date",
        ]
    }
    return pd.DataFrame(data)


def test_filter_date(sample_data_datetime):
    filtered_data = filter_date(sample_data_datetime)

    expected_data = pd.DataFrame(
        {
            "login_time": [
                pd.to_datetime("2023-08-25"),
                pd.to_datetime("2023-08-24"),
                pd.to_datetime("2023-09-01"),
                pd.to_datetime("2023-08-23"),
                pd.to_datetime("2023-08-24"),
                pd.to_datetime("2023-08-31"),
            ]
        }
    )

    assert_frame_equal(filtered_data, expected_data)


@pytest.fixture
def sample_data_date():
    data = {
        "login_time": [
            pd.to_datetime("2023-08-25"),
            pd.to_datetime("2023-08-24"),
            pd.to_datetime("2023-09-01"),
            pd.to_datetime("2023-08-23"),
            pd.to_datetime("2023-08-24"),
            pd.to_datetime("2023-08-31"),
        ]
    }
    return pd.DataFrame(data)


def test_sort_date(sample_data_date):
    sorted_data = sort_date(sample_data_date)

    expected_data = pd.DataFrame(
        {
            "login_time": [
                pd.to_datetime("2023-08-23"),
                pd.to_datetime("2023-08-24"),
                pd.to_datetime("2023-08-24"),
                pd.to_datetime("2023-08-25"),
                pd.to_datetime("2023-08-31"),
                pd.to_datetime("2023-09-01"),
            ]
        }
    )
    assert_frame_equal(sorted_data, expected_data)


@pytest.fixture
def sample_data_sorted_date():
    data = {
        "login_time": [
            pd.to_datetime("2023-08-23"),
            pd.to_datetime("2023-08-24"),
            pd.to_datetime("2023-08-24"),
            pd.to_datetime("2023-08-25"),
            pd.to_datetime("2023-08-31"),
            pd.to_datetime("2023-09-01"),
        ]
    }
    return pd.DataFrame(data)


def test_count_continuous_date(sample_data_sorted_date):
    counted_data = count_continuous_date(sample_data_sorted_date)

    expected_data = pd.DataFrame(
        {
            "START": [
                pd.Timestamp("2023-08-23"),
                pd.Timestamp("2023-08-31"),
            ],
            "END": [
                pd.Timestamp("2023-08-25"),
                pd.Timestamp("2023-09-01"),
            ],
            "LENGTH": [3, 3],
        }
    )

    assert_frame_equal(counted_data, expected_data)
