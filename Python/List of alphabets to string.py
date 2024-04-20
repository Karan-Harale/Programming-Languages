
from re import I


def list_to_string(N, ch):
    new=""
    for i in ch:
        new=new+i
    return new
    


N=int (input("No. of Items In List: "))

ch=input().split()

out=list_to_string(N,ch)
print(out)