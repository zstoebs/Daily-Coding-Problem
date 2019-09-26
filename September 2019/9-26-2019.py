"""
@author   Zach Stoebner
@date     9-26-2019
@descrip  Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""

#min_coins
#return the minimum number of coins to make n cents
#Complexity: O(1)
def min_coins(n):

    assert n > 0

    denoms = [25,10,5,1]

    count = 0
    rem = n
    # check for every denom
    for denom in denoms:
        if rem >= denom:
            count += int(rem // denom)
            rem = rem % denom
        if rem == 0:
            return count

### TESTS
print(min_coins(16)) #3
print(min_coins(25)) #1
print(min_coins(21)) #3
print(min_coins(-1)) #AssertionError
