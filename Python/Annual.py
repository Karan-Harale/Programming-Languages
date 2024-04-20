n=10
arr=[1, 2, 7, 5, 7, 4, 1, 1, 2, 5]
count=0

res=[]
for i in range(n):
    for j in arr[i+1:]:
        if arr[i]>j:
            res.append((arr[i],j))
            count+=1

print(res)
print(count)