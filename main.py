from goit_pycore_hw_03 import get_days_from_today


def main() -> None:
    date_input = input("Enter a date (YYYY-MM-DD): ").strip()

    try:
        result = get_days_from_today(date_input)
    except (TypeError, ValueError) as error:
        print(f"Invalid input: {error}")
        return

    print(f"Difference between today and {date_input}: {result} days")


if __name__ == "__main__":
    main()
