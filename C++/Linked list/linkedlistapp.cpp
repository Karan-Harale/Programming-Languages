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
        cout << tail << endl;

        Node *newnode = new Node(data);

        tail = newnode;
        head = newnode;
    }
    else
    {
        Node *newnode = new Node(data);

        tail->nextadd = newnode;

        newnode->prevadd = tail;

        tail = tail->nextadd;
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
    // Node *prevnode = NULL;

    int nodecount = 1;

    while (nodecount < (position - 1))
    {

        // prevnode = currentnode;

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

    newnode->prevadd = newnode;
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

void print(Node *&head)
{
    Node *temp = head;

    while (temp != NULL)
    {
        cout << temp->data << " ";

        temp = temp->nextadd;
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
    // Node *node = new Node(1);

    Node *head = NULL;

    Node *tail = NULL;

    int choice;
    cout << "**************************************************\n";

    cout << "Welcome to Doubly Linked list operations" << endl;

    while (1)
    {

        int input;

        cout << "\n\nNumber of nodes want to add or 99 for Options: ";
        cin >> input;

        if (input == 0)
        {
            break;
        }

        else
        {

            cout << "\nChoose operation option From below: " << endl;
            cout << "\n\t1.Insert Node at head of list\n\t2.Insert Node at tail of list\n\t3.Insert Node at nth Position of list\n\t4.Delete Node at nth Position of list\n\t5.Delete Node by value from list\n\t00.Exit\n\nChoice: ";

            cin >> choice;

            switch (choice)
            {
            case 1:

                for (int i = 1; i <= input; i++)
                {
                    int nodeip;

                    cout << "Enter node " << i << " value: ";
                    cin >> nodeip;
                    cout << endl;
                    insertAtHead(head, tail, nodeip);
                }

                print(head);
                break;

            case 2:

                for (int i = 1; i <= input; i++)
                {
                    int nodeip;

                    cout << "Enter node " << i << " value: ";
                    cin >> nodeip;
                    cout << endl;
                    insertAtTail(head, tail, nodeip);
                }

                print(head);
                break;

            case 3:

                for (int i = 1; i <= input; i++)
                {
                    int nodeip, posvalue;

                    cout << "Enter node " << i << " position: ";
                    cin >> posvalue;

                    cout << "Enter node " << i << " value: ";
                    cin >> nodeip;
                    cout << endl;
                    insertAtPosition(head, tail, posvalue, nodeip);
                }
                print(head);

                break;

            case 4:
                int posvalue;

                cout << "Enter node position to Be deleted :";
                cin >> posvalue;

                cout << endl;
                deletenodeByPosition(head, tail, posvalue);

                print(head);
                break;

            case 5:
                int nodeip;

                cout << "Enter node value to Be deleted : ";
                cin >> nodeip;
                cout << endl;
                deletenodeByPosition(head, tail, nodeip);

                break;
                print(head);

                cout << "Length of linkedlist = " << getlength(head) << endl;

                cout << "head = " << head->data << endl;

                cout << "tail = " << tail->data << endl;

            case 00:
                exit(0);
                break;

            default:
                cout << "Invalid choice" << endl;
                break;
            }
        }
    }
        return 0;
    }
