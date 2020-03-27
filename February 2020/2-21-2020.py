"""
@author Zach Stoebner
@date 2-21-2020
@details The skyline of a city is composed of several buildings of various widths and heights,
possibly overlapping one another when viewed from a distance. We can represent the buildings using
an array of (left, right, height) tuples, which tell us where on an imaginary x-axis a building
begins and ends, and how tall it is. The skyline itself can be described by a list of (x, height)
tuples, giving the locations at which the height visible to a distant observer changes, and each
new height.

Given an array of buildings as described above, create a function that returns the skyline.

For example, suppose the input consists of the buildings [(0, 15, 3), (4, 11, 5), (19, 23, 4)].
In aggregate, these buildings would create a skyline that looks like the one below.

     ______
    |      |        ___
 ___|      |___    |   |
|   |   B  |   |   | C |
| A |      | A |   |   |
|   |      |   |   |   |
------------------------
As a result, your function should return [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)]
"""

# skyline
# Returns a skyline given the building dimensions
# Complexity: O(n*L)
def skyline(buildings: list):

    xmin = min(buildings, lambda x: x[0])
    xmax = max(buildings, lambda x: x[1])

    starts = [b for b in buildings]
    starts.sort(key=lambda x: x[0]) #O(nlogn)

    chg_pts = []
    going = []

    height 0
    for pos in range(xmin,xmax+1):

        start? = False
        mx = -1
        # if the start of a building is found, add it to the going list
        if len(starts) != 0:
            while starts[0][0] == pos:
                mx = starts[0][2] if starts[0][2] > mx else mx
                going.append(starts.pop(0))
                flag1 = True

        end? = False
        to_pop = []
        for i, build in enumerate(going):
            if build[1] == pos:
                to_pop += i
                flag2 = True

        for i in reversed(to_pop):
            going.pop(i)

        # if a building starts and current tallest, then it's a change point
        if start?:
            if mx > height:
                height = mx
                chg_pts.append(tuple([pos,height]))
        # if a building didn't start but one ended, then find the drop height
        elif end?:
            drop_to = 0
            for build in going:
                drop_to = build[2] if build[2] > drop_to else drop_to

            if drop_to != height:
                height = drop_to
                chg_pts.append(tuple([pos,height]))

    return chg_pts

### TESTS
print(skyline([(0, 15, 3), (4, 11, 5), (19, 23, 4)]))
