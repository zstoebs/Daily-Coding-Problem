"""
@author Zach Stoebner
@date 10-8-2019
@descrip Given a list of points, a central point, and an integer k,
find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)],
the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
"""

# Can compute the distances of each of the points from the central point,
# then sort and just take the first k corr. points

from math import sqrt

#k_nearest_neighbors
#Finds the k nearest points to a center point from a domain list
#Complexity: O(nlogn) time
def k_nearest_neighbors(points=list([]),center=tuple([]),k=0):

    #compute_distance
    #helper function to compute the distance of a point from the center
    def compute_distance(point=tuple([])):
        return sqrt((center[0] - point[0])**2 + (center[1] - point[1])**2)

    distances = list([])
    lookup = dict([])
    for point in points: #O(n)
        distance = compute_distance(point)
        distances.append(distance)
        if distance not in lookup.keys():
            lookup[distance] = [point]
        else:
            lookup[distance].append(point)

    distances.sort() #O(nlogn)
    distances = distances[:k] #O(n)?
    ret = list([])
    for dist in distances: #O(n)
        ret.append(lookup[dist].pop())

    return ret

### TESTS
test = [(0, 0), (5, 4), (3, 1)]
center = tuple([1,2])
k = 2
print(k_nearest_neighbors(test,center,k)) # [(3, 1), (0, 0)]
