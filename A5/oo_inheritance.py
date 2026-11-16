### Assignment oo_inheritance ###

# s123456_s56789, YourLastname1_YourLastname2       ##TODO

####### IMPORTANT #######

# Make sure your document doesn't contain any syntax error and contains all procedures

#########################



# Implement the whole functionality for this assignment in this file!
# Modify and add to the provided code!


  
class Account:

    def __init__(self, owner: str):
        self.owner = owner
        self.__balance = 0.0

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Derf ned negativ sei")
        else:
            self.__balance += amount

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Derf ned negativ sei")
        else:
            self.__balance -= amount

    def __str__(self) -> str:
        return f"Account({self.owner}: {self.__balance:.2f} EUR)"

    @staticmethod
    def transfer(amount: float, fromAccount:Account, toAccount:Account):
        if amount < 0:
            raise ValueError("Derf ned negativ sei")

        fromAccount.withdraw(amount)
        toAccount.deposit(amount)


class StudentAccount(Account):

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Derf ned negativ sei")

        if amount > self.balance:
            raise ValueError("Geht ned")
        else:
            super().withdraw(amount)

    
    

##################### Demo ############

a1 = Account("A")
a2 = Account("B")
a1.deposit(100)
a2.withdraw(100)
print(a1)
print(a2)
Account.transfer(600, a1, a2)
print(a1)
print(a2)

print(a1.owner)
print(a1.balance)

#a1.balance = 999   ##this should not be allowed!

s1 = StudentAccount("S")
s1.deposit(100)

try:
  Account.transfer(500000, s1, a1)
except:
  print("Fehler") ##TODO where should the error message come from?
print(s1)
print(a1)