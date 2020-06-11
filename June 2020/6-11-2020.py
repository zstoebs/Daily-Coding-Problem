"""
@author Zach Stoebner
@date 6-11-2020
@details You are given a list of jobs to be done, where each job is represented by a start time and end time. Two jobs are compatible if they don't overlap. Find the largest subset of compatible jobs.
"""

# This problem is related to a topological sort problem
# Can be rewritten as the number line set problem
# We know that this problem has optimal substructure so |s| will be maximal

# creates a max subset of non-overlapping segments
# Complexity: O(n)
def create_S(segs: list):

    n = len(segs)
    if n < 2:
        return segs

    # sort based on start points
    segs.sort(key=(lambda x: x[0]))
    Ss = list()
    i = 0
    while i < n:

        # if last element and didn't get popped previously then it's safe b/c it doesn't overlap with anything that's in S
        if len(segs) == 1:
            Ss.extend(segs)
        # if there is no overlap b/w s1 and s2,
        # then s1 can be added to S b/c s3's start point must be greater
        # than s2's start point
        elif segs[1][0] >= segs[0][1]:
            Ss.append(segs[0])
            segs.pop(0)
        # otherwise s1 and s2 overlap
        else:
            # if s1 encompasses s2 then s1 should be eliminated
            # b/c s3 either starts in s1, starts in s2 which in this case
            # starts in s1, or starts beyond s1 which starts
            # beyond s2 in this case --> if s1 can be in the optimal solution
            # then so can s2, but s2 may also be in an optimal solution that
            # s1 couldn't be in b/c it overlaps some s00 later on
            if segs[1][1] < segs[0][1]:
                segs.pop(0)
            else:
                segs.pop(1)

        i += 1

    return Ss

### TESTS
x1 = [(1,1),(2,2),(3,3),(4,7),(7,9)]
print(create_S(x1))
x2 = [(10,11),(10,12),(10,13)]
print(create_S(x2))
x3 = [(0, 6),
(1, 4),
(3, 5),
(3, 8),
(4, 7),
(5, 9),
(6, 10),
(8, 11)]
print(create_S(x3))
"""
[(3, 9), (10, 15)]
[(1, 1), (2, 2), (3, 3), (4, 7)]
[(10, 11)]
[(1, 4), (4, 7), (8, 11)]
"""
