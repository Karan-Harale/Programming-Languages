# ip=int(input())
# li=[]
# for i in range(ip):
#     ips=input()
#     li.append(ips)

# print(li)

# lists=[]
# for j in li:
#     for k in li:
#         my=str(j)+str(k)
#         lists.append(my)
# print(lists)
# print(len(lists))



def cuckoo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        k1=2*cuckoo(n-2)
        return cuckoo(n-1)+k1+3

try:
    n=input()
    k=int(n)
    print(cuckoo(k))

except EOFError as e:
    print(e)