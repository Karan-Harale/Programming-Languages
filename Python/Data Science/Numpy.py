import numpy as np
import sys
import time

a=np.array([1,2,3,4])

print(type(a))

b=range(1000)
print("Normal: ", sys.getsizeof(5)*len(b))  #gives size which an integer holds

c=np.arange(1000)
print("Numpy: ", c.size*c.itemsize)# it also gives the size of an integer but we can see the difference of
                                    # both which determines that the numpy array is faster,convinient and took less memory than normal python list
print(a.shape, a.size ,a.ndim ,a.itemsize)

print(np.char.add(['hii '],['karan']))# gives concatination result

print(np.char.multiply(['hii '],3))#gives multiple strings ine.g. gives 3 hii's

print(np.char.index("karan","a"))

print(np.char.center("Welcome",20,fillchar="*"))

print(np.char.join(['','',''],['dd','mm','yy']))

print(np.char.strip(['karan','rahul','arjun'],'a'))