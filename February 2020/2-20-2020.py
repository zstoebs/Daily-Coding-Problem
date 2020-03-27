"""
@author Zach Stoebner
@date 2-20-2020
@details You are given an array representing the heights of neighboring buildings on a city street,
from east to west. The city assessor would like you to write an algorithm that returns how many of
these buildings have a view of the setting sun, in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since the top floors of the
buildings with heights 8, 6, and 1 all have an unobstructed view to the west.

Can you do this using just one forward pass through the array?
"""

# can put them into a aux array that should have all valid buildings in descending order

# clearview
# Returns number of buildings that have a clear view of the sunset
# Complexity: O(N)
def clearview(heights: list):

    aux = reversed(heights)
    mx = 0
    count = 0

    for height in heights:
        if height > mx:
            mx = height
            count += 1

    return count

### ADMIN SOLUTION
def sunset_views(buildings):
    views = []
    highest = 0

    for building in buildings:
        while views and views[-1] <= building:
            views.pop()
        views.append(building)

    return len(views)
