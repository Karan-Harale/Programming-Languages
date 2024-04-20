number=int(input("Enter Range of number : "))
evens=[]
odds=[]
ecount=0
ocount=0
for i in range(0,number+1):
    if i%2==0:
        evens.append(i)
        ecount+=1
    else:
        odds.append(i)
        ocount+=1

print(evens ," ","Count = ",ecount," ",sum(evens))
print(odds ," ","Count = ",ocount," ",sum(odds))


