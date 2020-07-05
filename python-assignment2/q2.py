"""
2. Write an if statement to determine whether a variable holding a year
is a leap year.
"""

from utils.utils import get_integer


def check_leap_year(year):
    """
    function to check if the given year is leap year or not
    :param year: input parameter
    :return: True if it is a leapyear else False
    """

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    else:
        return False


if __name__ == "__main__":
    print("Enter a Year: ")
    year = get_integer()
    result = check_leap_year(year)
    print(result)