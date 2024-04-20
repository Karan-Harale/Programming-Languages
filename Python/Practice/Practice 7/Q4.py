while True:

 num=int (input("Enter Number :"))
 prime=True

 for i in range(2,num):    
   if (num%2==0):
    prime=False
    break

 if prime: 
    print("Prime number")
 else:
    print("Not Prime number")