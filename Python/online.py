# textip=input()
# count=0
# arr=['1','2','3','4','5','6','7','8','9','0']

# for i in arr :
#     if i in textip:
#         count+=1

# print(count)

li=[]
num=int(input())
year=input().split()
thereshold=int(input())
count=0
maps=map(int, year)
print(maps)

for i in maps:
    li.append(i)

for i in li:
    if thereshold%i==0:
        count+=1

print(count)
