"""
@author Zach Stoebner
@date 12-14-2019
@descrip We say a number is sparse if there are no adjacent ones in its binary representation.
For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the
smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.
"""

# nearest_sparse
# Finds the smallest sparse number greater than or equal to N
# Complexity: O(N)
def nearest_sparse(N):

    # first need to find the alternating ones number for a number with the same number of bits
    def get_alts(N):
        power = 0
        i = 0
        while power < N:
            power = pow(2,i)
            i += 1
        power -= 1

        alt0 = power
        i = 0
        while pow(2,i) < N:
            alt0 -= pow(2,i)
            i += 2

        alt1 = power
        i = 1
        while pow(2,i) < N:
            alt1 -= pow(2,i)
            i += 2

        return alt0, alt1

    """
    10101
    01010
    10110
    10100

    If you ORR with the alternating ones sequence and it's greater, then there are adjacent ones.
    """
    ret = N
    alt0, alt1 = get_alts(ret)
    while ret | alt0 > alt0 and ret | alt1 > alt1:
        ret += 1
        alt0, alt1 = get_alts(ret)

    return ret, bin(ret)

### TESTS
print(nearest_sparse(21))
print(nearest_sparse(22))
print(nearest_sparse(257))
print(nearest_sparse(359))
print(nearest_sparse(0b110110110101011))

"""
(21, '0b10101')
(34, '0b100010')
(257, '0b100000001')
(514, '0b1000000010')
(32770, '0b1000000000000010')
"""

### ADMIN SOLUTION

# Complexity: O(logn)
def next_sparse_number(num):
    # Convert to list of bits, from least to most significant.
    b = []
    while num:
        b.append(num & 1)
        num = num >> 1
    b.append(0)

    # Find the places where 011 exists, and turn them into 100 with trailing zeros.
    highest_zeroed_bit = 0
    for i in range(len(b) - 2):
        if b[i] and b[i + 1] and not b[i + 2]:
            b[i + 2] = 1
            for j in range(i + 1, highest_zeroed_bit - 1, -1):
                b[j] = 0
            highest_zeroed_bit = i + 1

    # Convert back to integer.
    num = 0
    for i in range(len(b)):
        num += b[i] * (1 << i)
    return num
