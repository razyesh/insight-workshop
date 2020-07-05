"""
17. Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors.
"""


class Calculator:
    """
    class that acts as a simple calculator with the operation of Add, Subtract, Multiplication and Division
    """

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operator = None

    def get_two_numbers(self):
        """Method to get input from user"""
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))
        return 1

    def perform_calculation(self):
        """Method to perform calculation and print the result """
        self.operator = int(
            input("Choose Options: \n 1 = Add \n 2 = Subtract \n 3 = Division \n 4 = Multiplication \n"))
        if self.operator == 1:
            return "Addition: ", self.num2 + self.num1

        elif self.operator == 2:
            return "Subtraction: ", self.num1 - self.num2

        elif self.operator == 3:
            return "Multiplication: ", self.num1 * self.num2

        elif self.operator == 4:
            if self.num2 == 0:
                return "Not divisible by 0 Denominator"

            else:
                remainder = self.num1 % self.num2
                result = self.num1 / self.num2
                return f"remainder {remainder}" / f"answer {result}"

        else:
            return "Invalid Selection"


# object intiailization
c1 = Calculator()
c1.get_two_numbers()
result = c1.perform_calculation()
print(result)
