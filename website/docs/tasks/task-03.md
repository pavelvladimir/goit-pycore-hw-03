---
sidebar_position: 3
---

# Task 3

`normalize_phone(phone_number)` converts phone numbers from mixed user formats into a normalized SMS-friendly representation.

## Requirements covered

- removes spaces, punctuation, tabs, and line breaks
- keeps only digits and a leading `+`
- adds the Ukrainian `+38` country code when it is missing
- returns a normalized string ready for SMS processing

## Example

```python
from goit_pycore_hw_03 import normalize_phone

number = normalize_phone("    +38(050)123-32-34")
print(number)
```

For the generated Python API reference, open [API Reference](/python-api).
