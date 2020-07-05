"""
Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
"""

from utils.utils import get_string


def add_names_list(name_list, name):
    """Appending name of colleagues to the list"""

    return name_list.append(name)


if __name__ == '__main__':
    friends_name_list = []
    print("Enter Colleagues name to add in the list: ")
    input1 = get_string()
    result = add_names_list(friends_name_list, input1)
    print(id(friends_name_list))
    print(id(result))
    print("Here the id of list has changed")
    sorted_list = sorted(friends_name_list)
    try:
        print("First Item: ", friends_name_list[0])
        print("Second Item: ", friends_name_list[1])
    except IndexError:
        print("There is no second item in list")
