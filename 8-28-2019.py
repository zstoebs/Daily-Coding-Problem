"""
Author: Zach Stoebner
Created on: 8-28-2019
Descrip:

Given an unsigned 8-bit integer, swap its
even and odd bits. The 1st and 2nd bit
should be swapped, the 3rd and 4th bit
should be swapped, and so on.

For example, 10101010 should be 01010101.
11100010 should be 11010001.

Bonus: Can you do this in one line?

"""
#even_odd_bit_swap
#Note: swaps the even and odd bits
#Complexity: O(1) time + O(1) space
def even_odd_bit_swap(word):

    return bin(((word & 0b10101010) >> 1) | ((word & 0b01010101) << 1))

word = 0b10101010
print(even_odd_bit_swap(word))
word = 0b11100010
print(even_odd_bit_swap(word))
