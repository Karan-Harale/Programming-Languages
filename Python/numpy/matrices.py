from numpy import *

arr1=array([

    [1,2,3,6,2,9],
    [4,5,6,7,5,3]
])

j=arr1.flatten()   #merges multidimesion array to one dimension

m=matrix(j)   #matrix function creates new matrix using parameters
print(m)