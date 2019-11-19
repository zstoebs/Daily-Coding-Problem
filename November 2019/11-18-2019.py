"""
@author Zach Stoebner
@date 11-18-2019
@descrip Given a collection of intervals, find the minimum number of intervals
you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last
interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
"""

# This problem has shown up twice in the past couple of weeks for CS3250-Algo
# Starting by sorting by start points (or end points) and then choose by end points and pop any
# that overlap with the last added until the next valid interval is found

#count_removals
#Counts removals of intervals s.t. the remaining are non-overlapping (greedy)
#Modified from original code which created a set of non-overlapping intervals from input
#Complexity: O(n)
def count_removals(segs=list()):

    n = len(segs)
    assert n >= 2

    # sort based on start points
    segs.sort(key=(lambda x: x[0]))
    Ss = list()
    i = 0
    pops = 0
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
            if segs[1][1] <= segs[0][1]:
                segs.pop(0)
            else:
                segs.pop(1)
            pops += 1

        i += 1

    return pops

### TESTS
t1 = [(7, 9), (2, 4), (5, 8)]
print(count_removals(t1)) #1

###ADMIN SOLUTION
from math import inf

def non_overlapping_intervals(intervals):
    current_end = -inf
    overlapping = 0

    for start, end in sorted(intervals, key=lambda i: i[1]):
        if start >= current_end:
            current_end = end
        else:
            overlapping += 1
    return overlapping
