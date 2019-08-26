"""
Author: Zach Stoebner
Created on: 8-26-2019
Descrip:

Print the nodes in a binary tree level-wise.
For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5

"""

 ### NODE CLASSES FROM 8-8-2019.PY
class Node(object):

    #constructor
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

#level_wise_print
#Note: prints the pre-order level wise schema of a BST
#Complexity:
def level_wise_print(root_node):

    def print_children(node):

        if node.left != None:
            print(node.left.data)
        if node.right != None:
            print(node.right.data)

    def helper(nodes=list([])):

        if len(nodes) == 0:
            return

        next_list = list([])
        for node in nodes:
            print_children(node)
            if node.left != None:
                next_list.append(node.left)
            if node.right != None:
                next_list.append(node.right)

        helper(next_list)

    print(root_node.data)
    helper(list([root_node]))

### TESTS
tree = Node(1,Node(2),Node(3,Node(4),Node(5)))
level_wise_print(tree) #1,2,3,4,5
print()

"""

   1
  /
 2
/ \
3  4
"""
tree = Node(1,Node(2,Node(3),Node(4)))
level_wise_print(tree) #1,2,3,4
print()

tree = Node(1,Node(2,right=Node(4,right=Node(5))))
level_wise_print(tree) #1,2,4,5
