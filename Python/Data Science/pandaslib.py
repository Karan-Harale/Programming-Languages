import pandas as pd
print(pd.__version__)

arr=[1,2,3,4]
s1=pd.Series(arr)
print(s1)


order=['a','b','c','d']
s2=pd.Series(arr,index=order)

print(s2)



import numpy as np
n=np.random.randn(4)

ind=['a','b','c','d']
s3=pd.Series(n, index=ind)
print(s3)

s1.index=s3.index
print(s1)



dates=pd.date_range('today',periods=4)
data=np.random.rand(4,4)

columns=['a','b','c','d']

df1=pd.DataFrame(data,index=dates,  columns=columns)
print(df1)

df2=df1.head(2)
df3=df1.tail(3)

print(df2)
print(df3)

df1.to_csv(('Dataframe 1.csv'))
print("below file is readed from system:")
d=pd.read_csv('Dataframe 1.csv')
print(d)





import matplotlib as mt
# number1,number2=map(int,(input("Enter Range: ").split()))
# even=[]
# odd=[]
# ecount=0
# ocount=0
# for i in range(number1,number2+1):
#     if(i%2==0):
#         even.append(i)
#         ecount+=1
#     else:
#         odd.append(i)
#         ocount+=1
#
# print("even:",even)
# print("Count:",ecount)
# print("odd :",odd)
# print("Count:",ocount)
#
