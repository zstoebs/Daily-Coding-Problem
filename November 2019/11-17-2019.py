"""
@author Zach Stoebner
@date 11-17-2019
@descrip Given a circular array, compute its maximum subarray sum in O(n) time.
A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8
where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
"""

#max_sub_sum
#Returns the maximum subarray sum in linear time --> one pass
#Complexity: O(n) --> one pass
def max_sub_sum(arr=list()):

    n = len(arr)

    start = 0
    init_sum = 0
    # finding first negative number or summing entire array
    while start < n and arr[start] >= 0: #O(q) where q is first part of array that
        init_sum += arr[start]
        start += 1

    # no negative numbers
    if start == n:
        return init_sum

    # negative number so look over rest of array
    mx = init_sum
    run_sum = 0
    for i in range(start+1,n): #O(n - q) --> rest of array meaning both loops execute in one pass
        if i < n-1:
            if arr[i] >= 0:
                run_sum += arr[i]
            else:
                mx = run_sum if run_sum > ma else mx
                run_sum = 0
        else:
            if arr[i] >= 0:
                run_sum += arr[i] + init_sum
                mx = run_sum if run_sum > mx else mx

    return mx

###TESTS
t1 = [8, -1, 3, 4]
print(max_sub_sum(t1)) #15
t2 = [-4, 5, 1, 0]
print(max_sub_sum(t2)) #6

###ADMIN SOLUTION
def maximum_circular_subarray(arr):
    max_subarray_sum_wraparound = sum(arr) - min_subarray_sum(arr)
    return max(max_subarray_sum(arr), max_subarray_sum_wraparound)


def max_subarray_sum(arr):
     max_ending_here = max_so_far = 0
     for x in arr:
         max_ending_here = max(x, max_ending_here + x)
         max_so_far = max(max_so_far, max_ending_here)
     return max_so_far


def min_subarray_sum(arr):
     min_ending_here = min_so_far = 0
     for x in arr:
         min_ending_here = min(x, min_ending_here + x)
         min_so_far = min(min_so_far, min_ending_here)
     return min_so_far
