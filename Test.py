import sys
class Customer:
    '''Customer class with bank related operation'''

    bankname="State Bank Of India"


    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    
    def deposit(self,amount):
        self.balance = self.balance+amount
        print("After deposit the balance is ",self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Funds")
            sys.exit()
        self.balance=self.balance-amount
        print("After Withdraw Balance is ",self.balance)

print("Welcome to ",Customer.bankname)
name = input("Enter your name:\n")
c = Customer(name)
while(True):
    print("d - Deposit: \nw - Withdraw: \ne - Exit: \n")
    option = input("Enter your Choice: ")
    if option=="d" or option =="d":
        amount = float(input("Enter the amount to deposit: "))
        c.deposit(amount)

    elif option =='w' or option =="W":
        amount = float(input("Enter the amount to withdraw: "))
        c.withdraw(amount)
    
    elif option =="e" or option =="E":
        print("Thanks For Visiting ",Customer.bankname)
        sys.exit()

    else:
        print("Choose Valid Option ")