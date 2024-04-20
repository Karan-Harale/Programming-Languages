#include <iostream>
using namespace std;

class Node
{
public:
    int data;

    Node *addrofnxtnode;

    Node(int data)
    {
        this->data = data;

        this->addrofnxtnode = NULL;
    }


    ~Node()
    {
        int deletedValue = this->data;

        while (this->addrofnxtnode != NULL) 
        {
            this -> addrofnxtnode = NULL;

            delete this->addrofnxtnode;
        }

        cout <<"Deleted value: "<< deletedValue <<endl;
    }
};

void insertAtHead(Node* &head, int newnodedata)
{
    Node *newnode = new Node(newnodedata);

    newnode->addrofnxtnode = head;
    head = newnode;

    cout << "insertAtHead : " << head->data << " " << head->addrofnxtnode << endl;
}

void insertAtTail(Node* &tail, int newnodedata)

{
    Node *newnode = new Node(newnodedata);

   tail ->addrofnxtnode = newnode;

    tail = tail->addrofnxtnode;

    cout << "insertAtTail : " << tail->data << " " << tail->addrofnxtnode << endl;
}


void insertAtPositions(Node* &head, Node* &tail, int position,int newnodedata)
{




    Node* newnode = new Node(newnodedata);


    if (position == 1)
    {
        insertAtHead(head, newnodedata);
        return;
    }

    

    Node* current_node = head;

    Node* prev_node = NULL;

    int nodecount = 1;

       while(nodecount < position)
    {
        prev_node = current_node;
        current_node = current_node->addrofnxtnode;

        nodecount++;
    }
    
    newnode -> addrofnxtnode = current_node -> addrofnxtnode;
prev_node -> addrofnxtnode = newnode;

}


deleteNodebyPosition(Node* &head, Node* &tail, int position)

{

Node* firstnode = head;


if (position == 1)
{
    head = head->addrofnxtnode;

    firstnode ->addrofnxtnode = NULL;

    delete firstnode;
}
else
{

    Node* currentnode = head;

    Node* prevnode = NULL;

int nodecount = 1;

 while (nodecount < position)
 {
    prevnode = currentnode;
    currentnode = currentnode -> addrofnxtnode;
    nodecount++;
 }

 prevnode -> addrofnxtnode = currentnode -> addrofnxtnode;

 currentnode -> addrofnxtnode = NULL;


 delete currentnode;

}

if(tail ->addrofnxtnode != NULL)
{
    tail ->addrofnxtnode =NULL;

}
}







void printLinkedList(Node* &head)
{
    Node *current_node = head;

    cout << "printLinkedList : " << current_node << endl;

    while (current_node != NULL)

    {
        cout << current_node->data << " ";

        current_node = current_node->addrofnxtnode;
    }
    cout<< endl;
}



int main()
{

    Node* node1 = new Node(1); // creating new node as first node

    Node* head = node1; // creating head node to add element at head

    Node* tail = node1; // creating tail node to add element at tail of node1

    // insertAtHead(head, 2); // creating next node using insertAtHead function

    // insertAtHead(head, 3);
    // insertAtHead(head, 4);
    // insertAtHead(head, 5);

    insertAtTail(tail, 2); // creating next node using insertAtHead function

    insertAtTail(tail, 3);
    insertAtTail(tail, 4);
    insertAtTail(tail, 5);



    insertAtPositions(head, tail, 1, 6);

    

    printLinkedList(head); //


        deleteNodebyPosition(head, tail, 6);

printLinkedList(head); 

    cout <<"Head: "<<head -> data <<endl;

    cout <<"Tail: "<<tail -> addrofnxtnode <<endl;
    // cout<<head -> data <<endl;
}