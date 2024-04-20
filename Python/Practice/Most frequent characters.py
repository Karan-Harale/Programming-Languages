
def frequent(string):
    list1={}
    for i in string:
        if i in list1:
            list1[i] = list1[i] + 1
        else:
            list1[i]=1
    result = max(list1,key = list1.get)
    print(result)



string=input()
frequent(string) 
