def binarySearch(arr,  l, n):

    start = 0

    end = l-1

    mid = start + (end - start)//2

    while (start <= end):


        if arr[mid] == n:
            return mid

        if(n > arr[mid]):

            start = mid + 1

        if (n < arr[mid]):

            end = mid-1

        mid = start + (end - start) // 2

    return -1







arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

length = len(arr)

print( "Index: " ,binarySearch(arr, length , 2))