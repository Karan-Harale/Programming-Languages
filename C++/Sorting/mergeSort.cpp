#include <iostream>
using namespace std;

void merge(int *arr, int start, int mid, int end)
{

    int len1 = mid - start + 1;

    int len2 = end - mid;

    int *first = new int[len1];

    int *second = new int[len2];

    int startindex = start;

    cout << "*****" << endl;

    for (int i = 0; i < len1; i++)
    {
        first[i] = arr[startindex++];
        cout << "first [" << i << "] :" << first[i] << endl;
    }

    cout << endl;

    startindex = mid + 1;

    for (int i = 0; i < len2; i++)
    {
        second[i] = arr[startindex++];
        cout << "second [" << i << "] :" << second[i] << endl;
    }
    cout << "*****" << endl;

    cout << endl;

    int index1 = 0;

    int index2 = 0;

    int main = start;

    while (index1 < len1 && index2 < len2)
    {

        if (first[index1] < second[index2])
        {
            arr[main++] = first[index1++];
        }
        else
        {
            arr[main++] = second[index2++];
        }
    }

    while (index1 < len1)
    {

        arr[main++] = first[index1++];
    }

    while (index2 < len2)
    {

        arr[main++] = second[index2++];
    }
}

void mergeSort(int *arr, int start, int end)

{

    if (start >= end)
    {
        return;
    }

    int mid = (start + end) / 2;

    mergeSort(arr, start, mid);

    mergeSort(arr, mid + 1, end);

    // cout<<"mid: "<<mid<<endl;

    merge(arr, start, mid, end);
}

int main()
{

    // int arr[10] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};

    int arr[7] = {38, 27, 43, 3, 9, 82, 10};

    int start = 0;

    int n = 7;

    int end = n - 1;

    mergeSort(arr, start, end);

    cout << "final result: " << endl;

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }

    cout << endl;
    return 0;
}
