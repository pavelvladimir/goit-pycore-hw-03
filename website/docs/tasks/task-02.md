---
sidebar_position: 2
---

# Task 2

`get_numbers_ticket(min, max, quantity)` generates a sorted list of unique random numbers for a lottery ticket.

## Requirements covered

- validates the allowed `min`, `max`, and `quantity` constraints
- guarantees unique values
- returns a sorted list
- returns an empty list for invalid input

## Example

```python
from goit_pycore_hw_03 import get_numbers_ticket

numbers = get_numbers_ticket(1, 49, 6)
print(numbers)
```

For the generated Python API reference, open [API Reference](/python-api).
