k=int(input("Enter No. of elements: "))
ki=[]
for i in range(k):
    a=int(input("Enter element in k array : "))
    ki.append(a)
print(ki)

s=int(input("Enter Number Of students: "))
si=[]
for i in range(s):
    b=int(input("Credits of student: "))
    si.append(b)
print(si)
si.sort()
print(si)

maxi=si[-1]
print (maxi)
count=0

for i in ki:
    if i<=maxi:
        count+=1
print(count)