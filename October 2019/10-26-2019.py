"""
@author Zach Stoebner
@date 10-26-2019
@descrip Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?
"""
# A tranpose is a 180 degree rotation so a 90 rotation would be one

#with_space
#Returns a matrix rotated 90 degrees to the right, uses extra space
#Complexity: O(n^2)
import copy
def with_space(mat=list()):

    tmp = copy.deepcopy(mat)
    holder = list()
    length = len(mat)
    for i in range(length):
        holder = mat[i]
        col = length - i - 1
        for j in range(length):
            tmp[j][col] = holder[j]
    return tmp

#without_space
#Returns a matrix rotated 90 degrees in place to the right
#Complexity: O(n^2)
def without_space(mat=list()):

    n = len(mat)

    #transpose
    #Transposes a matrix in place
    #Complexity: O(n^2)
    def transpose(mat=list()):
        nonlocal n

        # computing the transpose
        tmp = None
        skip = 0
        for i in range(n):
            for j in range(skip,n):
                tmp = mat[j][i]
                mat[j][i] = mat[i][j]
                mat[i][j] = tmp
            skip += 1

        return mat

    # computing the transpose
    mat = transpose(mat)
    # unfortunately python doesn't support pass-by-reference
    # 2 reasons why this is O(1) space:
    # 1. assuming that an equal size memory block is allocated for the transpose and the previous memory is deleted on reassignment
    # 2. if the algo weren't a function then no extra space would be used as is

    # reversing the rows
    for i in range(n):
        mat[i].reverse()

    return mat

### TESTS
t1 = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
print(with_space(t1)) # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(without_space(t1)) # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
