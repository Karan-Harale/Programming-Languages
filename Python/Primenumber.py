number=int(input("Enter Number: "))
count=0
for i in range(2,number+1):
    if(i%2==0):
        count+=1
    else:
        pass

if count>1:
    print(number ," is Non Prime Number ")
else:
    print(number ," is Prime Number ")
