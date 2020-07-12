"""
Implementation of Insertion Sort
"""


def insertion_sort(sample_input):
    """
    function to sort the elements of array using insertion sort
    :param sample_input: unsorted list of array
    :return: sorted list of array
    """
    for i in range(len(sample_input)):
        j = i
        while j > 0 and sample_input[j] < sample_input[j - 1]:
            sample_input[j], sample_input[j - 1] = sample_input[j - 1], sample_input[j]
            j -= 1
    return sample_input


if __name__ == "__main__":
    sample_input = [5, 4, 1, 3, 2, 20, 23, 21]
    result = insertion_sort(sample_input)
    print(result)
