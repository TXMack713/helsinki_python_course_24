#!/usr/bin/env python 3

class BankAccount:
    def __init__(self, name: str, account: str, balance: float):
        self.__name = name
        self.__account = account
        self.__balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()
        else:
            raise ValueError("The deposit amount cannot be negative.")
    
    def withdraw(self, amount: float):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__service_charge()
        else:
            raise ValueError("Insufficient funds.")
    
    # Balance getter
    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        self.__balance *= 0.99


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)
    
