# N=int(input("N= "))
# count=0
# summ=0
# for i in range(N):
#     summ+=1
#     if(summ%2==0):
#         count+=1
# print(count)


def count(N):
    summ=0
    counts=0
    for i in range(N):
        summ+=1
        if (summ%2==0):
            counts+=1
    return counts

N=int(input("N: "))
result=count(N)
print(result)