#include <iostream>
using namespace std;

int binarySearch(int arr[], int size, int element)
{

    int start = 0;

    int end = size - 1;

    int mid = start + (end - start)/2 ;//((start + end) / 2); instead of this  we used start + (end - start)/2 this for large size to avoid error;

    while (start <= end)
    {

        if (arr[mid] == element)
        {
            return mid;
        }

        if (element > arr[mid])
        {
            start = mid + 1;
        }

        if (element < arr[mid])
        {
            end = end - 1;
        }

        mid = start + (end - start)/2 ;
    }

    return -1;
}

int main()
{

    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    int index = binarySearch(arr, 10, 9);

    cout << "\nIndex is : " << index << endl;

    return 0;
}
