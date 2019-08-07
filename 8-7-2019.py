"""
Author: Zach Stoebner
Created on: 8-7-2019
Descrip:

Implement division of two positive integers
without using the division, multiplication,
or modulus operators. Return the quotient
as an integer, ignoring the remainder.

"""
#know that inexact division and multiplication can be implemented with recursion
def inexactDivision(numerator,denominator):

    difference = numerator - denominator

    if difference < 0:
        return 0
    else:
        return 1 + inexactDivision(difference,denominator)

print(inexactDivision(4,2))
print(inexactDivision(10,3))
print(inexactDivision(3,10))
print(inexactDivision(20,1))
print(inexactDivision(1,20))
