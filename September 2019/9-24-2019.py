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
#Complexity: O(N^2)
def rectangle(mat=list([])):
    n = len(mat)
    m = len(mat[0])
    area = 0

    #parse_row
    #parses the row and returns a list of the longest consecutive cols
    #Complexity: O(M)
    def parse_row(row=list([])):
        nonlocal m

        length = cur_max_length = 0
        cols = cur_cols = list([])
        equal_length = list([])

        broken = False
        for j in range(m):

            #if continuous chain
            if not broken and row[j] == 1:
                length += 1
                cols.append(j)
            #if not a continuous chain
            elif broken and row[j] == 1:
                broken = False
                length += 1
                cols.append(j)

            #when chain breaks
            if row[j] == 0:
                #if just coming from chain
                if not broken:
                    #add to list of equal length chains
                    if length != 0 and length == cur_max_length:
                        equal_length.append(cols)
                    #if longest so far, set to cur_longest chain
                    elif length > cur_max_length:
                        cur_max_length = length
                        cur_cols = cols

                    length = 0
                    cols = list([])
                broken = True

        #checking for line that ends at end of row
        if length != 0 and length == cur_max_length:
            equal_length.append(cols)
        elif length > cur_max_length:
            cur_max_length = length
            cur_cols = cols

        #if the chains that were added to equal length along the way are equiv to longest chain,
        # add them to the return list of consecutive 1's
        lines = list([cur_cols])
        for mark in equal_length:
            mark = list([mark])
            if len(mark) == cur_max_length:
                lines.append([mark])
        return lines

    #find_rect
    #a helper function that takes the row and the list of cols that are 1 on that row
    #Complexity: O(NxM)
    def find_rect(row,lines):
        nonlocal n,area

        #for each consecutive line of equal length
        for line in lines:
            length = len(line)
            cur_area = length

            #for each of the next rows
            i = row+1
            while i < n:
                valid = True
                #if there is every a zero in the line that should be equal to initial chain,
                # it's no longer a rectangle
                for j in line:
                    if mat[i][j] == 0:
                        valid = False

                #if still valid after checking current row, increment area by length of chain
                if valid:
                    cur_area += length
                    i += 1
                #if not valid, move out of while loop
                else:
                    i = n+1

            #checking with the nonlocal area to set the max area rectangle
            if cur_area > area:
                area = cur_area

    for i in range(n): #N
        ones = parse_row(mat[i]) #M
        find_rect(i,ones) #NxM --> N^2

    return area

### TESTS
mat = [[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
print(rectangle(mat)) #4 -- it works; low confidence though

### ADMIN SOLUTION
def infer_area(cache):
    max_area = 0
    for i in range(len(cache)):
        for j in range(i + 1, len(cache) + 1):
            current_rectangle = min(cache[i:j]) * (j - i)
            max_area = max(max_area, current_rectangle)
    return max_area


def largest_rectangle(matrix):
    n, m = len(matrix), len(matrix[0])
    max_so_far = 0

    cache = [0 for _ in range(m)]
    for row in matrix:
        for i, val in enumerate(row):
            if val == 0:
                cache[i] = 0
            elif val == 1:
                cache[i] += 1
        max_so_far = max(max_so_far, infer_area(cache))

    return max_so_far
