"""
@author Zach Stoebner
@date 12-30-2019
@descrip Implement the function fib(n), which returns the nth number in the
Fibonacci sequence, using only O(1) space.
"""

# fib
# Returns the nth fibonacci number using O(1) space
# Complexity: O(n) time, O(1) space
def fib(n: int):

    # uses 3 local variables regardless of n
    prev = 1
    anteprev = 1
    tmp = None

    # assuming that 1 is the 0th and the 1st number
    while n > 1:
        tmp = prev
        prev += anteprev
        anteprev = tmp
        n -= 1

    return prev

### TESTS
for i in range(20):
    print(fib(i))

"""
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
"""

### ADMIN SOLUTION
"""
O(1) time and space solution that uses the closed form solution to the fib sequence.
"""
from math import sqrt

PHI = (1 + sqrt(5)) / 2

def fib(n: int):
    return int(PHI ** n / sqrt(5) + 0.5)
