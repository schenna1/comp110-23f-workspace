"""Combining two lists into a dictionary."""
__author__ = "730956810"


def zip(word: list[str], integer: list[int]) -> dict[str, int]:
    """Returns a word and its corresponding value at the same index."""
    empty_dict: dict[str, int] = {}

    if len(word) != 0 and len(integer) != 0 and len(word) == len(integer):
        for elem in range(0, len(word)):
            empty_dict[word[elem]] = integer[elem]  
    return empty_dict             