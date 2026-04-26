"""Task 02: generate unique random lottery ticket numbers."""

import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Return a sorted list of unique random numbers for a lottery ticket.

    :param min:
        The minimum allowed number in the ticket range. Must be at least 1.
    :param max:
        The maximum allowed number in the ticket range. Must be at most 1000.
    :param quantity:
        The amount of unique numbers to generate.
    :returns:
        A sorted list of unique random numbers, or an empty list if the input
        parameters are outside the allowed constraints.
    """

    if not all(type(value) is int for value in (min, max, quantity)):
        return []
    if min < 1 or max > 1000 or min > max or quantity < 1:
        return []

    available_numbers = max - min + 1
    if quantity > available_numbers:
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)
