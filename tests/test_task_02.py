import unittest
from unittest.mock import patch

from goit_pycore_hw_03 import get_numbers_ticket


class GetNumbersTicketTestCase(unittest.TestCase):
    def test_returns_sorted_unique_numbers(self) -> None:
        with patch("goit_pycore_hw_03.task_02.random.sample", return_value=[23, 4, 45, 15, 37, 28]):
            result = get_numbers_ticket(1, 49, 6)

        self.assertEqual(result, [4, 15, 23, 28, 37, 45])

    def test_calls_random_sample_with_inclusive_range(self) -> None:
        with patch("goit_pycore_hw_03.task_02.random.sample", return_value=[5, 3, 1]) as mocked_sample:
            get_numbers_ticket(1, 5, 3)

        mocked_sample.assert_called_once_with(range(1, 6), 3)

    def test_returns_empty_list_for_invalid_boundaries(self) -> None:
        self.assertEqual(get_numbers_ticket(0, 49, 6), [])
        self.assertEqual(get_numbers_ticket(1, 1001, 6), [])
        self.assertEqual(get_numbers_ticket(10, 5, 3), [])

    def test_returns_empty_list_when_quantity_is_invalid(self) -> None:
        self.assertEqual(get_numbers_ticket(1, 49, 0), [])
        self.assertEqual(get_numbers_ticket(1, 5, 6), [])

    def test_returns_empty_list_for_non_integer_values(self) -> None:
        self.assertEqual(get_numbers_ticket(1.5, 49, 6), [])  # type: ignore[arg-type]
        self.assertEqual(get_numbers_ticket(1, 49, "6"), [])  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
