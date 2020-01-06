"""
@author Zach Stoebner
@date 1-5-2020
@details One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

All of its keys must be distinct.
It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
"""

# unlock_patterns
# Returns the count of the total number of valid unlock patterns
# Complexity: O(N^2)
def unlock_patterns(N: int):

    assert 1 <= N and N <= 9

    patterns = set()
    keypad = [[7,8,9],
                [4,5,6],
                [1,2,3]]

    # checks if the location fits the constraints
    def check_valid(start: tuple, cur_pattern: str):
        nonlocal keypad

        if not (start[0] >= 0 and start[0] < 3 and start[1] >= 0 and start[1] < 3):
            return False

        num = keypad[start[0]][start[1]]

        return cur_pattern.count(str(num)) == 0

    # gets next set of locations
    def get_next_locs(start: tuple, cur_pattern: str):

        next = []
        up = down = left = right = up_left = up_right = down_left = down_right = False

        for i in range(1,3):
            for j in range(1,3):

                up_loc = (start[0]-i,start[1])
                if not up and check_valid(up_loc,cur_pattern):
                    next.append(up_loc)
                    up = !up

                down_loc = (start[0]+i,start[1])
                if not down and check_valid(down_loc,cur_pattern):
                    next.append(down_loc)
                    down = !down

                left_loc = (start[0],start[1]-j)
                if not left and check_valid(left_loc,cur_pattern):
                    next.append(left_loc)
                    left = !left

                right_loc = (start[0],start[1]+j)
                if not right and check_valid(right_loc,cur_pattern):
                    next.append(right_loc)
                    right = !right

                ul_loc = (start[0]-i,start[1]-j)
                if not up_left and check_valid(ul_loc,cur_pattern):
                    next.append(ul_loc)
                    up_left = !up_left

                ur_loc = (start[0]-i,start[1]+j)
                if not up_right and check_valid(ur_loc,cur_pattern):
                    next.append(ur_loc)
                    up_right = !up_right

                dl_loc = (start[0]+i,start[1]-j)
                if not down_left and check_valid(dl_loc,cur_pattern):
                    next.append(dl_loc)
                    down_left = !down_left

                dr_loc = (start[0]+i,start[1]+j)
                if not down_right and check_valid(dr_loc,cur_pattern):
                    next.append(dr_loc)
                    down_right = !down_right
        return next

    # paths
    # Finds all the paths given a start location
    # Complexity: O(N^2)
    def paths(start: tuple, cur_pattern: str = ""):
        nonlocal patterns, keypad, N

        num = keypad[start[0]][start[1]]

        #add to cur_pattern
        cur_pattern += str(num)

        # if cur_pattern is of size N, add it to set
        if len(cur_pattern) == N:
            patterns.add(cur_pattern)
        # otherwise call the next set of recursive path finds
        else:
            next = get_next_locs(start,cur_pattern)
            for start in next:
                paths(start,cur_pattern)

    # adding paths from each start location
    for i in range(3):
        for j in range(3):
            paths(tuple([i,j]))


    return len(patterns)

#print(unlock_patterns(3)) # 184
#print(unlock_patterns(9))
#print(unlock_patterns(2))
print(unlock_patterns(1))
### Takes a long time
