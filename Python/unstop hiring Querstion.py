
# Q4 Ans

# a=[2,3,4,7,8]
# arr=[]
# arr2=[]
# s=1
# n=(len(a)-1)
# for i in range(n):
#     s=a[i]*s
#     arr.append(s)

# arr.remove(arr[0])


# s=a[n]*a[n-1]
# arr.append(s)

# print(arr)



# sparse matrix

# mat=[[1,2,0],[0,0,0],[7,0,9]]

# lists=[]

# for i in mat:
#     for j in i:
#         lists.append(j)
#     print(i)


# noz=lists.count(0)
# noe=len(lists)
# diff=noe-noz

# print(diff)

# print(lists)

# if noz>diff:
#     print("Sparse Matrix")
# else:
#     print("Non Sparse Matrix")

# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9]
#    ]
# b=[[],[],[]]

# lists=[]
# nl=[]

# for i in a:
#     for j in i:
#         lists.append(j)
#     print(i)

# print(lists)


# nl.insert(0, lists[6])
# nl.insert(0, lists[3])
# nl.insert(0, lists[0])

# nl.insert(0, lists[7])
# nl.insert(0, lists[4])
# nl.insert(0, lists[1])

# nl.insert(0, lists[8])
# nl.insert(0, lists[5])
# nl.insert(0, lists[2])

# f=" "

# for i in nl:
#     f=f+" "+str(i)

# print(f)

# Python3 program for rearrange an
# array such that arr[i] = i.

# Function to rearrange an array
# such that arr[i] = i.


# def solve(A):
#     s=set()
#     for i in range(len(A)):
#         s.add(A[i])
#     print(s)
    
#     for i in range(len(A)):
#         if i in s:
#             A[i]= i
#         else:
#             A[i]= -1
#     return A

	
# # Driver code
# A = [1,2,3,4,8,6]

# print(solve(A))

