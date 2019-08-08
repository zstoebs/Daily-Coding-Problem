"""
Author: Zach Stoebner
Created on: 8-7-2019
Descrip:

Implement division of two positive integers
without using the division, multiplication,
or modulus operators. Return the quotient
as an integer, ignoring the remainder.

"""

import time

#know that inexact division and multiplication can be implemented with recursion
def inexactDivision(numerator,denominator):

    difference = numerator - denominator

    if difference < 0:
        return 0
    else:
        return 1 + inexactDivision(difference,denominator)

t1 = time.time()
print(inexactDivision(4,2))
print(inexactDivision(10,3))
print(inexactDivision(3,10))
print(inexactDivision(20,1))
print(inexactDivision(1,20))
print(inexactDivision(31,3))
t2 = time.time()
print("Time: ", t2-t1)

###SOLUTION GIVEN BY DCP
#More complicated, O(N) where N is the number of bits in x/y, slightly faster
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError('division by zero')

    quotient = 0
    power = 32           # Assume 32-bit integer
    yPower = y << power  # Initial y^d value is y^32
    remainder = x        # Initial remainder is x
    while remainder >= y:
        while yPower > remainder:
            yPower >>= 1
            power -= 1
        quotient += 1 << power
        remainder -= yPower

    return quotient

t3 = time.time()
print(divide(4,2))
print(divide(10,3))
print(divide(3,10))
print(divide(20,1))
print(divide(1,20))
print(divide(31,3))
t4 = time.time()
print("Time: ",t4-t3)
