def stripp(li,word):
    newli=li.replace(word,"")
    return newli.strip()


li="rohan  rahul pote prabhat shubham"

s=stripp(li,"rohan")
print(li)

print(s)
