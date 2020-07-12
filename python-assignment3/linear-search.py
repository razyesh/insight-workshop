"""
Implementation of Linear Search
"""


def linear_search(sample_input, item):
    """
    function to search the element in the sample list using linear method
    :param sample_input: just a simple list of number
    :param item: item to search
    :return: return true if found else false
    """
    for i in sample_input:
        if item == i:
            return "Found at Index {}".format(sample_input.index(item) + 1)

    return "Not Found"


if __name__ == "__main__":
    sample_input = [5, 4, 1, 3, 2, 20, 23, 21]
    item = int(input("Enter the Item to Search: "))
    result = linear_search(sample_input, item)
    print(result)
