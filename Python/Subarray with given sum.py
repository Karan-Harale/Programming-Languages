
from ast import Break
from operator import indexOf
from os import remove


def subarraySum(A , S):

    sum=0

    for i in A:

        if sum!=S:
            sum+=i
            temp=0

            while sum>S:
                sum=sum-1
                temp+=1

                if sum==S:
                    if temp in A:
                        remove(A[i])
                        
                    return sum


A=[1,2,3,7,5]
S=12
subarraySum(A, S)
