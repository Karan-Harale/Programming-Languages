#
# The output of the following pseudocode for a=9, b=2 is -14.
#
# Python
# Integer funn (Integer a, Integer b)
#
# if((4&a)<(3-b) && (a^b)>(3-a))
# b=2+2+b
# b=2+1+a
# return funn (b+b, a)
# End if
# return b-a+1

# def funn ( a,  b):
#     if((4&a)<(3-b) and (a^b)>(3-a)):
#         b=2+2+b
#         b=2+1+a
#         return funn (b+b, a)
#     return b-a+1
#
# print(funn(9,2))

# ans=-14



# What will be the output of the following
# Integer a,b,c
# Set a=6, b=2, c=9
# a=a+b
# for (each c from 4 to 6)
#  a=3+c
# End for
# Print a+b
#
#
# a=6
# b=2
# c=9
# a=a+b
#
# for c in range (4,7):
#     a=3+c
# print(a+b)


# What will be the output of the following pseudo code?
# Integer p,q,r
# Set p = 8 q = 7 , r = 10
# p =(q&2)+q
# p = (p * r) + q
# r = 4 + r
# Print p + q + r
#
#
#
# p=8
# q=7
# r=10
# p=(q&2)+q
# p=(p&r)+q
# r=4+r
# print(p+q+r)



# Integer pp, qq, rr
# Set pp = 2, qq = 3 rr = 9
# qq=rr+qq
# if((p * p ^ q * q ^ r * r) < (qq + rr * 8pp))
#     pp = 2&rr
# Else
#     if(8 < rr)
#         rr = (4 ^ 1) + qq
#     Else
#         rr = (pp + 10) & rr
#     End if
#     rr = (6 + 12) + pp
# End if
# Print pp+qq+rr

# pp = 2
# qq = 3
# rr = 9
# qq=rr+qq
#
# if((pp ^ qq ^ rr) < (qq + rr&pp)):
#     pp = 2&rr
# else:
#     if(8 < rr):
#         rr = (4 ^ 1) + qq
#     else:
#         rr = (pp + 10) & rr
#
#     rr = (6 + 12) + pp
#
# print (pp+qq+rr)

# ans=34


# Integer a,b,c
#  Set a=6, b=7, c=6
#  a=(10+4)+b
#  if (8>c && (b+c) < (8-b))
#  a= (12+1)+b
#  if((b+c+a) < (a+b))
# a=(a+c)+b
# Else
# a=(5+10)^b
# End if
# Else
# b=c+b
# if((b^a^c)<(c^b))
# C=8+c
# End if
# End if
# Print a+b+c

# a=6
# b=7
# c=6
# a=(10+4)+b
# if (8>c and (b+c) < (8-b)):
#     a= (12+1)+b
#     if((b+c+a) < (a+b)):
#         a=(a+c)+b
#     else:
#         a=(5+10)^b
# else:
#     b=c+b
#     if((b^a^c)<(c^b)):
#         C=8+c
#
# print (a+b+c)
#
# ans=40


# what will be the output of the following pseudocode for a=6,b=7?
#
# integer funn(a,b):
#     if(b>a and a>3):
#         a=(b+1)+a
#         b=1+3+a
#         return a-funn(b,b)
#     return b-1
#
#
# print(funn(6,7))
#
# ans=-3


# for a=6,b=3

# def funn (a,b):
#     if((b&a)<(a-b) and a>3):
#         b=b+3
#         b=a+3
#         b=(b+1)+a
#         return funn(a+1,b)+funn(a+b,b)
#     b=1+b+b
#     return b-a
# print(funn(6,3))
#
#
# ans=37


# def funn(a,b,c):
#     for c in range(3,6):
#         if((2&a)<(b+2)):
#             continue
#         a=(c&6)+c
#         b=(c+11)+b
#     return a+b
#
# print(funn(4,2,5))
#
# ans=6

# Integer p,q,r
# p=1
# q=4
# r=6
#
# for r in range(5,10):
#     if(7<p and (4 &r)<q):
#         break
#     q=(12+4)^r
#
# print(p+q)

# Integer p,q,r
# p=9
# q=5
# r=8
# p=p+r
# for r in range(2,3):
#     if((p-q+r)<(r+p)):
#         if((r^p)<q and (q&3)<p):
#             p=r^p
# print(p+q+r)
#
# ans=24

# for a=9,b=2
# def funn(a,b):
#     if((4&a)<(3-b) and (a^b)>(3-a)):
#         b=2+2+b
#         b=2+1+a
#         return funn(b+b,a)
#     return b-a+1
#
# print(funn(9,2))

import .csv from matplotlib


act=cv.open("C:\Users\Karan\OneDrive\Downloads\book1.csv")
titlec=cv.title("book1",capitalized("Purpose","Amount"))


load.csv()
end()




