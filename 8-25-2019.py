"""
Author: Zach Stoebner
Created on: 8-25-2019
Descrip:

Given an integer list where each number
represents the number of hops you can make,
determine whether you can reach to the last
index starting at index 0.

For example, [2, 0, 1, 0] returns True while
[1, 1, 0, 1] returns False.

"""
#hops
#Note: returns true if can hop to the end, else false
#Complexity: O(n) time
def hops(numbers):
    length = len(numbers)

    i = 0
    while i < length-1:
        if numbers[i] == 0:
            if i < length-1:
                return False
            return True
        i += numbers[i]
    return True

### TESTS
ints = [2,0,1,0]
print(hops(ints)) #True
ints = [1,1,0,1]
print(hops(ints)) #False
ints = [0,1,1,0]
print(hops(ints)) #False
ints = [3,0,0,1]
print(hops(ints)) #True
ints = [4,0,0,1]
print(hops(ints)) #True

### ADMIN SOLUTION
def can_reach_end(hops):
    steps_left = 1

    for i in range(len(hops) - 1):
        steps_left = max(steps_left - 1, hops[i])
        if steps_left == 0:
            return False
    return True
