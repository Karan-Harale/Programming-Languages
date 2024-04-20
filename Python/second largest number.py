arr=[]

sampleInput=int(input())

for i in range(sampleInput):
    element=int(input() )
    arr.append(element)

arr.sort()
result=arr[-2]

print("o/p=",result)