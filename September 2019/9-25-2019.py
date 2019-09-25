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
#t1.set(11,2) -- results in an infinite loop on my software but I think that it's Hydrogen or Atom.io
