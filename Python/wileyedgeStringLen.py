# def fun(st):
#     lis = st.split()
#
#     return len(lis[-1])
#
#
# s = "Hello World"
#
# print(fun(s))



# lista = list(map(int, input().split()))
# listb = list(map(int, input().split()))
#
# listaset = set(lista)
# listbset = set(listb)
# listA = list(listaset.union(listbset))
#
# listB = list(listaset.intersection(listbset))
#
# print(list(listA))
# print(list(listB))





# def findnearestitem(totalitems, itemids, targetid):
#     low = 0
#     high = totalitems - 1
#     nearestid = -1
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         if itemids[mid] <= targetid:
#             nearestid = itemids[mid]
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     if nearestid != -1:
#         print(f"The closest item ID less than or equal to {targetid} is {nearestid}.")
#     else:
#         print(f"No closest item with an ID less than or equal to {targetid} exists in the warehouse.")
#
#
# totalitems = int(input())
#
# itemids = list(map(int, input().split()))
#
# targetid = int(input())
#
# findnearestitem(totalitems, itemids, targetid)
#

# i = 10
#
# count = 0
# for j in range (1, i-1):
#     for k in range(1,i-1):
#         sum = (j*j)+(k*k)
#
#         if sum  == i:
#             count += 1
#
#             print(j, k)
# print("count: ", count)



