"""
@author Zach Stoebner
@date 12-11-2019
@descrip Given an integer n, return the length of the longest consecutive
run of 1s in its binary representation.

For example, given 156, you should return 3.
"""

def longest_1s_chain(num):

    mx = 0
    cur = 0
    while num != 0:
        if num & 1 == 1:
            cur += 1
        else:
            mx = cur if cur > mx else mx
            cur = 0
        num >>= 1
    mx = cur if cur > mx else mx
    return mx

### TESTS
print(longest_1s_chain(156)) #3
print(longest_1s_chain(256)) #1
