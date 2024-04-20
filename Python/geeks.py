# while 1:
    
# Simple Interest

    # P=int(input("Principle Amount:- "))
    # R=int(input("Rate:-"))
    # T=int(input("Time:-"))
    # cal=((P*T*R)/100)
    # print("Simple Interest:- ",cal,"\n Total Payable amount= ",P+cal)

# desired Number * Pattern
    # ip=input("\n")
    # for i in ip:
    #     i=int(i)
    #     print("*"*i,end="|")

# Compound Interest
    # P=int(input("Principle Amount:- "))
    # R=float(input("Rate:- "))
    # T=int(input("Time:- "))
    # A=P*(1+(R/100))**T
    # cal=A-P
    # print("Compound Interest:- ",cal)

# Armstrong Number
# list=[]
    # ip=input()
    # length=len(ip)

    # for i in ip:
    #     i=int(i)
    #     list.append(i**length)
    # print(list)
    # sums=sum(list)
    # if sums==int(ip):
    #     print("Yes")
    # else:
    #     print("No")

# Radius Of cirle
    # r=int(input("Radius= "))
    # pi=3.14
    # print("Area of circle= ",pi*(r*r))


# fibonacci
   # list=[]
    # ip=int(input("Enter Number:- "))
    # for i in range(1,ip):
    #     if ip%i==0:
    #         print(i)
    #         list.append(i)
    # sums=sum(list)
    # if sums==ip:
    #     print(True)
    # else:
    #     print(False)


# Fabonacci Series

# def fab(n):
#     f=0
#     s=1
#     if n<0:
#         print("Incorrect")
#     elif n==0:
#         return f
#     elif n==1:
#         return s
#     else:    
#         for i in range(2,n):
#             t=f+s
#             f=s
#             s=t
#         return s
  

# print(fab(9))


import turtle as t

sc=t.Screen ()
while 1:
    t.bgcolor("black")
    t.color("red")
    t.begin_fill()
    t.circle(50.5)
    t.clone()
    t.distance(2.5)
    t.left(40)
    t.right(40)