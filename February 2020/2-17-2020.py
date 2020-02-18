"""
@author Zach Stoebner
@date 2-17-2020
@details Given an array of integers, determine whether it contains a Pythagorean triplet.
Recall that a Pythagorean triplet (a, b, c) is defined by the equation a2+ b2= c2.
"""

# a,b < c so we  can use that with a sorted array to try all possible combos

# pythag_triplet
# Returns whether an array contains a pythagorean triplet
# Complexity: O(n^3)
def pythag_triplet(arr: list):

    arr.sort()
    n = len(arr)

    for i, a in enumerate(arr):
        for j, b in enumerate(arr[i+1:]):
            for c in arr[j+1:]:
                if a**2 + b**2 == c**2:
                    return True

    return False

### TESTS
print(pythag_triplet([1,2,3,4])) #False
print(pythag_triplet([1,89,5,4,6])) #True

### ADMIN SOL
def triplet(array):
    array = sorted([x ** 2 for x in array])

    for c in range(len(array) - 1, 1, -1):
        a, b = 0, c - 1

        while a < b:
            if array[a] + array[b] == array[c]:
                return True
            elif array[a] + array[b] < array[c]:
                a += 1
            else:
                b -= 1

    return False
