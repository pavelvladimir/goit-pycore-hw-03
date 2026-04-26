"""Task 04: calculate upcoming birthday congratulations."""

from datetime import date, datetime, timedelta

DATE_FORMAT = "%Y.%m.%d"


def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    """Return colleagues who should be congratulated within the next 7 days.

    :param users:
        A list of dictionaries with ``name`` and ``birthday`` keys. The
        birthday value must be a string in ``YYYY.MM.DD`` format.
    :returns:
        A list of dictionaries containing ``name`` and
        ``congratulation_date`` keys. Weekend birthdays are shifted to the
        following Monday.
    :raises TypeError:
        If ``users`` is not a list of dictionaries with string values.
    :raises ValueError:
        If a birthday string does not match the expected format.
    """

    if not isinstance(users, list):
        raise TypeError("users must be a list of dictionaries")

    today = datetime.today().date()
    upcoming_birthdays: list[dict[str, str]] = []

    for user in users:
        if not isinstance(user, dict):
            raise TypeError("each user must be a dictionary")

        name = user.get("name")
        birthday_value = user.get("birthday")
        if not isinstance(name, str) or not isinstance(birthday_value, str):
            raise TypeError("user name and birthday must be strings")

        birthday = datetime.strptime(birthday_value, DATE_FORMAT).date()
        birthday_date = _get_next_birthday_date(birthday, today)
        days_until_birthday = (birthday_date - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = _shift_to_workday(birthday_date)
            upcoming_birthdays.append(
                {
                    "name": name,
                    "congratulation_date": congratulation_date.strftime(DATE_FORMAT),
                }
            )

    return upcoming_birthdays


def _get_next_birthday_date(birthday: date, today: date) -> date:
    birthday_this_year = _replace_year(birthday, today.year)
    if birthday_this_year < today:
        return _replace_year(birthday, today.year + 1)
    return birthday_this_year


def _replace_year(birthday: date, year: int) -> date:
    try:
        return birthday.replace(year=year)
    except ValueError:
        return birthday.replace(year=year, day=28)


def _shift_to_workday(birthday_date: date) -> date:
    if birthday_date.weekday() == 5:
        return birthday_date + timedelta(days=2)
    if birthday_date.weekday() == 6:
        return birthday_date + timedelta(days=1)
    return birthday_date
