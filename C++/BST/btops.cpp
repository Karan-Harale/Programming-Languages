#include <iostream>

#include <queue>

using namespace std;

class node
{

public:
    int data;

    node *left;

    node *right;

    node(int d)
    {
        this->data = d;

        this->left = NULL;

        this->right = NULL;
    }
};

node *makeTree(node *&root)
{
    int parent;
    cout << "Enter node data: ";

    cin >> parent;

    root = new node(parent);

    if (parent == -1)
    {
        return NULL;
    }

    cout << "enter Child at left of " << parent << endl;

    root->left = makeTree(root->left);

    cout << "enter Child at right of " << parent << endl;

    root->right = makeTree(root->right);

    // cout << "\n"
    //      << root << endl;

    return root;
}

void levelorderTraversal(node *root) // levelorderTraversal is also nown as depth first search is
{

    // {// method 1 : from here bbelow this gives us thw queue of nodes but if we want to see tree structure we can use method 2 below this method
    //     queue<node *> q;

    //     q.push(root);

    //     cout << "root: " << root << endl;
    //     cout<<root ->data<<endl;
    //     cout << "roots: " << root << endl;

    //     while (!q.empty())
    //     {
    //         node *temp = q.front();

    //         cout << temp ->data << " ";

    //         q.pop();

    //         if (temp->left != NULL)
    //         {
    //             q.push(temp->left);
    //         }

    //         if (temp->right != NULL)
    //         {
    //             q.push(temp->right);
    //         }
    //     }
    // }

    // Method 2:

    queue<node *> q;

    q.push(root);

    q.push(NULL);

    // cout << "root: " << root << endl;

    int levelcount = 1;

    while (!q.empty())
    {

        node *temp = q.front();

        q.pop();

        if (temp == NULL)
        {

            cout << "            Level : " << levelcount << endl;

            levelcount++;

            if (!q.empty())
            {
                q.push(NULL);
            }
        }
        else
        {

            cout << " " << temp->data << " ";

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

void inorder(node *root)
{

    if (root == NULL)
    {
        return;
    }

    inorder(root->left); // left

    cout << root->data << " "; // root

    inorder(root->right); // right
}

void preorder(node *root)
{

    if (root == NULL)
    {
        return;
    }

    cout << root->data << " "; // root

    preorder(root->left); // left

    preorder(root->right); // right
}

void postorder(node *root)
{

    if (root == NULL)
    {
        return;
    }

    postorder(root->left); // left

    postorder(root->right); // right

    cout << root->data << " "; // root
}




void treeByLevel(node *&root) // this function creates nodes without using recursion
{
    queue<node *> q;

    cout << "Enter data for root node : ";

    int rootnode;

    cin >> rootnode;

    root = new node(rootnode);

    q.push(root);

    // cout << "root " << root << endl;

    // cout << "root - data " << root->data << endl;

    while (!q.empty())
    {
        node *temp = q.front();

        q.pop();

        cout << "\nEnter left node for " << temp->data << endl;

        int leftnode;
        cin >> leftnode;

        if (leftnode != -1)
        {
            temp->left = new node(leftnode);

            q.push(temp->left);
        }

        cout << "\nEnter right node  for " << temp->data << endl;

        int rightnode;
        cin >> rightnode;
        if (rightnode != -1)
        {
            temp->right = new node(rightnode);

            q.push(temp->right);
        }
    }
}


void leafs(node *root , int &leafcount)
{

    if (root == NULL)
    {
        return;
    }

    leafs(root ->left , leafcount);//give counts of left sifde leafs



    if (root ->left == NULL && root ->right == NULL) 
    {
        leafcount++;
    }
 
    leafs(root->right,  leafcount); // give counts of right sifde leafs
}



// 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1   1 2 3 -1 -1 -1 -1 -1 -1
int main()
{

    node *root = NULL;

    // makeTree(root);

    //   treeByLevel(root);
    // cout << "\nprinting Queue : \n";
    //  levelorderTraversal(root) ;


    // cout<<"\ninorder = ";
    // inorder(root);

    // cout<<"\npreorder = ";
    // preorder(root);

    // cout<<"\npostorder = ";
    // postorder(root);

    treeByLevel(root);
    // cout << "\nprinting Queue : \n";
    //  levelorderTraversal(root) ;


int leafcount = 0;
    leafs(root, leafcount );


cout<<"leafcount: "<<leafcount<<endl;
    return 0;
}
