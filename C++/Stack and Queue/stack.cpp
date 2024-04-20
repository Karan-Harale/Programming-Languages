#include <iostream>
using namespace std;

class Stack
{
public:
    int top;
    int size;

    int *arr;

    Stack(int size)
    {

        if (size > 0)
        {
            this->size = size;

            arr = new int[size];

            top = -1;
        }
        else
        {
            cout << "Stack is empty!" << endl;
        }
    }

    void push(int element)
    {

        if (top == -1)
        {
            top++;

            arr[top] = element;
            cout << element << " Pushed in stack " << endl;
        }

        else if (top >= 0)
        {
            top++;
            if (top < size)
            {
                arr[top] = element;

                cout << element << " Pushed in stack " << endl;
            }
            else
            {
                cout << "Stack overflow" << endl;
            }
        }
    }

    void pop()
    {
        if (top >= 0)
        {
            cout << arr[top] << " is popped " << endl;

            top--;
        }
        else
        {
            cout << "Stack is Underflow " << endl;
        }
    }


    int peek()
    {
        if(top>=0)
        {
            return arr[top];
        }
        else{
            return -1;
        }
    }
};

int main()
{

    Stack st(4);

    st.push(1);
    st.push(2);
    st.push(3);
    st.push(4);


    // st.pop();
    // st.pop();
    // st.pop();


    cout<<st.peek()<<endl;    

    return 0;
}
