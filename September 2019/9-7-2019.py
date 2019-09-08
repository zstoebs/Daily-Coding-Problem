"""
@author Zach Stoebner
@date 9-7-2019
@details Given a set of closed intervals,
  find the smallest set of numbers that covers
  all the intervals. If there are multiple smallest
  sets, return any of them.

  For example, given the intervals
  [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers
  that covers all these intervals is {3, 6}.
"""
#best to check edges of interval
#could interpret these intervals as a dense representation of a graph
# via a dictionary / adjacency list
#sets that are contained within other sets don't matter

#smallest_coverage
#Note: returns the smallest set that covers all intervals
#Complexity: O(n^2) time
def smallest_coverage(intervals):

    crit_ints = intervals.copy()


    #removing non-critical intervals and finding overall range
    for i in range(len(intervals)):
        for j in range(i+1,len(intervals)):
            if intervals[j][0] >= intervals[i][0] and intervals[j][1] <= intervals[i][1]:
                crit_ints.remove(intervals[j])


    #converting to a list and sorting based on first element
    crit_ints.sort(key=(lambda elem: elem[0]))

    pivot = None
    i = 0
    both = False
    length = len(crit_ints)
    cover_nums = set([])
    while i < length:
        for edge in crit_ints[i]:
            j = i+1
            if j < length:
                next_int = crit_ints[j]
                if edge >= next_int[0] and edge <= next_int[1]:
                    pivot = edge
        cover_nums.add(pivot)
        i += 1

    return cover_nums

inters = [[0, 3], [2, 6], [3, 4], [6, 9]]
print(smallest_coverage(inters))
inters = [[0, 3], [2, 6], [3, 4]]
print(smallest_coverage(inters))
