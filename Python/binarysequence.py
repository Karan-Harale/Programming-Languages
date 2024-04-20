T=int(input())
for i in range(T):
    lol=input().split()  
    print(lol)  
    if len(lol)==4:
        x,y,a,b=map(int,  lol)
        print(x,y,a,b)
        if(x*y==a+b):
            print("Yes")
        else:
            print("No")