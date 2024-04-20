
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

while True:
    x=int(input("Enter Number: "))
    print(fact(x))
