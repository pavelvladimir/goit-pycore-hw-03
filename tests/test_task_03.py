import unittest

from goit_pycore_hw_03 import normalize_phone


class NormalizePhoneTestCase(unittest.TestCase):
    def test_normalizes_numbers_from_the_example(self) -> None:
        raw_numbers = [
            "067\t123 4567",
            "(095) 234-5678\n",
            "+380 44 123 4567",
            "380501234567",
            "    +38(050)123-32-34",
            "     0503451234",
            "(050)8889900",
            "38050-111-22-22",
            "38050 111 22 11   ",
        ]

        sanitized_numbers = [normalize_phone(number) for number in raw_numbers]

        self.assertEqual(
            sanitized_numbers,
            [
                "+380671234567",
                "+380952345678",
                "+380441234567",
                "+380501234567",
                "+380501233234",
                "+380503451234",
                "+380508889900",
                "+380501112222",
                "+380501112211",
            ],
        )

    def test_preserves_explicit_plus_prefix(self) -> None:
        self.assertEqual(normalize_phone("+380 50 123 45 67"), "+380501234567")

    def test_adds_plus_for_numbers_starting_with_380(self) -> None:
        self.assertEqual(normalize_phone("380501234567"), "+380501234567")

    def test_adds_ukrainian_country_code_when_missing(self) -> None:
        self.assertEqual(normalize_phone("(050)123-45-67"), "+380501234567")

    def test_returns_empty_string_when_no_digits_exist(self) -> None:
        self.assertEqual(normalize_phone("   +()-   "), "")

    def test_raises_type_error_for_non_string_value(self) -> None:
        with self.assertRaisesRegex(TypeError, "string"):
            normalize_phone(380501234567)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
