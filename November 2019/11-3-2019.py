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
    set2 = set()
    cnt1 = list()
    cnt2 = list()
    for c in s1:
        set1.add(c)
    for c in s2:
        set2.add(c)

    # checking PHP
    l1 = len(set1)
    l2 = len(set2)
    if l2 < l1:
        return False

    for c in set1:
        cnt1.append(tuple([c,s1.count(c)]))
    for c in set2:
        cnt2.append(tuple([c,s2.count(c)]))

    pro = lambda x: x[1]
    cnt1.sort(key=pro)
    cnt2.sort(key=pro)
    print(cnt1,cnt2)

    for let in cnt1:
        while l2 > 0 and cnt2[0][1] < let[1]:
            cnt2.pop(0)
            l2 -= 1
        if l2 > 0:
            cnt2.pop(0)
            l2 -= 1
            l1 -= 1

        # check PHP
        if l2 < l1:
            return False

    return True

### TESTS
s1 = "abc"
s2 = "bcd"
print(injection(s1,s2))
s1 = "foo"
s2 = "bar"
print(injection(s1,s2))

###ADMIN SOLUTION
def mapping_exists(s1, s2):
    if len(s1) != len(s2):
        return False

    mapping = {}
    for char1, char2 in zip(s1, s2):
        if char1 not in mapping:
            mapping[char1] = char2
        elif mapping[char1] != char2:
            return False

    return True
