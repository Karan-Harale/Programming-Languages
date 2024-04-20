number=input("Enter Number: ")
sum=0
for i in number:
    i=int (i)
    i=(i**len(number))
    sum+=i
if (int(number)==sum):
    print("ArmstrongNumber")
else:
    print("Number is Non ArmstrongNumber")



