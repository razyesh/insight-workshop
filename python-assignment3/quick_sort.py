"""
Implementing quick sort algorithm
"""


def quick_sort(sample_input):
    """
    function to sort the unsorted sample_inputay using Quick Sort Algorithm
    :param sample_input: unsorted list of array
    :return: sorted list of array
    """

    if len(sample_input) <= 1:
        return sample_input

    pivot = sample_input[len(sample_input) // 2]
    left = [x for x in sample_input if x < pivot]
    middle = [x for x in sample_input if x == pivot]
    right = [x for x in sample_input if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    sample_input = [5, 4, 1, 3, 2, 20, 23, 21]
    result = quick_sort(sample_input)
    print("Quick Sort: ", result)