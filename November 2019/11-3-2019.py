"""
@author Zach Stoebner
@date 11-3-2019
@descrip Determine whether there exists a one-to-one character mapping
from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can
map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

#injection
#Returns true if there is an injection from s1 onto s2
#Complexity: O(n)
def injection(s1,s2):

    set1 = set()
    set1 = set()

    for c in s1:
        set1.add(c)
    for c in s2:
        set1.add(c)

    return len(set1) <= len(set2)
