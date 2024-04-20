def getIndex(lst,n):
    l=len(lst)
    ind=0
    output=0

    for i in range(l):

        if lst[i]==n:
            ind+=1
            if(ind==2):
                output=i
                break

        else:
            output=0
    return output


t=int(input("Total Number of Elements in list: "))
lse=[]

for i in range(t):
    lse.append(int(input()))

es=int(input("Enter Number: "))

print(lse,"\n",es)

print("Output: ",getIndex(lse,es))




