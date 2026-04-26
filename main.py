from goit_pycore_hw_03 import get_days_from_today, get_numbers_ticket


def run_task_01() -> None:
    date_input = input("Enter a date (YYYY-MM-DD): ").strip()

    try:
        result = get_days_from_today(date_input)
    except (TypeError, ValueError) as error:
        print(f"Invalid input: {error}")
        return

    print(f"Difference between today and {date_input}: {result} days")


def run_task_02() -> None:
    try:
        min_number = int(input("Enter minimum number: ").strip())
        max_number = int(input("Enter maximum number: ").strip())
        quantity = int(input("Enter quantity of numbers: ").strip())
    except ValueError:
        print("Invalid input: min, max, and quantity must be integers.")
        return

    numbers = get_numbers_ticket(min_number, max_number, quantity)
    if not numbers:
        print("Invalid input: unable to generate ticket numbers with these parameters.")
        return

    print(f"Your lottery numbers: {numbers}")


def main() -> None:
    print("Choose a task:")
    print("1 - Days from today")
    print("2 - Lottery ticket numbers")
    choice = input("Enter task number: ").strip()

    if choice == "1":
        run_task_01()
        return
    if choice == "2":
        run_task_02()
        return

    print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
