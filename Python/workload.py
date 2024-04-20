def min_time(N,work):

    def getp(array,val):
        valuep=0
        for i in range(len(array)):
            value=abs(array[i]-i+1-val)
            valuep+=value
        return valuep

    
    lowerval=0
    higherval=1000000000

    finalval=float("inf")


    while lowerval<=higherval:


        mval=lowerval+(higherval-lowerval)//2

        val1=(getp(work,mval))
        val2=(getp(work,mval+1))

        finalval=(min(finalval, val1,val2))
        print(finalval," ",val1," ",val2)

        if(val1<=val2):
            higherval=mval-1
        else:
            lowerval=mval+2
        return finalval


# N=int(input())
# work=list(map(int, input().split()))
N=6
work=[4,2,5,3,5,1]
print(N)
print(work)

out=min_time(N,work)

print (out)
