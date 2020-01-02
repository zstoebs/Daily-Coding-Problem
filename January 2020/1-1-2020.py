"""
@author Zach Stoebner
@date 1-1-2020
@details Given an array of numbers of length N, find both the minimum and maximum using
less than 2 * (N - 2) comparisons.
"""

# 5-comparison median method is likely useful here b/c need to find min and max with fewest comparisons possible
# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

# quick_max_min
# Returns the min and max of an array in approx. 3/2*n-2 comparisons
# Complexity: O(n)
def quick_max_min(arr: list):
    n = len(arr)

    min = None
    max = None
    i = 0
    if n%2 == 0:
        if arr[0] < arr[1]:
            min = arr[0]
            max = arr[1]
        else:
            min = arr[1]
            max = arr[0]
        i = 2
    else:
        min = max = arr[0]
        i = 1

    while i < n-1:
        if arr[i] < arr[i+1]:
            min = arr[i] if arr[i] < min else min
            max = arr[i+1] if arr[i+1] > max else max
        else:
            min = arr[i+1] if arr[i+1] < min else min
            max = arr[i] if arr[i] > max else max

        i += 2

    return min, max

### TESTS
t1 = [3,4,0,-1,9,2,17]
print(quick_max_min(t1)) # (-1, 17)

### ADMIN SOLUTION
def min_and_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    elif len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
    else:
        n = len(arr) // 2
        lmin, lmax = min_and_max(arr[:n])
        rmin, rmax = min_and_max(arr[n:])
        return min(lmin, rmin), max(lmax, rmax) 
