#include <iostream>
using namespace std;

class Node
{
public:
    int data;

    Node *prevadd;

    Node *nextadd;

    Node(int data)
    {
        this->data = data;

        this->prevadd = NULL;

        this->nextadd = NULL;
    }

    ~Node()
    {
        int value = this->data;

        if (nextadd != NULL)
        {
            delete this->nextadd;
            nextadd = NULL;
        }

        cout << "deleted node: " << value << endl;
    }
};

void insertAtHead(Node *&head, Node *&tail, int data)
{

    if (head == NULL)
    {
        Node *newnode = new Node(data);

        head = newnode;
        tail = newnode;
    }
    else
    {
        Node *newnode = new Node(data);

        newnode->nextadd = head;

        head->prevadd = newnode;

        head = newnode;
    }
}

void insertAtTail(Node *&head, Node *&tail, int data)
{

    if (tail == NULL)
    {

        Node *newnode = new Node(data);

        tail = newnode;
        head = newnode;
    }
    else
    {
        Node *newnode = new Node(data);

        tail->nextadd = newnode;

        newnode->prevadd = tail;

        tail = newnode; // as tails -> next = newnode we directly use newnodehead instead of  tail->nextadd
    }
}

void insertAtPosition(Node *&head, Node *&tail, int position, int data)

{

    if (position == 1)
    {
        insertAtHead(head, tail, data);
        return;
    }

    Node *currentnode = head;

    int nodecount = 1;

    while (nodecount < (position - 1))
    {

        currentnode = currentnode->nextadd;

        nodecount++;
    }

    if (currentnode->nextadd == NULL)
    {

        insertAtTail(head, tail, data);
        return;
    }

    Node *newnode = new Node(data);

    newnode->nextadd = currentnode->nextadd;

    currentnode->nextadd->prevadd = newnode;

    currentnode->nextadd = newnode;

    newnode->prevadd = currentnode;
}

void deletenodeByPosition(Node *&head, Node *&tail, int position)
{
    if (position == 1)
    {
        Node *current_node = head;

        head->prevadd = NULL;

        head = current_node->nextadd;

        current_node->nextadd = NULL;

        delete current_node;
    }
    else
    {
        Node *current_node = head;
        Node *prev_node = NULL;
        int nodecount = 1;

        while (nodecount < position)
        {
            prev_node = current_node;

            current_node = current_node->nextadd;

            nodecount++;
        }

        if (current_node->nextadd != NULL)
        {

            prev_node->nextadd = current_node->nextadd;

            current_node->nextadd->prevadd = prev_node;
            current_node->prevadd = NULL;
            current_node->nextadd = NULL;

            delete current_node;
        }
        else
        {
            prev_node->nextadd = NULL;
            tail = prev_node;
            delete current_node;
        }
    }
}

void deletenodeByValue(Node *&head, Node *&tail, int value)
{

    if (head->data == value)
    {

        Node *current_node = head;

        head->prevadd = NULL;

        head = current_node->nextadd;

        current_node->nextadd = NULL;

        delete current_node;
    }
    else
    {

        Node *current_node = head;
        Node *prev_node = NULL;
        int nodecount = 1;

        while ((current_node->data) != value)
        {
            prev_node = current_node;

            current_node = current_node->nextadd;

            nodecount++;
        }

        if (current_node->nextadd != NULL)
        {

            current_node->prevadd = NULL;

            prev_node->nextadd = current_node->nextadd;

            current_node->nextadd->prevadd = prev_node;

            current_node->nextadd = NULL;

            delete current_node;
        }
        else
        {
            prev_node->nextadd = NULL;
            tail = prev_node;
            delete current_node;
        }
    }
}

void print(Node *&head, Node *&tailnextheadadd, Node *&headprevtailadd)
{
    Node *currentnode = head;
    int nodecount = 0;


    while (currentnode != NULL)
    {

        nodecount++;

        if (nodecount == 1)
        {
            tailnextheadadd = currentnode;

            headprevtailadd = currentnode;

            cout << "1st head : " << currentnode<<"\n" << endl;
        }
        cout << currentnode->data << " ";

        currentnode = currentnode->nextadd;
    }
    cout << endl;
}

int getlength(Node *head)
{
    Node *temp = head;

    int len = 0;

    while (temp != NULL)
    {
        len++;

        temp = temp->nextadd;
    }
    return len;
}

int main()

{
    // started with Known node

    // Node *node = new Node(1);

    //  Node *head = node;

    // Node *tail = node;

    // started with null node below

    Node *head = NULL;

    Node *tail = NULL;

    Node *tailnextheadadd = NULL;

    Node *headprevtailadd = NULL;

    insertAtHead(head, tail, 2);

    insertAtHead(head, tail, 3);

    insertAtTail(head, tail, 4);

    insertAtTail(head, tail, 5);

    insertAtTail(head, tail, 12);

    insertAtPosition(head, tail, 3, 10);

    insertAtPosition(head, tail, 7, 11);

    deletenodeByPosition(head, tail, 5);

    deletenodeByPosition(head, tail, 1);

    deletenodeByValue(head, tail, 12);

    cout<<endl;

    cout<<"Linked List : ";

    print(head, tailnextheadadd, headprevtailadd);

    cout << "\nLength of linkedlist = " << getlength(head) << endl;

    cout << "headpre = " << head->prevadd << endl;

    cout << "tail = " << tail->data << endl;

    headprevtailadd->prevadd = tail;

    if (tail->nextadd == NULL)
    {

        tail->nextadd = tailnextheadadd;
    }
    cout << "Tail -> next : " << tail->nextadd ->data << endl;

 
    return 0;
}
