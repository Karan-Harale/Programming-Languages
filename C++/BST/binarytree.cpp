#include <iostream>

#include <queue>

using namespace std;

class Node
{

public:
    int data;

    Node *left = NULL;

    Node *right = NULL;

    Node(int data)
    {

        this->data = data;
    }
};

// without recursion
void buildbinarytree(Node *&rootnode)
{

    int root;

    cout << "\nEnter data for root node: ";

    cin >> root;

    rootnode = new Node(root);

    queue<Node *> q;

    q.push(rootnode);

    while (!q.empty())
    {
        Node *temp = q.front();

        q.pop();

        cout << "\nEnter data for left node of " << temp->data << ": ";

        int leftnode;

        cin >> leftnode;

        if (leftnode != -1)
        {
            temp->left = new Node(leftnode);

            q.push(temp->left);
        }

        cout << "\nEnter data for right node of " << temp->data << ": ";
        int rightnode;

        cin >> rightnode;

        if (rightnode != -1)
        {
            temp->right = new Node(rightnode);

            q.push(temp->right);
        }
    }
}

Node *treeusingrecursion(Node *&rootnode)
{
    cout << "\nEnter Data: ";

    int data;

    cin >> data;

    rootnode = new Node(data);

    if (data == -1)
    {
        return NULL;
    }

    cout << "\nEnter data for left node of " << data << ": ";

    rootnode->left = treeusingrecursion(rootnode->left);

    cout << "\nEnter data for right node of " << data << ": ";

    rootnode->right = treeusingrecursion(rootnode->right);

    return rootnode;
}

// test case  1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1

// 1 2 4 -1 -1 5 -1 -1 3 6 -1 -1 7 -1 -1

void levelOrdertraversal(Node *root)
{
    cout << "\nroot= " << root->data <<"\n"<< endl;

    queue<Node *> q;

    q.push(root);

    q.push(NULL);

    int levelcount = 1;

    while (!q.empty())
    {
        Node *temp = q.front();

        q.pop();

        if (temp == NULL)
        {
            cout<<"     level: "<<levelcount << endl;
            levelcount++;

            if (!q.empty())
            {
                q.push(NULL);
            }
        }

        else
        {

            cout << temp->data << " ";
            if (temp->left != NULL)
            {
                q.push(temp->left);
            }

            if (temp->right != NULL)
            {
                q.push(temp->right);
            }
        }
    }
}

void inorder(Node *rootnode)
{

    if (rootnode == NULL)
    {
        return;
    }

    inorder(rootnode->left);

    cout << rootnode->data << " ";
    inorder(rootnode->right);
}

void preorder(Node *rootnode)
{

    if (rootnode == NULL)
    {
        return;
    }

    cout << rootnode->data << " ";
    preorder(rootnode->left);
    preorder(rootnode->right);
}

void postorder(Node *rootnode)
{

    if (rootnode == NULL)
    {
        return;
    }

    postorder(rootnode->left);
    postorder(rootnode->right);
    cout << rootnode->data << " ";
}

int main()
{

    Node *rootnode = NULL;

    // buildbinarytree(rootnode);

    treeusingrecursion(rootnode);

    levelOrdertraversal(rootnode);

    cout << "\n\nInorder: ";
    inorder(rootnode);

    cout << "\n\nPreorder: ";
    preorder(rootnode);

    cout << "\n\nPostorder: ";
    postorder(rootnode);

    return 0;
}
