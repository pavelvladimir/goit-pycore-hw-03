import unittest
import datetime
from unittest.mock import patch

from goit_pycore_hw_03 import get_days_from_today


class FixedDatetime(datetime.datetime):
    @classmethod
    def today(cls) -> "FixedDatetime":
        return cls(2021, 5, 5, 15, 30, 45)


class GetDaysFromTodayTestCase(unittest.TestCase):
    def test_returns_negative_value_for_future_date(self) -> None:
        with patch("goit_pycore_hw_03.task_01.datetime", FixedDatetime):
            result = get_days_from_today("2021-10-09")

        self.assertEqual(result, -157)

    def test_returns_positive_value_for_past_date(self) -> None:
        with patch("goit_pycore_hw_03.task_01.datetime", FixedDatetime):
            result = get_days_from_today("2021-04-30")

        self.assertEqual(result, 5)

    def test_returns_zero_for_today(self) -> None:
        with patch("goit_pycore_hw_03.task_01.datetime", FixedDatetime):
            result = get_days_from_today("2021-05-05")

        self.assertEqual(result, 0)

    def test_raises_value_error_for_invalid_format(self) -> None:
        with self.assertRaisesRegex(ValueError, "YYYY-MM-DD"):
            get_days_from_today("05-05-2021")

    def test_raises_type_error_for_non_string_value(self) -> None:
        with self.assertRaisesRegex(TypeError, "string"):
            get_days_from_today(20210505)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
