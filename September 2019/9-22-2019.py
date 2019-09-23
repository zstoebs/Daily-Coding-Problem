"""
@author Zach Stoebner
@date   9-22-2019
@descrip You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that
implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
"""

#SparseArray class
#translates a very large sparse representation as a more efficient dense representation
class SparseArray:

    #initializer
    def __init__(self,arr,size):
        self.sparse_arr = arr
        self.size = size
        self.dense_arr = dict([])
        for i,val in enumerate(self.sparse_arr):
            if len(self.dense_arr) < self.size:
                if val != 0 and val != None:
                    self.dense_arr[i] = val
            else:
                return

    #string conversion function for printing
    def __str__(self):
        return str(self.dense_arr)

    #set
    #checks if
    def set(self,i,val):
        length = len(self.dense_arr)
        if length < self.size:
            if i not in self.dense_arr.keys():
                self.size += 1
            self.dense_arr[i] = val
            return
        elif length == self.size:
            if i in self.dense_arr.keys():
                self.dense_arr[i] = val
                return
        print("Not enough space")

    def get(self,i):
        if i in self.dense_arr.keys():
            return self.dense_arr[i]
        return None

### TESTS
long_arr = list([])
for i in range(10000):
    if i%13==0 and i%2==1:
        long_arr.append(1)
    else:
        long_arr.append(0)

sparr = SparseArray(long_arr,10)
sparr.set(196,0)
print(sparr.get(29))
print(sparr.get(39))
print(sparr)
