#include <iostream>
using namespace std;


void selsort(int arr[], int size)
{
    int count = 0;

    for (int i = 0; i < size; i++)
    {
        int minindex = i;

        for (int j = i + 1; j < size; j++)
        {

            if (arr[minindex] > arr[j])
            {
                minindex = j;
            }
        }
        swap(arr[minindex], arr[i]);
        count++;

        // cout<<i<<" ";
        cout << arr[i] << " ";
    }

    cout << "\nCount: " <<count << endl;
}

int main()
{

    int arr[5] = {8, 2, 6, 1, 5};

    cout << "Sorted array : ";
    selsort(arr, 5);

    return 0;
}
