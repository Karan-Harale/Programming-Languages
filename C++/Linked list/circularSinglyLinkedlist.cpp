#include <iostream>
using namespace std;

class Node
{
public:
    int data;

    Node *next = NULL;

    Node(int data)
    {

        this->data = data;

        this->next = NULL;
    }
};

void insertatHead(Node *&head, Node *&tail, int data)
{

    if (head == NULL)
    {
        Node *currentnode = new Node(data);

        head = currentnode;
        tail = currentnode;
    }
    else
    {

        Node *currentnode = new Node(data);

        currentnode->next = head;

        head = currentnode;
    }
}

void insertatTail(Node *&head, Node *&tail, int data)
{
    if (tail == NULL)
    {
        Node *currentnode = new Node(data);

        head = currentnode;
        tail = currentnode;
    }
    else
    {
        Node *currentnode = new Node(data);

        tail->next = currentnode;
        tail = tail->next;
    }
}

void inserAtPosition(Node *&head, Node *&tail, int position, int data)
{

    if (position == 1)
    {
        insertatHead(head, tail, data);

        return;
    }
    else
    {
        int nodecount = 1;
        Node *currentnode = head;

        while (nodecount < (position - 1))
        {
            currentnode = currentnode->next;
            nodecount++;
        }

        Node *newnode = new Node(data);

        newnode->next = currentnode->next;

        currentnode->next = newnode;
    }
}

void print(Node *&head, Node *&headadd)
{
    Node *currentnode = head;

    int nodecount = 0;

    while (currentnode != NULL)
    {
        nodecount++;

        if (nodecount == 1)
        {
            headadd = currentnode;

            cout << "currentnode : " << currentnode << endl;

            cout << "headadd : " << headadd << endl;
        }

        cout << currentnode->data << " ";

        currentnode = currentnode->next;
    }

    cout << endl;
}

int main()
{

    // Node* node = new Node(1);

    Node *head = NULL;

    Node *tail = NULL;

    Node *headadd = NULL;

    insertatHead(head, tail, 1);

    insertatTail(head, tail, 3);
    insertatTail(head, tail, 4);
    insertatTail(head, tail, 5);
    inserAtPosition(head, tail, 1, 3);
    inserAtPosition(head, tail, 5, 10);
    insertatTail(head, tail, 15);

    // cout<<"1st head : "<<head<<endl;

    print(head, headadd);

     cout << "\nLength of linkedlist = " << getlength(head) << endl;


    cout << "Head->data : " << head->data << endl;

    cout << "Tail->data: " << tail->data << endl;

    if (tail->next == NULL)
    {

        tail->next = headadd;
    }
    cout << "Tail -> next : " << tail->next->data << endl;

    return 0;
}
