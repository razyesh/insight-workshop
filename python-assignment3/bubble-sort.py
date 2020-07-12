"""
Implementation of Bubble Sort
"""


def bubble_sort(sample_list):
    """
    Function to sort the element using Bubble Sort
    :param sample_list: the unsorted array of list
    :return: sorted array of list
    """
    for i in range(len(sample_list)):
        for j in range(len(sample_list)):
            try:
                if sample_list[j+1] < sample_list[j]:
                    temp = sample_list[j]
                    sample_list[j] = sample_list[j+1]
                    sample_list[j+1] = temp
            except IndexError:
                pass

    return sample_list


if __name__ == "__main__":
    sample_input = [5, 4, 1, 3, 2, 20, 23, 21]
    result = bubble_sort(sample_input)
    print("Result After Bubble Sort", result)