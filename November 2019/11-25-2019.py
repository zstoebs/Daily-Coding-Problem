"""
@author Zach Stoebner
@date 11-25-2019
@descrip Given a set of distinct positive integers, find the largest
subset such that every pair of elements in the subset (i, j) satisfies
either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20].
Given [1, 3, 6, 24], return [1, 3, 6, 24].
"""

#factor_sets
#Returns the largest subset of integers s.t. any pair is a factor of the other
#Complexity: O(n^2)
def factor_sets(arr=list()):

    n = len(arr)
    if n == 0 or n == 1:
        return arr

    #helper to check if subset satisfies factor property
    def check(i,j):
        nonlocal arr

        for e in range(i,j+1):
            for k in range(e+1,j+1):
                if not arr[e] % arr[k] == 0 and not arr[k] % arr[e] == 0:
                    return False
        return True

    mx = tuple([0,0,0])
    for i in range(n):
        for j in range(i+1,n):
            l = j - i + 1
            if check(i,j) and l > mx[0]:
                mx = tuple([l,i,j+1])
    return arr[mx[1]:mx[2]]

### TESTS
t1 = [3, 5, 10, 20, 21]
t2 = [1, 3, 6, 24]
print(factor_sets(t1))
print(factor_sets(t2))
# [5, 10, 20]
# [1, 3, 6, 24]
