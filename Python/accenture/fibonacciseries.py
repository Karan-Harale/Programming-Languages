number=int(input())

prev=0
next=1

for i in range(0,number+1):
    print(prev)

    current=prev+next
    prev=next
    next=current
