A=[]
Q=0
queries=[]

N=int(input())

for i in range(N):
    A.append(int(input()))
    
    for j in range(len(A)):
        if A[0]==1:
            Q=A.count(1)
        elif A[0]==0:
                break
        A=A[::-1]
    queries.append(Q)




# print (queries)

print (A)
print (Q)

print (queries)


# #Type 1 rotate the array A in clockwise direction by 1

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
import sys
s = sys.stdin.readline(4)
user_in = s.split("\n")
 
print(s)
print(user_in)
for n in user_in:
    n = n.split()
    if len(n) == 4:
        x,y,a,b = map(int,n)
        if (x*y==a+b) : 
            print ("Yes")
        else:
            print ("No")
    else:
        print("")
