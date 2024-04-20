userip=int(input())
cp=userip
rev=0

while(userip>0):
    rem=userip%10
    rev=(rev*10)+rem
    userip=userip//10

print(rev)

if cp==rev:
    print("number is palindrom")
else:
    print("Not Palindrome")
# print(str(userip)[::-2])  #shortcut method
