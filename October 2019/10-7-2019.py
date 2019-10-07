"""
@author Zach Stoebner
@date 10-7-2019
@descrip Given a list of numbers L, implement a method sum(i, j)
which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return
sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should
be optimized over the pre-processing step.
"""

def sum(L,i,j):

    sum = 0
    for ind in range(i,j):
        sum += L[ind]

    return sum

### TESTS
L = [1,2,3,4,5]
print(sum(L,1,3)) #5
# I'm probably missing something here b/c DCP classified this problem as hard.
# But it appears extraordinarily easy. 
