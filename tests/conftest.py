import pytest

from commons.caching import TimedCache


@pytest.fixture
def create_timed_cache() -> TimedCache:
    return TimedCache()
