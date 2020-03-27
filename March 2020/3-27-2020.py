"""
@author Zach Stoebner
@date 3-27-2020
@details Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:

You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.
For example, given 100, you can reach 1 in five steps with the following route:
100 -> 10 -> 9 -> 3 -> 2 -> 1.
"""

import math

# prime_factors
# Return the prime factors of an integer N
# Complexity: O(logn)
def prime_factors(N: int):

    n = N

    factors = []

    while n % 2 == 0:
        factors += 2
        n /= 2

    for i in range(3, math.sqrt(n), 2):

        while n % i == 0:
            factors += i
            n /= i

    if n > 2:
        factors += n

    return factors


# steps
# Return the steps it takes to reach 1 with above stipulations
# Complexity: O((logN)^2)
def steps(N: int, nums = []):

    factors = prime_factors(N)

    l1 = []
    l2 = []
    i = 0
    k = len(factors) - 1
    while i <= k:
        if i % 2 == 0:
            l1.append(factors[i])
            if i != k:
                l1.append(factors[k])
        else:
            l2.append(factors[i])
            if i != k:
                l2.append(factors[k])
        i += 1

    f1 = 1
    for f in l1:
        f1 *= f
    f2 = 1
    for f in l2:
        f2 *= f

    next = max(f1,f2)
    nums += next

    if next == 1:
        return len(nums), nums

    return steps(next, nums)

### TESTS
print(steps(100))
