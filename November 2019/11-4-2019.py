"""
@author Zach Stoebner
@date 11-4-2019
@descrip Given a linked list and a positive integer k,
rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and
k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it
should become 3 -> 4 -> 5 -> 1 -> 2.
"""

def rotate(k,LL=list()):

    for _ in range(k):
        tmp = LL.pop(-1)
        LL.insert(0,tmp)


##TESTS
l1 = [7,7,3,5]
l2 = [1,2,3,4,5]
rotate(2,l1)
rotate(3,l2)
print(l1)
print(l2)
"""
[3, 5, 7, 7]
[3, 4, 5, 1, 2]
"""
