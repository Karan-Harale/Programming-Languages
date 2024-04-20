balance=0
pin=1234

while(1):
    custInput=int(input("1. Check Balance\n2. Withdraw Money\n3. Deposite\n4. Quit\n Enter option: "))
    
    if custInput==1:
        pinCheck=int(input("Enter 4 Digit pin: "))
        if pinCheck==pin:
            print("Total balance: ",balance)
        else:
            print("you've Entered Wrong pin\n Try Again!!")
    elif custInput==2:
        enterMoney=int(input("How Much Money Do You Want to withdraw : "))

        pinCheck=int(input("Enter 4 Digit pin: "))
        
        

        
        if enterMoney<=balance:
            if pinCheck==pin:
                balance-=enterMoney
                print("Total balance: ",balance)
            else:
                print("you've Entered Wrong pin\n Try Again!!")
        else:    
            print("Insufficient Balance ",balance)
    elif custInput==3:
        enterMoney=int(input("How Much Money Do You Want to Deposite : "))
        if enterMoney>0:
            balance+=enterMoney
            print("Deposited ",enterMoney,"to your Account total Balance = ",balance) 
        else:
            print("Enter Valid Amount")
    else:
        pass


