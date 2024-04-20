def hcf(a,b):
    if(b == 0):
        return a
    else:
        return hcf(b,a%b)


# import math
# print(math.gcd(60,48))
print(hcf(60,48))


