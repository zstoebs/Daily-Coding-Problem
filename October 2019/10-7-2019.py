"""
@author Zach Stoebner
@date 10-7-2019
@descrip Given a list of numbers L, implement a method sum(i, j)
which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return
sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should
be optimized over the pre-processing step.
"""

def sum(L,i,j):

    sum = 0
    for ind in range(i,j):
        sum += L[ind]

    return sum

### TESTS
L = [1,2,3,4,5]
print(sum(L,1,3)) #5
# I'm probably missing something here b/c DCP classified this problem as hard.
# But it appears extraordinarily easy.

### ADMIN SOLUTION

# Apparently they were referencing a segment tree which I completely didn't pick up on from the problem description.
class Node:
    def __init__(self, val, start_ind, end_ind, left=None, right=None):
        self.val = val
        self.start_ind = start_ind
        self.end_ind = end_ind
        self.left = left
        self.right = right

    @property
    def interval(self):
        return (self.start_ind, self.end_ind)


def make_segment_tree(lst):
    return _make_segment_tree(lst, 0, len(lst) - 1)


def _make_segment_tree(lst, start_ind, end_ind):
    if start_ind == end_ind:
        assert(len(lst) == 1)
        val = lst[0]
        return Node(val, start_ind, end_ind)

    mid = len(lst) // 2

    left = _make_segment_tree(lst[:mid], start_ind, start_ind + mid - 1)
    right = _make_segment_tree(lst[mid:], start_ind + mid, end_ind)

    root_val = left.val + right.val

    return Node(root_val, start_ind, end_ind, left, right)

def query(node, start_ind, end_ind):
    if node.start_ind == start_ind and node.end_ind == end_ind:
        return node.val

    result = 0
    left = node.left
    right = node.right

    if left.start_ind <= start_ind <= left.end_ind:
        result += query(left, start_ind, min(end_ind, left.end_ind))

    if right.start_ind <= end_ind <= right.end_ind:
        result += query(right, max(start_ind, right.start_ind), end_ind)

    return result
#This takes O(N log N) time and space during pre-processing while querying takes O(log N) time.
