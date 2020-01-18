"""
@author Zach Stoebner
@date 1-18-2020
@details The ancient Egyptians used to express fractions as a sum of several terms where each
numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.
"""

# https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/

import math
# egyptian_frac
# Converts a fraction to an egyptian fraction
# Complexity: O(a)
def egyptian_frac(a: int, b: int):

    denoms = []

    # helper function for recursion to find smaller fractions
    def recurse(num: int, denom: int):
        nonlocal denoms
        assert num < denom

        if num == 0:
            return

        unit = int(math.ceil(denom / num))
        denoms.append(unit)

        """
        a/b - c/d = a*d / b*d - c*b / b*d
        """
        new_num = num*unit - denom
        new_denom = unit*denom
        recurse(new_num,new_denom)

    recurse(a,b)
    ret = ""
    for denom in denoms:
        if ret == "":
            ret += "1 / " + str(denom)
        else:
            ret += " + 1 / " + str(denom)

    return ret

### TESTS
print(egyptian_frac(4,13))
