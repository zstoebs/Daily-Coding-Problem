"""
@author Zach Stoebner
@date 12-21-2019
@descrip Given a sorted array, find the smallest positive integer that is not the sum of a
subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
"""

# smallest_nonsum
# Finds the smallest positive integer that is not the sum of a subset of the array
# Complexity: O(n)
def smallest_nonsum(arr=[]):

    """
     for any consecutive sequence of numbers:
     1. their total sum equals n(n+1) / 2
     2. Each consecutive number up to the triangle sum is a subset sum'

     [2,3,10] should return 1
     [1,2,3,7,10] should return 14

     While triangle_sum + 1 is in the array [at arr[last_consec+1]], we can hop to that for reference
     b/c all numbers up to 2*triangle_sum+1 will be mapped
    """


    n = len(arr)
    if n == 0: # O(n)
        return None
    elif arr[0] != 1:
        return 1

    # helper to starting find consec sequence of indices
    def last_consec(ind_start=0):
        nonlocal n
        while ind_start+1 < n and arr[ind_start] == arr[ind_start + 1] - 1:
            ind_start += 1

        # either ind_start == n-1 or ind_start indicates index of last consec int from start ind
        return ind_start

    last = last_consec()
    tri_sum = int(arr[last]*(arr[last]+1) // 2)
    while last+1 < n and tri_sum + 1 in arr[last+1:]:
        back = arr[last+1:]
        next = back.index(tri_sum+1)
        last = next
        tri_sum += tri_sum + 1
    return tri_sum + 1

### TESTS
print(smallest_nonsum([1, 2, 3, 10]))
print(smallest_nonsum([ 2, 3, 10]))
print(smallest_nonsum([1, 2, 3, 7,10]))
print(smallest_nonsum([1, 2, 3, 7,10,14]))

"""
7
1
14 <-- error: should be 24
28 <-- error: should be 38 b/c 10 in array allows mapping
"""

# a much more laconic solution from: https://www.geeksforgeeks.org/find-smallest-value-represented-sum-subset-given-array/
def consec_sum(arr=[]):

    n = len(arr)
    if n == 0:
        return None
    ret = 1
    for i in range(n):
        if arr[i] <= ret:
            ret += arr[i]
        else:
            break
    return ret

### TESTS
print(consec_sum([1, 2, 3, 10]))
print(consec_sum([ 2, 3, 10]))
print(consec_sum([1, 2, 3, 7,10]))
print(consec_sum([1, 2, 3, 7,10,14]))
"""
7
1
24
38
"""

### ADMIN SOLUTION
def smallest_impossible_sum(nums):
    impossible_sum = 1
    for n in nums:
        if n <= impossible_sum:
            impossible_sum += n
        else:
            break
    return impossible_sum
