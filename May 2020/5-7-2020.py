"""
@author Zach Stoebner
@date 5-7-2020
@details A strobogrammatic number is a positive number that appears
the same after being rotated 180 degrees. For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""

# strobo_nums
# returns all strobogrammatic numbers with N digits
# Complexity: O(10**(N))
def strobo_nums(N: int):

    # determines whether an integer is strobogrammatic
    def is_strobo(number: int):
        flip = ['0','1','8']
        nonflip = ['2','3','4','5','7']

        num = str(number)
        length = len(num)
        mark = int(length // 2)

        first_half = num[:mark]
        first_half = first_half[-1::]

        for i, dig in enumerate(first_half):
            if dig == '6':
                first_half = first_half[:i] + first_half[i:].replace('6','9',1) # b/c str is immutable, can't index assign chars
            elif dig == '9':
                first_half = first_half[:i] + first_half[i:].replace('9','6',1)

        for dig in nonflip:
            first_half = first_half.replace(dig,'-')

        second_half = num[mark:]

        if length % 2 == 0:
            return first_half == second_half
        else:
            middle = second_half[0]
            second_half = second_half[1:]
            return middle in flip and first_half == second_half

    strobos = []
    if N == 1:
        strobos += [0]

    for num in range(10**(N-1),10**N):
        if is_strobo(num):
            strobos += [num]
    return strobos

### TESTS
print(strobo_nums(1))
print(strobo_nums(2))
print(strobo_nums(3))
print(strobo_nums(4))

### ADMIN SOLUTION
# Complexity: O(5^(N/2))
def backtrack(n, flips, nums, result, curr):
    if len(curr) == (n + 1) // 2:
        # We cannot use numbers that start with 0, and 6 or 9 cannot be in the center.
        if curr[0] == '0' or (n % 2 != 0 and curr[-1] in ('6', '9')):
           return

        # If the number has an odd number of digits, do not flip and add the center.
        prefix = curr if n % 2 == 0 else curr[:-1]

        # Take each digit down, flip it and reverse it.
        new_res = prefix + list(reversed([flips[num] for num in curr]))

        result.append(''.join(new_res))

    else:
        for num in nums:
            curr.append(num)
            backtrack(n, flips, nums, result, curr)
            curr.pop()

    return result

def strobos(n):
    result = []
    if n == 0:
        return result

    flips = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    nums = list(flips.keys())

    result = backtrack(n, flips, nums, result, [])

    return result
print()
print(strobos(1))
print(strobos(2))
print(strobos(3))
print(strobos(4))
print(strobos(10))
