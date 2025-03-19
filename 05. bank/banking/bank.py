import random
from banking.bank_account import BankAccount


class Bank:
    def __init__(self):
        self.account_types = {}
        self.accounts = {}

    def validate_string(self, value):
        if not isinstance(value, str):
            raise TypeError(f"{value} must be a string")

    def validate_account_number(self, account_number):
        self.validate_string(account_number)

        if not account_number.isdigit():
            raise ValueError(
                f"Account number: {account_number}, is not numeric. Ensure that the account number consists of digits only"
            )

        if len(account_number) != 10:
            raise ValueError("Please enter a ten digit account number")

    def validate_account_exists(self, account_number):
        if account_number not in self.accounts.keys():
            raise ValueError(f"Account number: {account_number}, does not exist")

    def add_account(self, account_number, account_name):
        self.accounts[account_number] = {
            "account_type": account_name,
            "account": BankAccount(self.account_types[account_name]),
        }

    def generate_account_number(self):
        while True:
            account_number = f"{random.randint(1000000000, 9999999999)}"
            if account_number not in self.accounts.keys():
                return account_number

    def add_account_type(self, account_name, interest_rate):
        self.validate_string(account_name)
        BankAccount.validate_type(interest_rate)

        if account_name not in self.account_types.keys():
            self.account_types[account_name] = interest_rate
        else:
            raise ValueError(f"{account_name} already exists")

    def open_bank_account(self, account_name):
        self.validate_string(account_name)
        account_number = self.generate_account_number()
        self.add_account(account_number, account_name)
        return account_number

    def deposit(self, account_number, amount):
        self.validate_account_number(account_number)
        self.validate_account_exists(account_number)
        self.accounts[account_number]["account"].deposit(amount)

    def withdraw(self, account_number, amount):
        self.validate_account_number(account_number)
        self.validate_account_exists(account_number)
        self.accounts[account_number]["account"].withdraw(amount)

    def transfer(self, from_account_number, to_account_number, amount):
        self.withdraw(from_account_number, amount)
        self.deposit(to_account_number, amount)

    def compound_interest(self):

        for account_details in self.accounts.values():
            account_details["account"].compound_interest()

    def get_balance(self, account_number):
        self.validate_account_number(account_number)
        self.validate_account_exists(account_number)
        return self.accounts[account_number]["account"].balance

    def get_interest_rate(self, account_number):
        self.validate_account_number(account_number)
        self.validate_account_exists(account_number)
        return self.account_types[self.accounts[account_number]["account_type"]]
