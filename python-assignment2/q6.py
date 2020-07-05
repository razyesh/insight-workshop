"""
Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

"""

from q5 import user_info


def add_friend(friend_list):
    """
    adding friend to the friend list
    :param friend_list: list where the friend should add
    :return: friend list
    """
    for _ in range(3):
        result = user_info()
        friend_list.append(result)

    return friend_list


if __name__ == "__main__":
    friend_list = []
    result = add_friend(friend_list)
    count = 0
    for i in result:
        if i[0] == 'John':
            count = 1

    if count == 1:
        print("Found")
    else:
        print("Not found")
