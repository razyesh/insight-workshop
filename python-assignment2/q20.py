"""
20. Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""


def get_three_num(sample_list):
    """
    function to get the three numbers from the given list
    :param sample_list:
    :return:
    """
    output = []
    n = len(sample_list)
    for i in range(n - 1):
        s = set()
        for j in range(i + 1, n):
            x = -(sample_list[i] + sample_list[j])
            if x in s:
                output.append([x, sample_list[i], sample_list[j]])
            else:
                s.add(sample_list[j])

    return output


result = get_three_num([-25, -10, -7, -3, 2, 4, 8, 10])
print(result)


