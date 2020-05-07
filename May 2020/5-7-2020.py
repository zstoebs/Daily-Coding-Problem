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
