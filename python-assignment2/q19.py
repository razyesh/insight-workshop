"""
19. Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
"""
import re


def check_bracket_validity(sample_input):

    """function to validate parenthesis"""

    openning_bracket = '{(['
    closing_bracket = '])}'
    count1 = 0
    count2 = 0
    for i in openning_bracket:
        if i in sample_input:
            count2 += 1

    for i in closing_bracket:
        if i in sample_input:
            count1 += 1

    if count1 == count2:
        return 'valid'

    else:
        return "invalid"


result = check_bracket_validity('()[]{}')
print(result)