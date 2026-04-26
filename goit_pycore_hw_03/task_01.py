"""Task 01: calculate the number of days between a date and today."""

from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"


def get_days_from_today(date: str) -> int:
    """Return the number of days between ``date`` and today.

    :param date:
        A date string in ``YYYY-MM-DD`` format.
    :returns:
        The signed day difference between the given date and today.
        Positive values mean the date is in the past, negative values
        mean the date is in the future.
    :raises TypeError:
        If ``date`` is not a string.
    :raises ValueError:
        If ``date`` does not match the expected ``YYYY-MM-DD`` format.
    """

    if not isinstance(date, str):
        raise TypeError("date must be a string in YYYY-MM-DD format")

    try:
        target_date = datetime.strptime(date, DATE_FORMAT).date()
    except ValueError as error:
        raise ValueError("date must be in YYYY-MM-DD format") from error

    today = datetime.today().date()
    return (today - target_date).days
