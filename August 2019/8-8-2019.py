"""
Author: Zach Stoebner
Created on: 8-8-2019
Descrip:

Determine whether a tree is a valid binary search tree.

"""
#know that BSTs are naturally recursive
#implementing a postorder check
def checkBST(tree):

    def isBST(root):
        left_valid = True
        right_valid = True

        #checking left subtree
        if root.left != None:
            left_valid = (isBST(root.left) and root.left.data <= root.data)

        #checking right subtree
        if root.right != None:
            right_valid = (isBST(root.right) and root.right.data >= root.data)

        return (left_valid and right_valid)

    return isBST(tree.root)


class Node(object):

    #constructor
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BST(object):

    #constructor
    def __init__(self,root=Node(0)):
        self.root = root

    def insert(self,node,root=None):

        #setting root
        if root == None:
            root = self.root

        #inserting node
        if (root.left == None and node.data <= root.data):
            root.left = node
        elif (root.right == None and node.data >= root.data):
            root.right = node
        else:
            if (node.data <= root.data):
                self.insert(node,root.left)
            else:
                self.insert(node,root.right)

#creating test BSTs

#valid BST
bst1 = BST()
bst1.insert(Node(-1))
bst1.insert(Node(1))
print(checkBST(bst1))
bst1.insert(Node(-3))
bst1.insert(Node(-2))
print(checkBST(bst1))

#not a BST
bad = Node(0,Node(-1,Node(6)),Node(5,Node(4),Node(4)))
badBST = BST(bad)
print(checkBST(badBST))

#unbalanced BST, still valid
unbalanced = BST()
unbalanced.insert(Node(-1))
unbalanced.insert(Node(1))
unbalanced.insert(Node(0))
print(checkBST(unbalanced))

###ADMIN SOLUTION
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_bst(root):
    def is_bst_helper(root, min_key, max_key):
        if root is None:
            return True
        if root.key <= min_key or root.key >= max_key:
            return False
        return is_bst_helper(root.left, min_key, root.key) and \
               is_bst_helper(root.right, root.key, max_key)

    return is_bst_helper(root, float('-inf'), float('inf'))
