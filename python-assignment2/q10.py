"""
10. Write a function that takes camel-cased strings (i.e.
ThisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well.
"""


def get_camel_case(input_string, separation_param):
    """Function to convert the camel-case string into the snake case or kebab case or any other case"""
    convert_list = list(input_string)
    place_to_insert = []
    count = 0
    for i in range(len(convert_list)):
        if convert_list[i].isupper():
            if i != 0:
                place_to_insert.append(i+count)
                count += 1

    for i in place_to_insert:
        convert_list.insert(i, separation_param)

    return "".join(convert_list)


if __name__ == "__main__":
    sample_input = 'ThisIsCamelCased'
    result = get_camel_case(sample_input, '-')
    result2 = get_camel_case(sample_input, '_')
    print(result)
    print(result2)