num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))
list1=[]
list2=[]

for i in range(1,num1+1):
    list1.append(i*num1)
for j in range(1,num2+1):
    list2.append(j*num2)


lcm=[]
for i in list1:
    for j in list2:
        if i==j:
            lcm.append(i)
            break

print("LCM = ", lcm[0])
