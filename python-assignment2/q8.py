"""
Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.
"""


def check_prime(n):
    """
    function to check whether the number n is prime or not
    :param n: any number
    :return: prime if prime else not prime
    """
    flag = 0
    for i in range(2, n):
        if n % i == 0:
            flag += 1

    if flag == 0:
        return "Prime"
    else:
        return "Not Prime"


if __name__ == "__main__":
    n = int(input("Enter integer: "))
    result = check_prime(n)
    print(result)