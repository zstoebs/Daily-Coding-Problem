"""
@author Zach Stoebner
@date 1-2-2020
@details You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN)
representing a polygon. You can assume these points are given in order; that is,
you can construct the polygon by connecting point 1 to point 2, point 2 to point 3,
and so on, finally looping around to connect point N to point 1.

Determine if a new point p lies inside this polygon. (If p is on the boundary of the
polygon, you should return False).
"""
"""
Notes:
1. Each point connects to two others
2. A point is in the polygon if it is within the angle of each vertex

How to find the angle of a vertex?
From a horizontal, take the inverse tangent of the y-distance / x-distance.
If y_2 > y_1, use the vertical as a reference, else use the horizontal.

Or the slope from the vertex to the point must be in the range of the slopes to the connections
for each vertex.

Also in any one direction the horizontal beyond the point should intersect an odd number of edges.
https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
"""

# inside_polygon
# Returns bool if point is in polygon
# Complexity: O(n)
def inside_polygon(points: list, p: tuple):

    edge_lines = []

    max_y = max(points,key=lambda x: x[1])
    min_y = min(points,key=lambda x: x[1])

    max_x = max(points,key=lambda x: x[0])
    min_x = min(points,key=lambda x: x[0])

    n = len(points)

    # finding slopes, horizontal and vertical ranges
    for i in range(n):
        point = points[i]

        if i == n-1:
            next_point = points[0]
        else:
            next_point = points[i+1]

        try:
            slope_next = (next_point[1] - point[1]) / (next_point[0] - point[0])
        except ZeroDivisionError:
            slope_next = None

        y_inter = point[1] - slope_next*point[0] if slope_next not is None else None

        low = min([point,next_point],key=lambda x: x[1])
        high = max([point,next_point],key=lambda x: x[0])
        edge_lines.append(tuple([slope_next,y_inter,low,high]))

    # checking if point falls within height and width of entire polygon
    x = p[0]
    y = p[1]
    if not (x > min_x and x < max_x and y > min_y and y < max_y):
        return False

    count = 0
    for line in edge_lines:
        slope = line[0]
        inter = line[1]
        low = line[2]
        high = line[3]
        rel_x = (y - inter) / slope
        if y > low and y < high:
            if rel_x > x:
                count += 1

            # if it sits on an edge
            if rel_x == x:
                return False

    return count % 2 != 0


#### ADMIN SOLUTION
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def create_sides(points):
    sides = [(points[-1], points[0])] + list(zip(points, points[1:]))
    return [(Point(*a), Point(*b)) for (a, b) in sides]

def intersects(p, side):
    p1, p2 = side

    # Get the slope and intercept of the side. Check for zero and undefined slopes.
    dy, dx = (p2.y - p1.y), (p2.x - p1.x)
    if dx == 0.0:
        return 1 if p.x < p1.x and min(p1.y, p2.y) <= p.y <= max(p1.y, p2.y) else 0
    if dy == 0.0:
        return 0

    slope = dy / dx
    intercept = p1.y - slope * p1.x

    # Plug in the y-coordinate of our point and solve for the intersection.
    intersection = Point((p.y - intercept) / slope, p.y)

    # Check to see if the intersection is valid before returning.
    if p.x <= intersection.x and min(p1.y, p2.y) <= intersection.y <= max(p1.y, p2.y):
        return 1
    else:
        return 0

def check_inside(p, polygon):
    p = Point(*p)

    count = 0
    sides = create_sides(polygon)
    for side in sides:
        count += intersects(p, side)

    if count % 2 == 1:
        return True
    else:
        return False
