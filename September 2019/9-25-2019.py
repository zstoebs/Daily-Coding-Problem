"""
@author Zach Stoebner
@date   9-25-2019
@descrip Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
"""

class bit_array:

    def __init__(self,size):
        self.size = size
        self.array = [0]*size

    def set(self,i,val):

        data = val
        while data != 0 and data != 1:
            data = input("Please input a value of 0 or 1: ")

        ind = i
        while not ind < self.size and not ind >= 0:
            ind = input("Please input an inbound index: ")

        self.array[ind] = data


    def get(self,i):

        ind = i
        while not ind < self.size and not ind >= 0:
            ind = input("Please input an inbound index: ")

        return self.array[ind]

    def __str__(self):
        return str(self.array)

### TESTS
t1 = bit_array(10)
print(t1)
t1.set(1,1)
print(t1.get(1))
#t1.set(11,2) -- results in an infinite loop on my machine but I think that it's Hydrogen being unable to handle Python input or Atom.io

### ADMIN SOLUTION
import math


BITS_PER_INT = 32


class BitArray(object):
    def __init__(self, size):
        self._list = [0] * int(math.ceil(size / float(BITS_PER_INT)))
        self._size = size

    def get(self, i):
        if i < 0 or i >= self._size:
            raise IndexError('Index out of bounds')

        list_idx = i / BITS_PER_INT
        int_idx = i % BITS_PER_INT

        return (self._list[list_idx] >> int_idx) & 1

    def set(self, i, val):
        if i < 0 or i >= self._size:
            raise IndexError('Index out of bounds')

        list_idx = i / BITS_PER_INT
        int_idx = i % BITS_PER_INT

        self._list[list_idx] ^= (-val ^ self._list[list_idx]) & (1 << int_idx)
