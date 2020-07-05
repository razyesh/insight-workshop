"""
Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
"""


def check_palindrome(n):
    """simple function to check whether given number is palindrome or not"""
    original = n
    reversen = 0
    while n != 0:
        remainder = n % 10
        reversen = reversen * 10 + remainder
        n = n // 10

    if original == reversen:
        return "Palindrome"

    else:
        return "Not Palindrome"


n = int(input("Enter an integer to check palindrome: "))
result = check_palindrome(n)
print(result )
