#include <iostream>
using namespace std;

class Node
{
public:
    int data;

    Node *addofnextnode;

    Node(int data)
    {

        this->data = data;

        this->addofnextnode = NULL;
    }

    ~Node()
    {
        int value = this->data;

        if (this->addofnextnode != NULL)
        {
            this->addofnextnode = NULL;

            delete this->addofnextnode;
        }
        cout << "\ndeleted node is " << value << "\n"
             << endl;
    }
};

void insertAtHead(Node *&head, int nextnodedata)
{

    Node *current_Node = new Node(nextnodedata);

    current_Node->addofnextnode = head;

    head = current_Node;

    // cout<<"nextheadnode = "<<current_Node->data<<endl;
    //  cout<<"addnextheadnode = "<<current_Node->addofnextnode;
}

void insertAtEnd(Node *&tail, int nextnodedata)
{

    Node *current_Node = new Node(nextnodedata);

    tail->addofnextnode = current_Node;

    tail = tail->addofnextnode;
}

void middlenode(Node *&head, Node *&tail, int position, int nextnodedata)
{

    if (position == 1)
    {
        insertAtHead(head, nextnodedata);
        return;
    }

    if (tail->addofnextnode == NULL)
    {
        insertAtEnd(tail, nextnodedata);
        return;
    }

    Node *current_Node = head;

    int nodecount = 1;

    while (nodecount < position - 1)
    {
        current_Node = current_Node->addofnextnode;

        nodecount++;
    }

    Node *middlenode = new Node(nextnodedata);

    middlenode->addofnextnode = current_Node->addofnextnode;

    current_Node->addofnextnode = middlenode;
}

void deletenodebyposition(Node *&head, int position)

{

    if (position == 1)

    {
        Node *current_node = head;

        head = head->addofnextnode;

        current_node->addofnextnode = NULL;

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

            current_node = current_node->addofnextnode;
            nodecount++;
        }

        prev_node->addofnextnode = current_node->addofnextnode;

        current_node->addofnextnode = NULL;

        delete current_node;
    }
}

void deletenodeByValue(Node *&head, int value)
{

    if (head->data == value)
    {

        Node *temp = head;
        head = head->addofnextnode;

        temp->addofnextnode = NULL;

        delete temp;
    }

    else
    {

        Node* current_node = head;

        Node *prev_node = NULL;


        cout << "c" << current_node->data << endl;

        cout << "h" << head->data << endl;

        while ((current_node->data) != value)
        {
            prev_node = current_node;

            current_node = current_node->addofnextnode;

            cout <<"current Node Value As we traversing from start to end = " << current_node->data << endl;
 
        }

        prev_node->addofnextnode = current_node->addofnextnode;

        current_node->addofnextnode = NULL;

        delete current_node;
    }
    
}

void print(Node *&head)
{

    Node *current_Node = head;

    while (current_Node != NULL)
    {

        cout << current_Node->data << "   ";
        cout << current_Node->addofnextnode << endl;

        current_Node = current_Node->addofnextnode;
    }
}

int main()
{

    Node *firstnode = new Node(10);

    // cout<<firstnode->data<<endl;
    // cout<<firstnode->addofnextnode<<endl;

    Node *head = firstnode;

    Node *tail = firstnode;

    // insertAtHead(head, 20);
    // insertAtHead(head, 30);
    // insertAtHead(head, 40);
    // insertAtHead(head, 50);

    insertAtEnd(tail, 20);
    insertAtEnd(tail, 30);
    insertAtEnd(tail, 40);
    insertAtEnd(tail, 50);

    middlenode(head, tail, 6, 25);

    print(head);

    deletenodebyposition(head, 1);
    deletenodeByValue(head, 25);

    print(head);


     cout <<"Head: "<<head -> data <<endl;

    cout <<"Tail: "<<tail -> data <<endl;
    return 0;
}
