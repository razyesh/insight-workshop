import csv
from datetime import datetime


class Student:
    """
    Class for student where student can get the detail about the course and register themselves from the academy program
    """
    def __init__(self):
        print("Hello How Can we help you!!!")
        self.deposit_amount = 20000
        self.duplicate_email_msg = "User with this email already registered"
        self.error_balance_msg = "The minimum amount to deposit now must be Rs.10,000 and not greater than 20000"
        self.success_msg = "Student Successfully Registered"

    def get_detail(self):
        """
        method to get the user information for registering in Academy program
        :return:
        """
        self.name = input("Your Name: ")
        self.email = input("Your Email: ")
        response = self.validate_user(self.email)
        if not response:
            self.address = input("Your Address: ")
            self.deposited_amount = int(input("Amount You Wish to deposit now: "))
            self.date_of_join = datetime.today()
            if self.deposited_amount < 10000 or self.deposited_amount > 20000:
                return self.error_balance_msg

            detail = {'name': self.name, 'email': self.email, 'address': self.address,
                      'date_of_join': self.date_of_join,
                      'deposited_amount': self.deposited_amount,
                      'remaining_amount': 20000 - self.deposited_amount}
            return detail
        else:
            return self.duplicate_email_msg

    def register_student(self):
        """
        method to save record into our database
        :return:
        """
        detail = self.get_detail()
        if detail == self.error_balance_msg or detail == self.duplicate_email_msg:
            return detail

        else:
            with open('students.csv', 'a', newline='') as student_record:
                fieldnames = ['name', 'email', 'address', 'date_of_join', 'deposited_amount', 'remaining_amount']
                writer = csv.DictWriter(student_record, fieldnames=fieldnames)
                writer.writerow(detail)
                return self.success_msg

    @staticmethod
    def validate_user(email):
        """
        Checking whether or not user exists
        :param email: email to check
        :return: true if found else false
        """
        with open('students.csv') as student_record:
            reader = csv.DictReader(student_record)
            for row in reader:
                if row['email'] == email:
                    return True
            return False



