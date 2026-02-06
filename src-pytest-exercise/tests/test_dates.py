import pytest
from timeutils.dates import days_between, is_weekend, format_relative

def test_days_between_same_day():
    """Two identical dates should be 0 days apart."""
    assert days_between("2025-03-15", "2025-03-15") == 0
def test_days_between_one_week():
    """A known pair exactly 7 days apart."""
    assert days_between("2025-03-01", "2025-03-08") == 7
def test_days_between_order_independent():
    """Swapping the arguments should give the same result."""
    assert days_between("2025-01-01", "2025-06-15") == days_between("2025-06-15", "2025-01-01")
def test_is_weekend_saturday():
    """March 15, 2025 is a Saturday."""
    assert is_weekend("2025-03-15") is True
def test_is_weekend_weekday():
    """March 17, 2025 is a Monday."""
    assert is_weekend("2025-03-17") is False
def test_days_between_invalid_format():
    """A badly formatted string should raise ValueError."""
    with pytest.raises(ValueError):
        days_between("not-a-date", "2025-03-15")

def test_relative_format_is_today():
    assert format_relative("2026-02-06") == "today"

def test_relative_format_is_in_future():
    assert format_relative("2026-02-25") == "in 19 day(s)"

def test_relative_format_is_in_past():
    assert format_relative("2026-02-01") == "5 day(s) ago"