"""
@author Zach Stoebner
@date 1-9-2020
@details Given an array of numbers N and an integer k, your task is to split N into k partitions
such that the maximum sum of any partition is minimized. Return this sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, since the optimal
partition is [5, 1, 2], [7], [3, 4].
"""

# I thought this was stars and bars at first but I implemented a greedy algorithm that I think worked.

# min_max_sum
# Returns the minimized maximum sum of any k-partition grouping of N numbers
# Complexity: O(n)
def min_max_sum(arr: list, k: int):
    arr.sort()
    n = len(arr)
    parts = [[] for _ in range(k)]
    sums = [0 for _ in range(k)]

    for _ in range(n // k):
        last_k, arr = arr[-k:], arr[:k]
        last_k.reverse()
        for num in last_k:
            mn = min(sums)
            i = sums.index(mn)
            parts[i].append(num)
            sums[i] += num

    return parts, max(sums)

### TESTS
t1 = [5, 1, 2, 7, 3, 4]
print(min_max_sum(t1,3))
t2 = [10,11,3,5,6,8,12,14,21]
print(min_max_sum(t2,3))

"""
([[7, 1], [5, 2], [4, 3]], 8)
([[21, 5], [14, 5, 6], [12, 6, 3, 3]], 26)
"""
