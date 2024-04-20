

def selSort(arr):

    l = len(arr)
    count = 0

    for i in range(l):
        for j in range(i+1, l):

            print("i: ",arr[i], " ","j: ", arr[j])
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

                count+=1

        print(arr[i])

    return arr, count






arr = [ 40, 20, 10, 18, 22, 36]

print(selSort(arr))