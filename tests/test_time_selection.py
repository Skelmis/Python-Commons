import datetime

import pytest

from commons import timing


@pytest.mark.parametrize(
    "current_time,check_time,delta,expected",
    (
        (
            datetime.datetime(2025, 1, 5, 4, 30),
            datetime.datetime(2025, 1, 5, 4, 31),
            datetime.timedelta(minutes=5),
            True,
        ),
        (
            datetime.datetime(2025, 1, 5, 4, 30),
            datetime.datetime(2025, 1, 7, 4, 31),
            datetime.timedelta(minutes=5),
            False,
        ),
        (
            datetime.datetime(2025, 1, 4, 23, 59),
            datetime.datetime(2025, 1, 5, 0, 2),
            datetime.timedelta(minutes=5),
            True,
        ),
        (
            datetime.datetime(2025, 1, 5, 4, 30),
            datetime.datetime(2025, 1, 5, 4, 6),
            datetime.timedelta(minutes=5),
            False,
        ),
        (
            datetime.datetime(2025, 1, 5, 4, 30),
            datetime.datetime(2025, 1, 7, 4, 6),
            datetime.timedelta(days=5),
            True,
        ),
        (
            datetime.datetime(2025, 1, 5, 4, 30),
            datetime.datetime(2025, 5, 7, 4, 6),
            datetime.timedelta(days=300),
            True,
        ),
    ),
)
async def test_time_compare(current_time, check_time, delta, expected):
    assert timing.is_within_next_(current_time, check_time, delta) == expected
