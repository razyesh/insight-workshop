"""
Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.
"""

import math


def search_item(sequence, item):
    """
    function to perform binary search operation
    :param sequence:
    :param item:
    :return:
    """
    mid_value = math.ceil(len(sequence) / 2)
    count = 0
    if item == sequence[mid_value]:
        return "Found"
    else:
        try:
            if item > sequence[mid_value]:
                return search_item(sequence[mid_value:], item)
            elif item < sequence[mid_value]:
                return search_item(sequence[:mid_value], item)

        except IndexError:
            return "Not found"


result = search_item([1, 2, 3, 4, 5, 6], 2)
print(result)
