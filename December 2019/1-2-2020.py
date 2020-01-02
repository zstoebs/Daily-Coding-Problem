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
"""

import math

# inside_polygon
# Returns bool if point is in polygon
# Complexity: O(n)
def inside_polygon(points: list, p: tuple):

    slopes = {point: [] for point in points}

    # finding slopes
    n = len(points)
    for i in range(n):
        point = points[i]
        next_point = None
        if i == n-1:
            next_point = points[0]
        else:
            next_point = points[i+1]

        if i == 0:
            prev_point = points[-1]
        else:
            prev_point = points[i-1]

        try:
            slope_next = (next_point[1] - point[1]) / (next_point[0] - point[0])
        except ZeroDivisionError:
            slope_next = math.inf
        try:
            slope_prev = (prev_point[1] - point[1]) / (prev_point[0] - point[0])
        except ZeroDivisionError:
            slope_prev = math.inf
        try:
            slope_p = (p[1] - point[1]) / (p[0] - point[0])
        except ZeroDivisionError:
            slope_p = math.inf

        vertices[point].append(slope_next)
        vertices[point].append(slope_prev)
        vertices[point].append(slope_p)


    # finding a connection that matches the relative coordinate of the point to the vertex
    for vertex in vertices.keys():
        connections = vertices[vertex]

    ## i don't know
