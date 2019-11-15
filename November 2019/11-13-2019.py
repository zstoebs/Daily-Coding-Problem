"""
@author Zach Stoebner
@date 11-13-2019
@descrip Given an array of positive integers, divide the array into
two subsets such that the difference between the sum of the subsets
is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and
{5, 15, 20}, which has a difference of 5, which is the smallest
possible difference.
"""
#high_cost
#Returns the subsets with the
def high_cost(arr=list()):
    n = len(arr)

    sets = set()

    # This is an error because it doesn't construct sets of non-consecutive numbers in the given array
    for i in range(n):
        for j in range(i+1,n):
            if j < n - 1:
                sets.add(arr[i:j])
            else:
                sets.add(arr[i:])

    def sum_set(arr=list()):
        sum = 0
        for i in arr:
            sum += i
        return sum

    cur_min = None
    min_sets = None
    i = 1
    for s1 in sets:
        sum1 = sum_set(s1)
        for s2 in sets[i:]
            sum2 = sum_set(s2)
            diff = abs(sum1-sum2)
        if cur_min is None:
            cur_min = diff
            min_sets = tuple([s1,s2])
        elif diff < cur_min:
            cur_min = diff
            min_sets = tuple([s1,s2])

    i += 1
    return min_sets

#This function doesn't work


def small_diff(arr=list()):

    n = len(arr)
    arr.sort()

    total = 0
    for i in arr:
        total += i

    sub1 = list()
    sub2 = list()
    sum = 0
    while sum < total / 2:
        sub1.append(arr.pop(0))
        sum += sub1[-1]

    ### perhaps there's some more efficient algorithm using element differences or something ??

### ADMIN SOLUTION
from math import inf
from itertools import combinations

def two_subsets(nums):
    smallest_diff = inf

    result = None
    for subset1, subset2 in subset_pairs(nums):
        diff = abs(sum(subset1) - sum(subset2))
        if diff < smallest_diff:
            smallest_diff = diff
            result = (subset1, subset2)
    return result

def subset_pairs(nums):
    n = len(nums)
    for r in range(n + 1):
        for indices in combinations(range(n), r):
            subset1 = [nums[i] for i in indices]
            subset2 = [nums[i] for i in set(range(n)) - set(indices)]
            yield subset1, subset2
