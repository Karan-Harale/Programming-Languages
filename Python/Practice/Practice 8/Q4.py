def sum(n):
    if n==0:
        return n
    return (sum(n-1)+ n)


n=int(input("Enter Number : "))
sum(n)