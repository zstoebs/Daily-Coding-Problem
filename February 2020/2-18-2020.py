"""
@author Zach Stoebner
@date 2-18-2020
@details A regular number in mathematics is defined as one which evenly divides some power of 60.
Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning
instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
"""

#https://math.stackexchange.com/questions/2415583/determining-sequence-of-regular-numbers

# reg_nums
# Returns a sequence of the first N regular numbers
# Complexity: O(N)
def reg_nums(N: int):

    seq = set()
    count = 0
    a = b = c = 1
    while a <= N:
        while a*b <= N:
            while a*b*c <= N:
                seq.add(a*b*c)

                c *= 5
            b *= 3
        a *= 2

    return seq

### TESTS
print(reg_nums(5))
