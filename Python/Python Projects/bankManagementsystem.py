'''Q1. Make a class that represents a bank account. Create four methods named set_details, display, withdraw and deposit.
In the set_details method, create two instance variables : name and balance. The default value for balance should be zero. In the display method, display the values of these two instance variables.
Both the methods withdraw and deposit have amount as parameter. Inside withdraw, subtract the amount from balance and inside deposit, add the amount to the balance.
Create two instances of this class and call the methods on those instances.
'''

class Bankaccount:

    def __init__(self):
        pass

    def set_detail(self,name,balance=0):
        self.name=name
        self.balance=balance

    def display(self):
        return print(f"Name: {self.name}\nBalance: {self.balance}")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

accountobj=Bankaccount()

while (1):
    msg = int(input("What Do you want to do?\n1. Create New Account\n2. Display Balance\n3. Withdraw Money\n4. Deposite Money\n\nChoice: "))

    if msg == 1:
        Name = input("Enter Name: ")
        Amount=int(input("Enter Deposite Amount: "))

        accountobj.set_detail(Name,Amount)
        print("Account Created Successfully")

    elif msg == 2:
        accountobj.display()

    elif msg == 3:
        amount = int(input("How Much Amount you want to withdraw : "))
        accountobj.withdraw(amount)
        accountobj.display()

    elif msg == 4:
        damount = int(input("How Much Amount you want to Deposite : "))
        accountobj.deposit(damount)
        accountobj.display()

    else:
        print("Invalid Choice !!!")