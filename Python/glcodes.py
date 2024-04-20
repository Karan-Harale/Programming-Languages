# while True:
# factorial

# def fact(x):
#     f=1
#     if x<0:
#         return print("Can't get factorial")
#     elif x==0:
#         return print("Factorial of ",x,"is=1")
#     else:
#         for i in range(2,x+1):
#             f=f*i
#         return print("Factorial of ",x,"is=",f)


# number=int(input("Enter Number:- "))

# fact(number)

#2.Fibonacci Series


# num=int(input("Enter Number="))
# f=0
# s=1
# for i in range(1,num+1):
#     n=f+s
#     f=s
#     s=n
#     print(n)


#swapping of two numbers
# num1=int(input("Enter Num1: "))
# num2=int(input("Enter Num2: "))
# temp=0

# print("num1= ",num1)
# print("num2= ",num2)

# # temp=num1
# # temp2=num2
# # num1=temp2
# # num2=temp
# num1=num1+num2
# num2=num1-num2
# num1=num1-num2


# print(num1,num2)

# # reverse string
# str=input("Enter String: ")
# print(str[::-1])

#prime numbers

    # enter=int(input())

    # for i in range(enter+1):
    #     if i%2==0:
    #         print(i,"Even Number")
    #     else:
    #         print(i,"Odd Number")
# Pattern Generator

# enter=int(input())
# Square,Rectangular

# for j in range(enter):
#         print("*"*enter)


    #triangle leftside
# for j in range(enter+1):
#         print(" "*enter)
#         print("*"*j,end=" ")
#         enter-=1

# triangle rightside
# for j in range(enter+1):
#         print(" "*enter,end=" ")
#         print("*"*j)
#         enter-=1


# midrange triangle+diamond

# k=enter
# print("      *",end=" ")

# for i in range (enter+1):
#     print(" "*k,end=" ")

#     print("*"*i,end=" ")
#     print("*"*i)
#     k-=1

# k=1
# for i in range(enter-1,0,-1):
#     print(" "*k,end=" ")
#     print("*"*i,end=" ")
#     print("*"*i)
#     k+=1
# print("      *",end=" ")





# digits 
# no_of_rows = 5
# for i in range(no_of_rows):
#     for j in range(i):
#         print(i,end=" ")
    # print('')

# k=enter
# for i in range(0,enter+1):
#     print(" "*k,end=" ")
#     print("*"*(i*2))
#     k-=1
# k=1
# for i in range(enter-1,0,-1):
#     print(" "*k,end=" ")
#     print("*"*(i*2))
#     k+=1

# import numpy as np

# a1=[[1,2,3,4],[1,2,3,4]]
# a2=[[1,2,3,4],[1,2,3,4]]
# print(dot(a1,a2))

# NUMBER PAttern

# for i in range(1,enter+1):
#     for j in range(i+1):
#         print(j,end=" ")
#     print(' ')

# for i in range(enter+1):
#     for j in range(i+1):
#         print(" "*enter,end=" ")
#         print(j,end="")
#     print(' ')
# for i in range(enter+1):
#     for j in range(i+1):
#         print(" "*enter,end=" ")
#         print(i,end="")
#     print(' ')



a=[]
b=[]

in1=input().split()

for i in in1:
    i=int(i)
    a.append(i)
print(a)

in2=input().split()

for i in in2:
    i=int(i)
    b.append(i)
print(b)

import numpy as np

print(np.dot(a,b))

