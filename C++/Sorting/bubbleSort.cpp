#include <iostream>
using namespace std;

void bubblesort(int arr[], int size)
{
    int count = 0;
    for (int i = 1; i <= size; i++)
    {

        int j = 0;
        for (; j < size - i; j++)
        {

            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                count++;
            }
        }
        cout << arr[i-1] << " ";
        cout<<"\ncount"<<count<<endl;
    }
}

int main()
{

    int arr[5] = {5, 3, 8, 4, 6};

    int size = 5;

    bubblesort(arr, size);

    return 0;
}
