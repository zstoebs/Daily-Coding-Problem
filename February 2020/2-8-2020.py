"""
@author Zach Stoebner
@date 2-8-2020
@details A fixed point in an array is an element whose value is equal to its index.
Given a sorted array of distinct elements, return a fixed point, if one exists.
Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8],
you should return False.
"""

def has_fixed_point(arr: list):

    for i, num in enumerate(arr):
        if num == i:
            return True

    return False


### TESTS
print(has_fixed_point([-6,0,2,40]))
print(has_fixed_point([1,5,7,8]))
