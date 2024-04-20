userip=int(input())
rev=0

while(userip>0):
    rem=userip%10
    rev=(rev*10)+rem
    userip=userip//10

print(rev)

# print(str(userip)[::-2])  #shortcut method
