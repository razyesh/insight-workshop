"""
Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?
"""
import random


class Customer:
    """
    simple banking application through the point of view from customer
    """
    def __init__(self, full_name, age, address):
        """Basic attributes of any customer"""
        self.full_name = full_name
        self.age = age
        self.address = address
        self.actual_balance = 0
        self.services = None

    def open_bank_account(self):
        """Openning new bank account"""
        id = random.randint(0, 1000)
        self.full_name = input("Provide your Full name: ")
        permanent_address = input("Please provide your permanent address: ")
        father_name = input("Please provide your Father name: ")
        mother_name = input("Please provide your Mother name: ")
        grand_father_name = input("Please provide your grand father name: ")
        occupation = input("Are you (Student, Businessman, Employed): ")
        services = input("Do you plan using any of our services (Debit Card, M-banking, e-Banking etc.) y/n: ")

        return id, permanent_address, father_name, mother_name, grand_father_name, occupation, services

    def withdraw_money(self):
        """Function to handle the withdrawing user balance"""
        uid = random.randint(0, 1000)
        amount_withdraw = int(input("Enter amount to withdraw: "))
        result = self.update_balance(uid, amount_withdraw, "withdraw")

    def update_balance(self, uid, amount, key):
        """function to update the user balance"""
        if key == "withdraw":
            if self.actual_balance < amount:
                return "Not enough balance"
            else:
                self.actual_balance = self.actual_balance - amount_withdraw
                return "Success"

        elif key == "deposit":
            self.actual_balance = self.actual_balance + amount
            return "Success"

    def deposit_money(self):
        uid = random.randint(0, 1000)
        amount_deposit = int(input("Enter the amount to deposit: "))
        result = self.update_balance(self, uid, amount_deposit, "deposit")

    def update_services(self, uid):
        self.services = self.get_user_services(uid)
        return self.services

    @staticmethod
    def get_user_services(uid):
        return "Service list returned"





