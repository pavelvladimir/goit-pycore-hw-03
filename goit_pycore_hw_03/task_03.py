"""Task 03: normalize phone numbers to a standard SMS-friendly format."""

import re


def normalize_phone(phone_number: str) -> str:
    """Return a normalized Ukrainian phone number with an international prefix.

    :param phone_number:
        A raw phone number string in an arbitrary user-provided format.
    :returns:
        A normalized phone number containing only digits and a leading ``+``.
        If the country code is missing, the function adds ``+38``.
    :raises TypeError:
        If ``phone_number`` is not a string.
    """

    if not isinstance(phone_number, str):
        raise TypeError("phone_number must be a string")

    stripped_number = phone_number.strip()
    has_plus_prefix = stripped_number.startswith("+")
    digits_only = re.sub(r"\D", "", stripped_number)

    if not digits_only:
        return ""
    if has_plus_prefix or digits_only.startswith("380"):
        return f"+{digits_only}"
    return f"+38{digits_only}"
