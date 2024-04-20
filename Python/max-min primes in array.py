# array=[]
# array_length=int(input("N: "))

# for i in range(array_length):
#     i+=1

#     num=i
#     if num<=2:
#         None
#     elif (num%2==1):
#         array.append(num)

# print(array)
# print("output=",array[-1]-array[0])



def prime_list(value):

    for i in range(value):
        i+=1
        
        num=i
        if num<=2:
            None
            
        elif (num%2==1):
            result.append(num)
            finalresult= result[-1]-result[0]
    return finalresult


result=[]
result.sort()

print(prime_list(50))