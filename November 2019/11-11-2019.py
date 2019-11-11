"""
@author Zach Stoebner
@date 11-11-2019
@descrip Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""

# could use Euclid's GCD algo but would need to do that for each pair
def gcd(numbers=list()):

    lookup = dict()
    for num in numbers:
        if num not in lookup.keys():
            lookup[num] = set()


    for num in numbers:
        for i in range(1,num+1): # can't divide by 0 and need to include number
            if num % i == 0:
                lookup[num].add(i)

    inter = None
    for key in lookup.keys():
        if inter == None:
            inter = lookup[key].copy()
        else:
            inter &= lookup[key]

    return max(inter)

### TESTS
nums = [42,56,14]
print(gcd(nums)) #14
