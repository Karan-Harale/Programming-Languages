# inputt=(input()).split()
# li=[]
# if len(inputt)==3:
#     a,b,c=map(int, inputt)
#     li.append(a)
#     li.append(b)

#     li.append(c)

# li.sort()
# print(li)
# print(li[0])


# Python3 Program to find middle digit of number
import math

# Function to find the middle digit
def middleDigit(n):

	# Find total number of digits
	digits = math.log10(n) + 1;

	# Find middle digit
	n = int((n // math.pow(10, digits // 2))) % 10;

	# Return middle digit
	return n;

# Driver program

# Given Number N
N = int (input());

# Function call
print(middleDigit(N))


