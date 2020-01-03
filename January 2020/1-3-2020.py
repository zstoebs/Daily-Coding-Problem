"""
@author Zach Stoebner
@date 1-3-2020
@details A tree is symmetric if its data and shape remain unchanged when it is reflected
about the root node. The following tree is an example:

        4
      / | \
    3   5   3
  /           \
9              9
Given a k-ary tree, determine whether it is symmetric.
"""

class Node:

    def __init__(self,data: int, k: int):
        self.data = data
        if k < 0:
            raise ValueError("k must be >= 0")
        self.k = k
        self.children = [None]*k

    def add(self,index: int, data: int):
        if index >= 0 and index < self.k:
            self.children[index] = Node(data,self.k)
        else:
            msg = "Invalid index: " + str(index)
            raise IndexError(msg)

    def remove(self,index: int):
        if index >= 0 and index < self.k:
            self.children[index] = None
        else:
            msg = "Invalid index: " + str(index)
            raise IndexError(msg)

    def get_child_data(self):
        ret = []
        for child in self.children:
            if not child is None:
                ret += child.data
            else:
                ret += None
        return ret

tree = Node(4,3)
tree.add(0,3)
tree.add(1,5)
tree.add(2,3)
left = tree.children[0]
right = tree.children[2]
left.add(0,9)
right.add(2,9)

# in-order traversal prints symmetrically
# how to handle in-order traversal on an odd k-ary tree?
# can put odd middle nodes into their own list
# can also split tree in half and compare if halves are symmetric

# is_symmetric
# Return bool if tree is symmetric
# Complexity: O(n)
def is_symmetric(tree: Node):

    odds = []
    evens = []
    k = tree.k
    is_odd = k % 2 == 1

    def helper(node: Node):
        nonlocal odds,evens,k,is_odd

        for i in range(k):
            if i == k // 2:
                evens.append(node.data)
                if is_odd:
                    if not node.children[i] is None:
                        helper(node.children[i])
                        odds.append(node.children[i].data)
                    else:
                        odds.append(None)
                    continue
            if not node.children[i] is None:
                helper(node.children[i])
            else:
                evens.append(None)

    helper(tree)
    len_odds = len(odds)
    len_evens = len(evens)

    mid = len_odds // 2
    if len_odds % 2 == 1:
        first = odds[:mid]
        second = reversed(odds[mid+1:])
        if first != second:
            return False
    else:
        first = odds[:mid]
        second = reversed(odds[mid:])
        if first != second:
            return False

    mid = len_evens // 2
    if len_evens % 2 == 1:
        first = evens[:mid]
        second = reversed(evens[mid+1:])
        if first != second:
            return False
    else:
        first = evens[:mid]
        second = reversed(evens[mid:])
        if first != second:
            return False

    return True

### TESTS
print(is_symmetric(tree))
