def check(cls,input1,input2):

    if len(input1)==len(input2):
        check = all(item in input1 for item in input2)
        if check==True:
            print("yes")
        else:
            print("no")
    else:
        print("no")


input1=input()
input2=input()

check(0,input1,input2)