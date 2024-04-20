#include <iostream>
using namespace std;

void insertionSort(int *arr, int n)
{

    cout << "4, 3, 2, 10, 12, 1, 5, 6" << endl;
 
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < (n - 1); j++)
        {

            if (arr[j + 1] < arr[j])
            {
                swap(arr[j], arr[j + 1]);
                
             }
        }
    }

 }

int main()
{

    int arr[8] = {4, 3, 2, 10, 12, 1, 5, 6};

    int n = 8;

    insertionSort(arr, n);

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
}
