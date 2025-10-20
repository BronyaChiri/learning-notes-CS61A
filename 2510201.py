class account:
    interest = 0.02  # this is a class attribute.

    def __init__(self,holder):
        self.balance = 0
        self.holder = holder  # instance attribute

    def withdraw(self,x):
        if self.balance < x:
            print("money is not enough!")
        else:
            self.balance -= x
            print(self.balance)
            return self.balance

    def deposit(self,x):
        self.balance += x
        print(self.balance)
        return self.balance

a = account("jim")

class checkingaccount(account):
    withdraw_fee = 1
    def withdraw(self,amount):
        return account.withdraw(self,amount + self.withdraw_fee)
    
a = checkingaccount("jim")
a.deposit(300)
print(a.withdraw(499))
        
