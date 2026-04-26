from goit_pycore_hw_03 import get_days_from_today, get_numbers_ticket, normalize_phone


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


def run_task_03() -> None:
    phone_number = input("Enter phone number: ")

    try:
        normalized_phone = normalize_phone(phone_number)
    except TypeError as error:
        print(f"Invalid input: {error}")
        return

    if not normalized_phone:
        print("Invalid input: phone number must contain digits.")
        return

    print(f"Normalized phone number: {normalized_phone}")


def main() -> None:
    print("Choose a task:")
    print("1 - Days from today")
    print("2 - Lottery ticket numbers")
    print("3 - Normalize phone number")
    choice = input("Enter task number: ").strip()

    if choice == "1":
        run_task_01()
        return
    if choice == "2":
        run_task_02()
        return
    if choice == "3":
        run_task_03()
        return

    print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
