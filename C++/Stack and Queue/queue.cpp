

#include <iostream>
using namespace std;

class Queue
{

public:
    int size;

    int front;

    int rear;

    int *arr;

    Queue(int size)
    {
        this->size = size;

        front = -1;

        rear = -1;

        arr = new int[size];
    }

    void enqueue(int element)
    {

        if (rear == -1 && front == -1)
        {

            rear++;
            front++;

            arr[rear] = element;

            arr[front] = arr[rear];
            cout << arr[rear] << "  ";
        }

        else if (rear >= 0 && rear < (size - 1))
        {

            rear++;

            arr[rear] = element;
            cout << arr[rear] << "  ";
        }
        else
        {
            cout << "\n\nQueue is full!" << endl;
        }
    }

    void dequeue()
    {

        if (front >= 0 && front < (rear + 1))
        {

            cout << "\n\n"
                 << arr[front] << " is deleted!\n" << endl;

            front = front + 1;

        }
        else
        {
            cout << "\n\nQueue is Empty!" << endl;
        }
        display();

    }

    void display()
    {

        rear = front;

       while (rear >= 0 && rear < (size - 1))
        {
            cout << arr[rear] << " ";
            rear++;
        }
    }
};

int main()
{

    Queue q(6);

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.enqueue(40);
    q.enqueue(50);
    q.enqueue(60);

    // q.enqueue(40);

    q.dequeue();

    q.dequeue();
    // q.dequeue();
    // q.dequeue();
    // q.dequeue();

    // q.display();
    return 0;
}
