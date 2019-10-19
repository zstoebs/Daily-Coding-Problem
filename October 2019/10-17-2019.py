"""
@author Zach Stoebner
@date 10-17-2019
@descrip Given a string, return the first recurring character in it,
or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef",
return null.
"""

#first_recurring
#Returns the first recurring letter in the stirng
#Complexity: O(n)
def first_recurring(string=""):

    lookup = dict([])
    for letter in string:
        if letter in lookup.keys():
            return letter
        else:
            lookup[letter] = 1

    return None

### TESTS
print(first_recurring("acbbac")) # b
print(first_recurring("abcdef")) # None

### ADMIN SOLUTION

def first_recurring(str):
    checker = 0
    for c in str:
        val = ord(c) - ord('a')
        if (checker & (1 << val)) > 0:
            return c
        checker |= (1 << val)
    return None
