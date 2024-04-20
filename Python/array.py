# indexing starts with 1 

in1=int(input("Enter Size of array: "))
arr=[]
for i in range(in1):
    in2=int(input(f"Enter {i} element in array:"))
    arr.append(in2)

print(arr)

in3=int(input("Enter Which element you want to locate: "))


if in3 in arr:
    print(f"location of {in3} in array: ",arr.index(in3)+1)
else:
    print("Enter valid element")

