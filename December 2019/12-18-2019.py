"""
@author Zach Stoebner
@date 12-18-2019
@descrip Let's define a "sevenish" number to be one which is either a power of 7, or the sum of
unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm
to find the nth sevenish number.
"""

# the sequence of sevenish numbers starts with the powers and then for every power before it
# in sorted order add to the current power.
# the next power will bever be less than the sum of all powers before it
# recursion is a potential solution here

# sevenish
# Returns the nth sevenish number
# Complexity: O(n^2)
def sevenish(n=0):

    # getting the first n powers
    powers = []
    for i in range(n):
        powers.append(pow(7,i))

    # filling in the unique sums
    for i in range(n):
        run_sum = powers[i]
        for j in range(i+1,n):
            powers.append(powers[i]+powers[j])
            run_sum += powers[j]
            if j != i+1:
                powers.append(run_sum)

    # sorting the sequence to get the nth sevenish number
    powers.sort()
    return powers[n-1]

### TESTS
print(sevenish(1))
print(sevenish(2))
print(sevenish(3))
print(sevenish(4))

"""
1
7
8
49
"""

###ADMIN SOLUTION
def nth_sevenish_number(n):

    answer = 0
    bit_place = 0

    while n:
        if (n & 1):
            answer += 7 ** bit_place

        n >>= 1
        bit_place += 1

    return answer
