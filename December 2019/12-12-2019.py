"""
@author Zach Stoebner
@date 12-12-2019
@descrip The horizontal distance of a binary tree node describes how far left or
right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

The horizontal distance of the root is 0.
The horizontal distance of a left child is hd(parent) - 1.
The horizontal distance of a right child is hd(parent) + 1.
For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8
The bottom view of a tree, then, consists of the lowest node at each horizontal
distance. If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].

Given the root to a binary tree, return its bottom view.
"""

class Node:

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

# bottom_view
# Returns the bottom view of a tree
# Complexity: O(V+E)
def bottom_view(tree):

    levels = dict()

    # traverses the tree and adds the node to the dictionary --> the bottom-most node at the level will be at the end of the list
    def traverse(node,hd=0):
        nonlocal levels

        if hd in levels.keys():
            levels[hd].append(node.data)
        else:
            levels[hd] = list([node.data])

        if node.left != None:
            traverse(node.left,hd-1)
        if node.right != None:
            traverse(node.right,hd+1)

    # traversing the tree
    traverse(tree)

    ret = []
    for level in levels.values():
        ret.append(level[-1])

    ret.sort()
    return ret

### TESTS
"""
             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8
 """
t1 = Node(5,Node(3,Node(1,Node(0)),Node(4)),Node(7,Node(6),Node(9,Node(8))))
print(bottom_view(t1)) # [0, 1, 3, 6, 8, 9]
