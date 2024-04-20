arr=[]

arr_length=int(input("Length:- "))

copyarr=[]

count=0

for i in range(arr_length):
    num=(int(input(': ')))
    arr.append(num)
    copyarr.append(num)

print (arr)

copyarr.sort()
print(copyarr)

for i in range (arr_length):
    if (copyarr[i]==arr[i]):
        count+=1

print(count)

# using  function
# def sorted(arr,num):

#     copyarr=[0] * n

#     for i in range(n): 
#         copyarr[i]=arr[i]


#     count=0
#     arr.sort()
#     print (arr)


#     for i in range(n):
#         if (arr[i]==copyarr[i]):
#             count+=1

#     return count



# arr=[1,3,2,4,5]
# n=len(arr)

# print(sorted(arr,n))