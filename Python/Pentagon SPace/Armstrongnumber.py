userip=int(input())
cp=userip
length=len(str(userip))
sums=0
while(userip>0):
    rem=userip%10
    userip=userip//10
    sums+=rem**length

if cp==sums:
    print("number is Armstrong")
else:
    print("Not Armstrong")
