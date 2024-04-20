import array
from numpy import *

arr1=array([

    [1,2,3,6,2,9],
    [4,5,6,7,5,3]
])

arr2=arr1.flatten()

arr3=arr2.reshape(4,3)   #changing 2 dimensional array to multi dimensional array (rows,columns)
print(arr3)


arr4=arr2.reshape(2,2,3) #changing 2 dimensional array to multi dimensional array (rows,columns , elements)
print(arr4)