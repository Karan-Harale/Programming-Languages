arr1=[5,2,7,3,9]
arr1=arr1[::-1]
arr2=[55,45,35,25,55]

arr3=[]

while (len(arr2)!=0):
    arr3.append(arr1.pop())
    arr3.append(arr2.pop())

print(arr3)
print(sorted(arr3))
