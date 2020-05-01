"""
@author Zach Stoebner
@date 4-30-2020
@details You are given an array X of floating-point numbers x1, x2, ... xn. These can be rounded
up or down to create a corresponding array Y of integers y1, y2, ... yn.

Write an algorithm that finds an appropriate Y array with the following properties:

The rounded sums of both arrays should be equal.
The absolute pairwise difference between elements is minimized. In other words,
|x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.
For example, suppose your input is [1.3, 2.3, 4.4]. In this case you cannot do better than
[1, 2, 5], which has an absolute difference of |1.3 - 1| + |2.3 - 2| + |4.4 - 5| = 1.2.
"""

from math import ceil, floor, inf

# Helpful reference: https://www.geeksforgeeks.org/minimum-sum-absolute-difference-pairs-two-arrays/
# Helpful solution: https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_355.py

# diff_Y
# Computes the Y array of X s.t. 1. rounded sum of both arrays is equal and 2. absolute pairwise
# difference is minimized using a recursive search algo (complete binary tree search)
# Complexity: O(2^(N+1) - 1)
def diff_Y(arr: list):

    X = sorted(arr)
    Sum = int(round(sum(X)))
    N = len(X)

    """
    Recursive search algo:
    1. if last element and if the sum of Y is the rounded sum, found the array, else no
    2. else, take next element of X's floor and ceiling, recurse through paths as if they were
        the next element
    3. compare the absolute differences for the minimal
    """
    def helper(ind, Y, abs_diff):
        nonlocal X, Sum, N

        if ind >= N:
            return (abs_diff, Y) if int(round(sum(Y))) == Sum else (inf, None)

        xi = X[ind]

        up = int(ceil(xi))
        down = int(floor(xi))

        d1, Y1 = helper(ind+1, Y + [up], abs_diff + abs(xi - up))
        d2, Y2 = helper(ind+1, Y + [down], abs_diff + abs(xi - down))

        return (d1,Y1) if d1 < d2 else (d2, Y2)

    # return order: rounded sum, absolute pairwise difference, Y, X
    return Sum, helper(0,[],0), X

### TESTS
print(diff_Y([1.3,2.3,4.4]))
print(diff_Y([2.3,1,4.4]))
print(diff_Y([1.3,2.3,4.4,7.2]))
