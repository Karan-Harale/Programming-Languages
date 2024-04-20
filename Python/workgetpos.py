def getp(array,val):
    valuep=0

    for i in range(len(array)):
        value=abs(array[i]-i+1-val)
        valuep+=value
        print(array[i]," ",i," ",value," ",valuep)


def getpi(array,val):
    valuep=0

    for i in range(len(array)):
        value=abs(array[i]-i+1-val)
        valuep+=value
        print(array[i]," ",i," ",value," ",valuep)

mval=500000000

work=[4,2,5,3,5,1]

print(getp(work,mval))

print(getp(work,mval+1))

                   
