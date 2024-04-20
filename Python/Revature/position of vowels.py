inputt=input()

k=1
li=['a','e','i','o','u']
for i in inputt:
    for j in li:
        if (i==j):
            print(k)
            break
    k+=1
