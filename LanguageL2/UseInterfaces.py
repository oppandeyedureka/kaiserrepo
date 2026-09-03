from abc import ABC, abstractmethod


class bankingoperations:
    @abstractmethod
    def Deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

class Account(bankingoperations):
    def ShowDetails(self):
        print("Hello")

 