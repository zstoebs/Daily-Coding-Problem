"""
@author Zach Stoebner
@date 11-22-2019
@descrip Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller than
M[i1, j1] and larger than M[i2, j2].

For example, given the following matrix:

[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]
And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 (WRONG should be 14) as there are 15 numbers in
the matrix smaller than 6 or greater than 23.
"""
#This problem resembles a median of medians setup

#less_greater
#Return the number elems less than M[i1,j1] and greater than M[i2,j2]
#Complexity: O(NM)
def less_greater(M,i_1,j_1,i_2,j_2):

    m1 = M[i_1][j_1]
    m2 = M[i_2][j_2]

    n = len(M)
    m = len(M[0])
    count = 0
    for i in range(n):
        for j in range(m):
            count = count + 1 if M[i][j] < m1 or M[i][j] > m2 else count

    return count

#corners
#Return the number elems less than M[i1,j1] and greater than M[i2,j2]
#Complexity: O(NM) but better than the previous algo
def corners(M,i_1,j_1,i_2,j_2):

    m1 = M[i_1][j_1]
    m2 = M[i_2][j_2]

    n = len(M)
    m = len(M[0])
    count = 0

    # b/c rows and columns are pre-sorted, know that these corners satisfy conditions
    count += (i_1+1)*(j_1+1) - 1 + (n - i_2)*(m - j_2) - 1

    #checking elems that we don't know about

    #lows
    for i in range(i_1):
        u_j = j_1 + 1
        while M[i][u_j] < m1:
            count += 1
            u_j += 1
    for j in range(j_1):
        u_i = i_1 + 1
        while M[u_i][j] < m1:
            count += 1
            u_i += 1

    #highs
    for i in range(i_2+1,n):
        u_j = j_2 - 1
        while M[i][u_j] > m2:
            count += 1
            u_j -= 1
    for j in range(j_2+1,m):
        u_i = i_2 - 1
        while M[u_i][j] > m2:
            count += 1
            u_i -= 1

    return count



### TESTS
M = [[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]
print(less_greater(M,1,1,3,3)) #14
print(corners(M,1,1,3,3)) #14
