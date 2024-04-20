num1=int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))
num3=int(input("Enter Number 3:"))
num4=int(input("Enter Number 4:"))

if num1>num2:
    f1=num1
else:
    f1=num2
if num3>num4:
    f2=num3
else:
    f2=num4

if f1>f2:
    print(f1)
else:
    print(f2)