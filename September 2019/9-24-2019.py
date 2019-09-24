"""
@author Zach Stoebner
@date   9-24-2019
@descrip Given an N by M matrix consisting only of 1's and 0's,
find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4.
"""
#Can check each entry sequentially and keep track of the index and length on cur row
#If there is a rectangle it will match same length and column indices on next row

#rectangle
#returns the area of the largest rectangle of 1's in an NxM matrix
#Complexity:
def rectangle(mat=list([])):
    n = len(mat)
    m = len(mat[0])
    area = 0

    #parse_row
    #parses the row and returns a list of the longest consecutive cols
    #Complexity: O(M)
    def parse_row(row):
        nonlocal m,mat

        length = 0
        cols = list([])

        cur_max_length = length
        cur_cols = cols
        equal_length = list([])

        broken = False
        for j in range(m):

            if not broken and mat[row][j] == 1:
                length += 1
                cols.append(j)
            elif broken and mat[row][j] == 1:
                broken = False
                length += 1
                cols.append(j)

            if mat[row][j] == 0:
                if length == cur_max_length:
                    equal_length.append(cols)
                elif length > cur_max_length:
                    cur_max_length = length
                    cur_cols = cols

                length = 0
                cols = list([])

        lines = list([cur_cols])
        for mark in equal_length:
            if len(mark) == cur_max_length:
                lines.append(mark)

        return lines

    #find_rect
    #a helper function that takes the row and the list of cols that are 1 on that row
    #Complexity: O(NxM)
    def find_rect(row,lines):
        nonlocal n,area,mat

        for line in lines:
            length = len(line)
            cur_area = length

            i = row+1
            while i < n:
                valid = True
                for j in line:
                    if mat[i][j] == 0:
                        valid = False

                if valid:
                    cur_area += length
                    i += 1
                else:
                    i = n+1

            if cur_area > area:
                area = cur_area

    for i in range(n):
        ones = parse_row(i)
        find_rect(i,ones)

    return area

### TESTS
mat = [[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
print(rectangle(mat)) #3
#yikes that's one short, need to debug
