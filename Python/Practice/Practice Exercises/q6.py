#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

user=str(input("Enter String : "))
user1=user[::-1]

print(user1)
if user==user1:
    print("palindrome")
else:
    print("Not Palindrome")