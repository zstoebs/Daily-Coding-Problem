"""
@author Zach Stoebner
@date 2-12-2020
@details UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100.
The rules for mapping characters are as follows:

For a single-byte character, the first bit must be zero.
For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes
all start with 10.
Visually, this can be represented as follows.

 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Write a program that takes in an array of integers representing byte values, and returns
whether it is a valid UTF-8 encoding.
"""

def is_utf8(bytes: list):

    n = len(bytes)

    # can't have n 1s and a 0 with more than 7 total bytes
    if n > 7:
        return False

    # single byte special condition
    if n == 1 and bytes[0] >= 2**7:
        return False

    mask = 0
    rest = 0b10000000

    # making a mask to check the first byte
    exp = 7
    for i in range(n):
        mask += 2**(exp - i)

    for i in range(n+1,8):
        mask += 2**(exp - i)

    if byte[0] & mask != byte[0]:
        return False

    for byte in bytes[1:]:
        if byte & 0b10111111 != byte:
            return False

    return True

### TESTS
print(is_utf8([0b0]))
print(is_utf8([0b11010101, 0b10111111]))
print(is_utf8(0b10101010, 0b10000000))
print(is_utf8([0b11010101, 0b01001010]))
