sub1=int(input("Enter Marks Of sub1 :"))
sub2=int(input("Enter Marks Of sub2 :"))
sub3=int(input("Enter Marks Of sub3 :"))

percentage=((sub1+sub2+sub3)/3)
print(percentage)


if percentage>=40:
    print("Student Passed!")

elif sub1<=33 or sub2<=33 or sub3<=33:
    print("Student Failed")
else:
    print("Student passed!")