# # Problem
# # A number  is said to be special if the sum of its digits is divisible by 4.

# # For a given integer , find a number  such that:

# #  is a special number
# #  is minimum possible
# # Input format

# # The first line contains an integer  denoting the number of test cases.
# # For each test case:
# # The first line contains an integer .
# # Output format

# # For each test case, print a number  that satisfies the above conditions in a new line.




    


T=int(input())
for i in range(T):
    a=int(input())

    sum=0
    
    for j in str(a):
        sum+=int(j)
    print(sum)
    count=0
    
    while(sum%4!=0):
        count+=1
        if(sum%4==0):
            break
    
print(count)
































# import sys
# input = sys.stdin.readline
 
# MAXN = 10000000
# def sumOfDigits(n):
#     sum = 0
#     while(n > 0):
#         sum += n % 10
#         n //= 10
#     return sum
 
# def solve(n):
#     res = -1
#     for i in range(n, MAXN):
#         s = sumOfDigits(i)
#         if s % 4 == 0:
#             return i
#     return -1   
             
# for _ in range(int(input())):
#     print(solve(int(input())))