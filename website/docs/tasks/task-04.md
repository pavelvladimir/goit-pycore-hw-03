---
sidebar_position: 4
---

# Task 4

`get_upcoming_birthdays(users)` returns colleagues whose birthdays fall within the next 7 days, including today.

## Requirements covered

- checks birthdays within the next 7 days including the current date
- shifts Saturday and Sunday congratulations to the following Monday
- returns a list of dictionaries with `name` and `congratulation_date`
- supports year rollover when the birthday window crosses into the next year

## Example

```python
from goit_pycore_hw_03 import get_upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]

upcoming = get_upcoming_birthdays(users)
print(upcoming)
```

For the generated Python API reference, open [API Reference](/python-api).
