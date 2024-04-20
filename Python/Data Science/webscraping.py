import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from urllib.request import  urlopen
from bs4 import BeautifulSoup
import re

url="https://www.hubertiming.com/results/2018MLK"
html=urlopen(url)

soup=BeautifulSoup(html)

title=soup.title()
print(title)

data=[]
allrows=soup.find_all("tr")
print(allrows[:5])

for row in allrows:
    rowlist=row.find_all("td")
    datarow=[]

    for cell in rowlist:
        datarow.append(cell.text)
        data.append(datarow)
# print(data[0])

df=pd.DataFrame(data)
print(df)
count=0
colhead=soup.find_all('th')
for colname in colhead:
    count+=1
    print(colname)
print(count)
print(df.shape)

df2=df.dropna(how ='any')
print(df2.shape)


