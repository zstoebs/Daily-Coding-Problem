"""
@author Zach Stoebner
@date 10-18-2019
@descrip Given a tree where each edge has a weight, compute the length of the longest path in the tree.

For example, given the following tree:

   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the longest path would be c -> a -> d -> f, with a length of 17.

The path does not have to pass through the root, and each node can have any amount of children.
"""

#Node class
#Supports a node w/ variable children --> can be used to a create a tree
class Node:

    def __init__(self, name, to_parent,*args):
        self.name = name
        self.to_parent = to_parent # weight to parent
        self.children = list()
        for child in args:
            self.children.append(child)

t1 = Node("a",None,Node("b",3),Node("c",5),Node("d",8,Node("e",2,Node("g",1),Node("h",1)),Node("f",4)))
#longest_path
#Returns an order list of the longest path traversal of the tree
#Complexity: O(V+E)
def longest_path(tree=Node("",None)):

    #long_paths
    #A helper fnc to traverse the tree and return a list of the longest paths
    #Must be called for each of root's children b/c requires access to to_parent
    #Complexity: O(V+E)
    def long_paths(root=Node("",None)):

        # if a leaf, return the weight to parent
        if (len(root.children) == 0):
            return root.to_parent

        # getting all paths down children and finding max path
        max_path = None
        for child in root.children:
            if max_path is None:
                max_path = long_paths(child)
            else:
                potential = long_paths(child)
                if potential > max_path:
                    max_path = potential

        max_path += root.to_parent

        return max_path

    # getting longest path for each child of the root --> this runs in O(V+E) total
    root_paths = list()
    for child in tree.children:
        root_paths.append(long_paths(child))


    num_children = len(tree.children)
    # if just a root
    if (num_children == 0):
        return 0

    # if only one child of root
    elif (num_children == 1):
        return root_paths[0]

    # if more than one child then the top two will generate the longest path b/c there are no cycles in a tree
    else:

        # this block runs in O(2n) which is in O(n) b/c just two sequential searches for the greatest and second greatest path sums
        total = 0
        mx = max(root_paths)
        total += mx
        root_paths.remove(mx)
        mx = max(root_paths)
        total += mx
        return total

### TESTS
print(longest_path(t1)) #17
