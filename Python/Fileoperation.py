import re
k=re.search('lo','hello')
print(k)

f=open("mytxt.txt","w")
f.write("Namaste Duniya")


f=open("python.txt","r+")
strs=f.read()
print(strs)
f.write("hello python")
f.close
import os
os.rename("hello.txt","python.txt")

import mysql.connector
mysql.connector.connect(host='localhost',database='mysql',user='root',password='your pass')
