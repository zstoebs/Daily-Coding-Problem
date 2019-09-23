"""
@author Zach Stoebner
@date   9-23-2019
@descrip Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""

class Node:

    def __init__ (self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def min_path_sum(node):

    sum = node.data
    if node.left == None and node.right == None:
        return sum

    left_sum = 0
    if node.left != None:
        left_sum = min_path_sum(node.left)

    right_sum = 0
    if node.right != None:
        right_sum = min_path_sum(node.right)

    sum += min([left_sum,right_sum])
    return sum

### TESTS
tree = Node(10,Node(5,right=Node(2)),Node(5,right=Node(1,left=Node(-1))))
print(min_path_sum(tree)) #15
