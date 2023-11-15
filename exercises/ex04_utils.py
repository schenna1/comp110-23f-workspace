"""EX04 - Lists !"""
__author__ = "730956810" 


def all(input: list[int], given_int: int) -> bool:
    """Evaluates if given int is the same as every int in the list."""
    index = 0
    if len(input) == 0:
        return False
    while index < len(input):
        if given_int != input[index]:
            return False
        index += 1
    return True

        
def max(input: list[int]) -> int:
    """Returns largest number from list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index = 1
    max_number = input[0]
    while index < len(input):
        if max_number < input[index]:
            max_number = input[index]
        index += 1
    return max_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Evaluates if lists are the exact same."""
    index = 0
    if len(list_1) != len(list_2):
        return False
    while index < len(list_1) and index < len(list_2):
        if list_1[index] != list_2[index]:
            return False    
        index += 1
    return True