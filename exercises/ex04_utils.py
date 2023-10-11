"""EX04 - Lists !"""
__author__ = "730956810" 

def all(input: list[int], given_int: int) -> bool:
    index = 0
    while index < len(input):
        if given_int == input[index]:
            index += 1
            return True
        else:
            return False
        
def max(input: list[int]) -> bool:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index = 1
    max_number = input[0]
    while index < len(input):
        if max_number > input[index]:
            index += 1
            return max_number
        else:
            max_number = input[+1]
            return input[index]

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    index_1 = 0
    index_2 = 0
    while index_1 < len(list_1) and index_2 < len(list_2):
        if list_1[index_1] == list_2[index_2]:
            index_1 += 1
            index_2 += 2
            return True
        else:
            return False



