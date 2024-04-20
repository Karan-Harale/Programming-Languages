


class Node:

    def __init__(self, data ):

        self. data = data

        self.left = None

        self.right = None

    def insertNode(self, newnode):

        if self.data:
            if newnode < self.data:
                if self.left is None:
                    self.left = Node(newnode)
                else:
                    self.left.insertNode (newnode)

            elif newnode > self.data:
                if self.right is None:
                    self.right = Node(newnode)
                else:
                    self.right.insertNode((newnode))

        else:
            self.data = newnode


    def displaytree(self):

        print(self.data, end=" ")


        if self.left:
            self.left.displaytree()


        if self.right:
            self.right.displaytree()



    def inorder(self, root):

        res = [ ]

        if root:
            res = self.inorder(root.left)

            res.append(root.data)

            res = res + self.inorder(root.right)

        return res


    def preorder(self, root):

        res = [ ]

        if root:

            res.append(root.data)

            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)

        return res


    def postorder(self, root):

        res = [ ]

        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.data)


        return res


    def countleaf(self,root, leafcount):

        if(root == None):
            return

        res = []

        self.countleaf(root.left,leafcount)

        if(root.left == None and root.right ==None):

            leafcount+=1


        self.countleaf(root.right,leafcount)


        return leafcount





root = Node(27)

root.insertNode(14)
root.insertNode(35)
root.insertNode(10)
root.insertNode(19)
root.insertNode(31)
root.insertNode(42)



root.displaytree()

print( "\ninorder: " ,  root.inorder(root))

print( "\npreorder: " , root.preorder(root))


print( "\npostorder: " ,    root.postorder(root))


leafcount = 0
print("\nleafs: "  , (root.countleaf(root,leafcount)) )

