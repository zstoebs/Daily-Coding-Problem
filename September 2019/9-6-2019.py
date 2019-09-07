"""
@author Zach Stoebner
@date 9-6-2019
@details Given a sorted list of integers,
          square the elements and give the output in sorted order.

          For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""

def square_sort(ints):

    for i,int in enumerate(ints):
        ints[i] = int**2

    return sorted(ints)

ints = [-9, -2, 0, 2, 3]
print(square_sort(ints))
