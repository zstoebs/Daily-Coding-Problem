"""
@author Zach Stoebner
@date 1-7-2020
@details In academia, the h-index is a metric used to calculate the impact of a researcher's
papers. It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each. If there are
multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5].
Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
"""

# h_index
# Calculates the h_index given a list of the citations of each paper
# Complexity: O(nlogn)
def h_index(cites: list):

    cites.sort()
    n = len(cites)
    h = 0
    for i in range(n):
        cite = cites[i]
        h = cite if n+1-cite >= cite else h

    return h

### TESTS
t1 = [4, 3, 0, 1, 5]
print(h_index(t1)) #3
t2 = [1,2,3,8,9,10]
print(h_index(t2)) #3
t3 = [1,2,5,8,9,10]
print(h_index(t3)) #2
