"""Summing the elements of a list using different loops."""
__author__ = "730956810"


def w_sum(vals: list[float]) -> float:
    """Returns sum of list using while loops."""
    index: int = 0
    sum: float = 0
    if len(vals) != 0:
        while index < len(vals):
            sum += vals[index]
            index += 1
        return sum
    else:
        return 0.0
    

def f_sum(vals: list[float]) -> float:
    """Returns sum of list using for loops."""
    sum: float = 0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns sum of list using range and for loops."""
    sum: float = 0
    for index in range(0, len(vals)):
        sum += vals[index]
    return sum