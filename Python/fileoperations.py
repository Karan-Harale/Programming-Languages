
# f=open("file1.txt","a")
#
# for i in range(10):
#     f.write("This is appended line number %d\r\n"%i)
# f.close()
#
# r=open("file1.txt","r")
# c=r.read()
# print(c)
# r.close()


r=open("file1.txt","r")
for c in r:
    print("extracted:- ",c)
r.close() 