"""
@author Zach Stoebner
@date 12-25-2019
@descrip Given a list of numbers, create an algorithm that arranges them in order to
form the largest possible integer. For example, given [10, 7, 76, 415], you should return 77641510.
"""

# Need to find the nums with the largest MSDs which can be done using a base conversion algo
# I'm opting to not convert the integer to a string and access the 0th digit

# large_int
# Given a list of ints, return the ints rearranged to find the largest possible integer
# Complexity: O(nlogn + k*n), where k is the number of digits in the largest number
def large_int(nums=[]):

    # initializing a digit map
    msd_map = {i: [] for i in range(10)}

    # finding the MSD
    def find_MSD(num): # O(k)

        iters = 1
        while num // 10 > 0:
            num //= 10
            iters += 1
        return int(num % 10)

    # mapping
    for num in nums: #O(n)
        msd = find_MSD(num)
        msd_map[msd].append(num)

    # sorting
    for msd in msd_map.keys(): #O(nlogn)
        msd_map[msd].sort()

    # creating the number
    ret = ""
    # from largest digits to smallest
    for msd in sorted(msd_map.keys(),reverse=True):
        cur_num = ""
        # from largest nums to smallest
        for num in reversed(msd_map[msd]):
            # a single digit then prepend for a larger number
            if num == msd:
                cur_num = str(num) + cur_num
            # if not a single digit, want the larger numbers to go first
            else:
                cur_num += str(num)
        ret += cur_num

    return int(ret)

### TESTS
print(large_int([10, 7, 76, 415]))

### ADMIN SOLUTION
def get_largest_value(nums):
    nums = [str(x) for x in nums]
    length = len(max(nums, key=len))

    normalized = []
    for i, x in enumerate(nums):
        element = x * (length // len(x) + 1)
        normalized.append(element[:length])

    ordered = sorted(zip(nums, normalized), key=lambda x: x[1], reverse=True)

    return ''.join([x[0] for x in ordered])
