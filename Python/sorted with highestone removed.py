# array=list(map(int,input().split()))
#
# array.sort()
# array.remove(array[-1])
# print(array)

A=[2,4,6,8]
N=len(A)

if N%2==0 and N>2:
    r=N//2
    s=0
    for i in range(r+1):
        s=A[i]^A[i+1]
    print(s)
else:
    print(N)
