#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.


num=int(input("Enter Number : "))


if (num%4==0):
    print("Number Is Divisible By 4")

elif (num%2==0):

    print("Number Is Even")
else:
     print("Number Is Odd")