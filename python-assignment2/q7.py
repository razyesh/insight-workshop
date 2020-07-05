"""
Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.

"""

from q6 import add_friend


if __name__ == "__main__":
    friend_list = []
    result = add_friend(friend_list)
    count = 0
    total = 0
    for i in result:
        total = total + i[2]

    average = total / len(friend_list)

    status = []

    for i in result:
        if i[2] < average:
            status.append("Young")
        elif i[2] > average:
            status.append("Old")
        else:
            status.append("Average")

    print(status)
