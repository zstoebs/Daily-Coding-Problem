"""
Author: Zach Stoebner
Created on: 8-12-2019
Descrip:

Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.

"""

###CLASSES DERIVED FROM 8-11-2019.py
class Node(object):

    #constructor
    #Note: including arg vector assumed to be children
    def __init__(self,data,*argv):
        self.data = data #assuming string type for this problem
        self.children = [] #list for tuples of children
        for arg in argv:
            self.children.append(Node(arg))

    #add
    #Note: pairs key and a node with key as data
    def add(self,key):
        self.children.append(Node(key))

    def getHeight(self):
        if len(self.children) == 0:
            return 0
        else:
            return 1 + max([child.getHeight() for child in self.children])

    def __str__(self, level=0):
        ret = "    "*(level-1)+"|---"*(level>0)+repr(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'


class Tree(object):

    #constructor
    #Note: contains root to point to least nodes
    def __init__(self,root=Node(0)):
        self.root = root

    #place
    #Note: recursively places children in appropriate node directory
    def insert(self,key,parent_val,cur_node=None):

        #setting cur to root if initial recursive iteration
        if cur_node == None:
            cur_node = self.root

        if cur_node.data == parent_val:
            cur_node.add(key)
            return True
        elif len(cur_node.children) == 0:
            return False
        else:
            for child in cur_node.children:
                if self.insert(key,parent_val,child):
                    return True
            return False

    #getHeight
    #Note: returns int height of tree
    def getHeight(self):

        return self.root.getHeight()

    def __str__(self):
        ret = self.root.__str__()
        return ret

### MY SOLUTION
#find_largest_BST
#Note: recursively finds largest BST
def find_largest_BST(root):

    def largest_BST_helper(node):
        left_valid = True
        right_valid = True

        if len(node.children) <= 2:

            for child in node.children:
                if len(node.children) > 1:
                    if child is node.children[0]:
                        left_valid = child.data <= node.data and largest_BST_helper(child)[1]
                    else:
                        right_valid = child.data >= node.data and largest_BST_helper(child)[1]
                else:
                    return largest_BST_helper(child)

            return node,(left_valid and right_valid)
        return node,False

    largest_node = None
    found_BST = False
    while not found_BST and len(root.children) > 0:
        largest_node,found_BST = largest_BST_helper(root)
        if not found_BST:
            for child in root.children:
                tmp_node,tmp_bool = find_largest_BST(child)
                if tmp_bool:
                    largets_node, found_BST = tmp_node,tmp_bool
                    break
    return largest_node,found_BST

###TESTS

#whole tree is BST
tree = Tree(root=Node(1))
tree.insert(0,1)
tree.insert(2,1)
tree.insert(2,2)
tree.insert(3,2)
node,found = find_largest_BST(tree.root)
print(found)
print(tree.getHeight())
print(node.getHeight())

#has BST subtree
tree2 = Tree(root=Node(1))
tree2.insert(2,1)
tree2.insert(0,1)
tree2.insert(3,0)
tree2.insert(2,3)
tree2.insert(4,3)
tree2.insert(5,4)
tree2.insert(6,5)
node2,found2 = find_largest_BST(tree2.root)
print(found2)
print(tree2.getHeight())
print(node2.getHeight())

#no BSTs
#infinite loop?
tree3 = Tree(root=Node(1))
tree3.insert(3,1)
tree3.insert(0,1)
node3,found3 = find_largest_BST(tree3.root)
print(found3)
print(tree3.getHeight())
print(node3.getHeight())

###ADMIN SOLUTION
def largest_bst_subtree(root):
    max_size = 0
    max_root = None
    def helper(root):
        # Returns a tuple of (size, min_key, max_key) of the subtree.
        nonlocal max_size
        nonlocal max_root
        if root is None:
            return (0, float('inf'), float('-inf'))
        left = helper(root.left)
        right = helper(root.right)
        if root.key > left[2] and root.key < right[1]:
            size = left[0] + right[0] + 1
            if size > max_size:
                max_size = size
                max_root = root
            return (size, min(root.key, left[1]), max(root.key, right[2]))
        else:
            return (0, float('-inf'), float('inf'))

    helper(root)
    return max_root
