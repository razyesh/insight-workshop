"""
Implementation of Merge Sort
"""


def merge_sort(sample_input):
    """
    function to sort unsorted list of array using merge sort
    :param sample_input: unsorted list of array
    :return: sorted list of array
    """
    if len(sample_input) > 1:
        mid = len(sample_input) // 2
        left_half = sample_input[:mid]
        right_half = sample_input[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sample_input[k] = left_half[i]
                i = i + 1
            else:
                sample_input[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            sample_input[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            sample_input[k] = right_half[j]
            j = j + 1
            k = k + 1

        return sample_input

    else:
        return sample_input


if __name__ == '__main__':
    sample_input = [5, 4, 1, 3, 2, 20, 23, 21]
    result = merge_sort(sample_input)
    print(result)