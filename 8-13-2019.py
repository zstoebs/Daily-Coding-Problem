"""
Author: Zach Stoebner
Created on: 8-13-2019
Descrip:

Given a binary tree of integers,
find the maximum path sum between two nodes.
The path must go through at least one node,
and does not need to go through the root.

"""

# reusing BST and Node classes from 8-8-2019
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

#max_path_sum
#Note: finds the additive max sum between two nodes
def max_path_sum(bst):

    cur_sum = 0

    def max_helper(node):
        nonlocal cur_sum

        go_left = False
        if (cur_sum + node.data) >= cur_sum:
            cur_sum += node.data
            go_left = True

        if node.left != None and go_left:
            max_helper(node.left)
        if node.right != None:
            max_helper(node.right)

    max_helper(bst.root)
    return cur_sum

bst1 = BST(root=Node(1))
bst1.insert(Node(0))
bst1.insert(Node(2))
print(max_path_sum(bst1))
