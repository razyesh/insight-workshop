"""
5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
"""

import datetime


def user_info():
    """
    getting user info as for first_name, last_name and birth_date
    :return: returning user info
    """
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    birth_date = input("Enter age (year/month/date): ")
    age = (calculate_age(birth_date)/365).days
    return first_name, last_name, age


def calculate_age(birth_age):
    return datetime.datetime.today() - datetime.datetime.strptime(birth_age, '%Y/%m/%d')


def take_first(elem):
    return elem[1]


def take_second(elem):
    return elem[2]


if __name__ == "__main__":
    people = []
    print("Enter data of 3 people")
    for i in range(3):
        result = user_info()
        people.append(result)
    print("Sorted using first_name: ", sorted(people, key=take_first))
    print("Sorted using last_name: ", sorted(people, key=take_second))
    print("Sorted using age: ", sorted(people))




