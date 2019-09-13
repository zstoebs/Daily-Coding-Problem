"""
@author Zach Stoebner
@date 9-13-2019
@descrip Given the root of a binary search tree, and a target K,
          return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
"""

class Node(object):

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

#node_sum
#Note: returns the value stored in two nodes of a given tree that equal k
#Complexity:
def node_sum(root,k):

    #getting all nodes
    def get_nodes(root,nodes=list([])):

        left = root.left
        right = root.right

        if root.data <= k:
            nodes.append(root.data)

        if left == None and right == None:
            return nodes

        if left != None:
            left_tree = get_nodes(left)
            nodes.extend(left_tree)
        if right != None:
            right_tree = get_nodes(right)
            nodes.extend(right_tree)

        return nodes

    nodes = get_nodes(root)
    nodes.sort()
    ret = None
    found = False
    length = len(nodes)
    for i in range(length):
        if found:
            break

        for j in range(i+1,length):

            if nodes[i] + nodes[j] == k:
                ret = [nodes[i],nodes[j]]
                found = True

    return ret

### TESTS
tree = Node(10,Node(5),Node(15,Node(11),Node(15)))
print(node_sum(tree,20))
