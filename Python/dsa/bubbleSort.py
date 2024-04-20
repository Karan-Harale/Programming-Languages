

def bubbleSort(arr):

    l = len(arr)


    for i in range(l):
        for j in range(i, l-1):

            if arr[j] > arr[j+1]:

                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


        # print(arr[i])
    return arr



arr = [5, 3, 8, 4, 6]

print(bubbleSort(arr))