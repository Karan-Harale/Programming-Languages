def increasing_subarray(n,m,s,x,y):
    paths=[]
    for i in range(m):
        if x[i]==x[i-1]:
            paths.append(x[i])
            paths.append(y[i])
        elif x[i]>x[i-1]:
            paths.append(x[i])
            paths.append(y[i])
        
    
    paths=set(paths)
    # return paths

    svars=[]
    
    for i in paths:
        if max(paths)>n:
            return -1
        
        else:
            svars.append(s[i-1])
    
    total_counts=[]

    for i in svars:
        total_counts.append(svars.count(i))   
    
    
    if max(total_counts)<=1:
        return -1
    else:
        return max(total_counts)        


n=int(input("n: "))
m=int(input("m: "))
s=input("S: ")
x=list(map(int,input("x: ").split()))
y=list(map(int,input("y: ").split()))

print(increasing_subarray(n,m,s,x,y))
