"""
@author Zach Stoebner
@date 10-22-2019
@descrip You are given an array of length n + 1 whose elements belong to the
set {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate.
Find it in linear time and space.
"""
### This solution may actually require the bit technique to rotate through the array to find the duplicate.
# I can't remember how to do this off the top of my head though.

# PHP
# Returns the duplicate element in the array
# Complexity: O(n) time and space
def PHP(arr=list()):

    lookup = dict() # O(n) space
    for elem in arr: #O(n) time
        if lookup.get(elem) == None: #O(1) time
            lookup[elem] = 1
        else:
            return elem

    raise Exception("Invalid array")

### TESTS
test1 = [1,2,3,4,4]
print(PHP(test1)) #4

# Witty way to do it: https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

def php1(arr=list()):

    l = len(arr)

    for i in range(l):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            return abs(arr[i])

    raise Exception("Invalid array")

print(php1(test1)) #4
