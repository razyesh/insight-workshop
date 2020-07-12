"""
Implementation of Binary Search

"""
from quick_sort import quick_sort


def search_item(sequence, item):
    """
    function to perform binary search operation
    :param sequence:
    :param item:
    :return:
    """
    mid_value = len(sequence) // 2
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


if __name__ == "__main__":
    sample_input = quick_sort([5, 4, 1, 3, 2, 20, 23, 21])
    item = int(input("Enter the number to search: "))
    result = search_item(sample_input, item)
    print(result)