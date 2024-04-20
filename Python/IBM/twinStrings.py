
def swap_even(list1):

    finallist = []

    for i in list1:

        finalstring = ""

        evenlist = []

        for j in range(len(i)):
            if (j % 2 == 0):
                evenlist.append((j))

        # print(evenlist )


        newlist = []

        for e in i:
            newlist.append(e)

        for f in range(len(evenlist) - 1):
            temp = newlist[evenlist[f]]
            newlist[evenlist[f]] = newlist[evenlist[f + 1]]
            newlist[evenlist[f + 1]] = temp
        # print(newlist)

        for g in newlist:
            finalstring += g

        finallist.append(finalstring)

    return (finallist)


def swap_odd(list1):

    finallist= []

    for i in list1:

        finalstring = ""

        oddlist = []

        for j in range(len(i)):
            if (j%2 != 0):
                oddlist.append((j))

        # for k in range(len(oddlist)-1):
        #     temp = oddlist[k]
        #     oddlist[k] = oddlist[k+1]
        #     oddlist[k + 1] = temp

        # print(oddlist )

        newlist = []

        for e in i:
            newlist.append(e)

        for f in range(len(oddlist)-1):
            temp = newlist[oddlist[f]]
            newlist[oddlist[f]] = newlist[oddlist[f+1]]
            newlist[oddlist[f + 1]] = temp
        # print(newlist)

        for g in newlist:
            finalstring += g

        finallist.append(finalstring)

    return (finallist)


def twinString(firstString, secondString ):
    evenout=""
    oddout=""

    result = " "

    evenout = swap_even(firstString)
    oddout = swap_odd(secondString)

    for i in range(len(evenout)):
        if evenout[i] == secondString[i]:
            result = "yes"
            break

        elif oddout[i] == firstString[i]:
            result = "yes"

        elif evenout[i] == oddout[i]:
            result = "yes"
        else:
            result = "no"

    return result


firstString = ["abcd","abcd"]
secondString = ["cbad","adbc"]

# print("Even: ", swap_even(firstString,secondString))
# print("odd: ",  swap_odd(firstString,secondString))


print("output: ", twinString( firstString, secondString))

        # for j in (secondString):
        #     print(i)