# number=int(input())
# count=0
# sums=0
# for i in range(number):
#     if i%3==0 and i%2==0:
#         count+=1
#         sums+=i
#
# print(sums)
#
# avg=sums/count
#
# print(count)


def avgs(number):
    count=0
    sums=0
    for i in range(number):
        if i%3==0 and i%2==0:
            count+=1
            sums+=i

    print(sums)

    avg=sums/count
    return int(avg)


number=int(input())
print(avgs(number))
