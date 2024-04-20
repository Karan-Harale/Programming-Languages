'''Q2.In the BankAccount class that you had created in the previous exercise, delete the set_details() method and create an __init__ method'''

class Bankaccount:

    def __init__(self,name,balance=0):
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
    msg = int(input("nWhat Do you want to do?\n1. Create New Account\n2. Display Balance\n3. Withdraw Money\n4. Deposite Money\n\nChoice: "))

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