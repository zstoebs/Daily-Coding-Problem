"""
Author: Zach Stoebner
Created on: 8-29-2019
Descrip:

Given a binary tree, return all paths
from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].

"""

### NODE CLASS ORIGINALLY DEFINED IN 8-8-2019.PY
class Node(object):

    #constructor
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


#################################

#all_paths
#Note: returns a list of lists with all ordered paths starting at the root
#Complexity: theta(n) time
def all_paths(tree):

    paths = list([])

    #helper
    #Note: recursively adds node data to path
    def helper(node,path=list([])):

        nonlocal paths

        path.append(node.data)

        if node.left == None and node.right == None:

            paths.append(path)

        else:

            left = path.copy()
            right = path.copy()

            if left != None:
                helper(node.left,left)
            if right != None:
                helper(node.right,right)

    helper(tree)
    return paths





### TESTS
tree = Node(1,Node(2),Node(3,Node(4),Node(5)))
print(all_paths(tree)) #[[1, 2], [1, 3, 4], [1, 3, 5]]
tree = Node(1,Node(2,Node(6),Node(7)),Node(3,Node(4),Node(5)))
print(all_paths(tree)) #[[1, 2, 6], [1, 2, 7], [1, 3, 4], [1, 3, 5]]
