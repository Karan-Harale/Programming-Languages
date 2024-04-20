#include <iostream>

using namespace std;

class Node
{
public:
    int data;

    Node *left;
    Node *right;

    Node(int data)
    {
        this->data = data;
    }
};

void insertleft(Node *&leftnode, int data)

{
    Node *newleft = new Node(data);

    leftnode->left = newleft;

    newleft->left = NULL;

    // cout<<leftnode-> left -> data <<endl;
}

void insertright(Node *&rightnode, int data)

{
    Node *newright = new Node(data);

    rightnode->right = newright;

    newright->right = NULL;

    // cout<<rightnode-> right -> data <<endl;
}

void display(Node *rootnode, Node *&leftnode, Node *&rightnode)
{
    Node *currentleft = leftnode;
    Node *currentright = rightnode;

    cout << currentleft->left->data << " " << rootnode->data << " " << currentright->right->data;

    currentleft = currentleft->left;

    currentright = currentright->right;
    cout << endl;
}

int main()
{

    Node *rootnode = new Node(1);

    Node *leftnode = rootnode;

    Node *rightnode = rootnode;

    insertleft(leftnode, 2);
    insertright(rightnode, 3);

    display(rootnode, leftnode, rightnode);

    insertleft(leftnode, 4);
    insertright(rightnode, 5);

    display(rootnode, leftnode, rightnode);

    return 0;
}
