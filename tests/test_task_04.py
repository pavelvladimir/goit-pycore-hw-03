import datetime
import unittest
from unittest.mock import patch

from goit_pycore_hw_03 import get_upcoming_birthdays


class FixedDatetime(datetime.datetime):
    @classmethod
    def today(cls) -> "FixedDatetime":
        return cls(2024, 1, 22, 10, 30, 45)


class EndOfYearDatetime(datetime.datetime):
    @classmethod
    def today(cls) -> "EndOfYearDatetime":
        return cls(2023, 12, 28, 9, 0, 0)


class GetUpcomingBirthdaysTestCase(unittest.TestCase):
    def test_returns_example_birthdays_with_weekend_shift(self) -> None:
        users = [
            {"name": "John Doe", "birthday": "1985.01.23"},
            {"name": "Jane Smith", "birthday": "1990.01.27"},
        ]

        with patch("goit_pycore_hw_03.task_04.datetime", FixedDatetime):
            result = get_upcoming_birthdays(users)

        self.assertEqual(
            result,
            [
                {"name": "John Doe", "congratulation_date": "2024.01.23"},
                {"name": "Jane Smith", "congratulation_date": "2024.01.29"},
            ],
        )

    def test_includes_today_and_sunday_birthday(self) -> None:
        users = [
            {"name": "Today Person", "birthday": "1991.01.22"},
            {"name": "Sunday Person", "birthday": "1992.01.28"},
        ]

        with patch("goit_pycore_hw_03.task_04.datetime", FixedDatetime):
            result = get_upcoming_birthdays(users)

        self.assertEqual(
            result,
            [
                {"name": "Today Person", "congratulation_date": "2024.01.22"},
                {"name": "Sunday Person", "congratulation_date": "2024.01.29"},
            ],
        )

    def test_skips_birthdays_outside_the_next_seven_days(self) -> None:
        users = [
            {"name": "Past Person", "birthday": "1990.01.21"},
            {"name": "Later Person", "birthday": "1990.01.30"},
        ]

        with patch("goit_pycore_hw_03.task_04.datetime", FixedDatetime):
            result = get_upcoming_birthdays(users)

        self.assertEqual(result, [])

    def test_handles_year_rollover(self) -> None:
        users = [
            {"name": "New Year", "birthday": "1990.01.01"},
            {"name": "Too Far", "birthday": "1990.01.06"},
        ]

        with patch("goit_pycore_hw_03.task_04.datetime", EndOfYearDatetime):
            result = get_upcoming_birthdays(users)

        self.assertEqual(result, [{"name": "New Year", "congratulation_date": "2024.01.01"}])

    def test_raises_type_error_for_non_list_input(self) -> None:
        with self.assertRaisesRegex(TypeError, "list"):
            get_upcoming_birthdays("invalid")  # type: ignore[arg-type]

    def test_raises_value_error_for_invalid_birthday_format(self) -> None:
        users = [{"name": "Broken", "birthday": "1990-01-22"}]

        with self.assertRaisesRegex(ValueError, "%Y.%m.%d|does not match"):
            get_upcoming_birthdays(users)


if __name__ == "__main__":
    unittest.main()
