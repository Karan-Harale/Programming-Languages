inputt=input('string: ').split()
print(inputt)

for i in range(0, len(inputt)):
    inputt[i]=int(inputt[i])

inputt.sort()

add=inputt[-1]+inputt[-2]
print(add)

