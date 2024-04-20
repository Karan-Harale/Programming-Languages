# happy Number

x=int(input())
Ei=[]
for N in range(0, x+1):
    if N%2==0:
        Ei.append(N)
        print(Ei)

        if Ei==x:
            break
    print(sum(Ei))

print(len(Ei))

