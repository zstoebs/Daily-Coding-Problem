"""
@author Zach Stoebner
@date 10-19-2019
@descrip Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
                              return 0000 1111 0000 1111 0000 1111 0000 1111.
"""

#flip_bits
#Returns the inverse (one's complement) of a 32-bit number
#Complexity: O(1)
def flip_bits(num):
    return bin(num ^ 0xFFFFFFFF)

### TESTS
num = 0xF0F0F0F0 # the input binary number in hex
print(flip_bits(num)) #0b1111000011110000111100001111 --> python truncates any leading 0's so this is the 28-bit version w/o a nibble of 0's
