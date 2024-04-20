def linearSearch(arr , n, num):

    for i in range(n):

        if arr[i] == num:
            return i



arr = [15, 45, 67, 42, 30, 16]

l =len(arr)

print(linearSearch(arr, l , 42))