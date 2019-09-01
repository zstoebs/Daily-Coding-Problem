"""
Author: Zach Stoebner
Created on: 8-19-2019
Descrip:

You are in an infinite 2D grid where
you can move in any of the 8 directions.

You are given a sequence of points and
the order in which you need to cover the
points. Give the minimum number of steps
in which you can achieve it. You start
from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1).
It takes one more step to move from (1, 1) to (1, 2).

"""
"""
8 directions:
 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
"""

#know that points don't have to be one-step away from each other
#can determine Euclidean distance from difference of corr. entries of coords
#only need abs value to determine steps
#taking diagonal routes is quicker than taking component routes
#knowing Euclidean distance:
# abs(Xdist - Ydist) + min([Xdist,Ydist])
# --> minimum of comps. equals number of diagonal steps s.t. Xdist = Ydist
# --> abs difference equals number of extra steps along Xdist or Ydist

#minimum_steps
#Note: returns minimum number of steps to pass through all points
#Complexity:
def minimum_steps(path):

    assert(len(path) > 0)

    #distance
    #Note: returns a tuple of x and y distance to reach point
    def distance(a,b):
        return tuple([abs(b[0]-a[0]),abs(b[1]-a[1])])

    #finding steps between sequential points
    steps = 0
    prev = path[0]
    for point in path[1:]:

        dist = distance(prev,point)
        steps += abs(dist[0] - dist[1]) + min(dist)
        prev = point

    return steps

### TESTS
path = [(0, 0), (1, 1), (1, 2)]
print(minimum_steps(path))
"""
.----.-
      |-
       |-
        |--.

"""
path = [(0,0),(5,0),(11,-3)] #11 steps
print(minimum_steps(path))

### ADMIN SOLUTION
"""
Java implementation:

// X and Y co-ordinates of the points in order.
// Each point is represented by (X.get(i), Y.get(i))
public int coverPoints(ArrayList<Integer> X, ArrayList<Integer> Y) {
    int totalDistance = 0;
    for (int i = 1; i < X.size(); i++) {
        totalDistance += getDistance(X.get(i - 1), Y.get(i - 1), X.get(i), Y.get(i));
    }
    return totalDistance;
}

private int getDistance(int x1, int y1, int x2, int y2) {
    return (int)Math.max(Math.abs(x2 - x1), Math.abs(y2 - y1));
}

"""
