"""
@author   Zach Stoebner
@date     9-28-2019
@descrip  Given an array of integers in which two elements appear
  exactly once and all other elements appear exactly twice, find
  the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8.
The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""

#two_once
#returns a list of ints that only occur once in the array, all others occur twice
#Complexity: O(nlogn) time O(1) space
def two_once(arr):

    count = 0
    pair = list([None,None])
    for i in range(len(arr)):
        cp = arr.copy()
        cp.pop(i)
        if not arr[i] in cp:
            pair[count] = arr[i]
            count += 1
        if count > 1:
            return pair

    assert pair[0] != None and pair[1] != None
    return pair

### TESTS
arr = [2, 4, 6, 8, 10, 2, 6, 10]
print(two_once(arr)) #4,8
arr.append(4)
arr.append(8)
print(two_once(arr)) #AssertionError

#for linear time, constant space solution, have to use bits
#https://www.geeksforgeeks.org/find-the-element-that-appears-once/


### ADMIN SOLUTION
def array_two_elements(arr):
    xor = 0
    for num in arr:
        xor = xor ^ num

    # Get rightmost set bit
    xor = xor & -xor

    rets = [0, 0]
    for num in arr:
        if num & xor:
            rets[0] = rets[0] ^ num
        else:
            rets[1] = rets[1] ^ num
    return rets
