"""
@author Zach Stoebner
@date 1-21-2020
@details The transitive closure of a graph is a measure of which vertices are reachable from
other vertices. It can be represented as a matrix M, where M[i][j] == 1 if there is a path
between vertices i and j, and otherwise 0.

For example, suppose we are given the following graph in adjacency list form:

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
The transitive closure of this graph would be:

[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
Given a graph, find its transitive closure.
"""

# graph_closure
# Returns the adj matrix closure of an adj list graph
# Complexity: O(V^2)
def graph_closure(graph: list):

    v = len(graph)
    mat = [[0 for _ in range(v)] for _ in range(v)]

    # diagonals connect to each other
    for i in range(v):
        mat[i][i] = 1

    # subroutine for exploring paths
    def find_paths(start,cur):
        nonlocal mat

        if start == cur or len(graph[cur]) == 0:
            return
        else:
            for next in graph[cur]:
                if mat[start][next] != 1:
                    mat[start][next] = 1
                    find_paths(start,next)

    for lst in graph:
        others = lst[1:]
        # assuming there is a first vertex in the list
        start = lst[0]
        for adj in others:
            find_paths(start,adj)

    return mat

### TESTS
g1 = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
print(graph_closure(g1)) # [[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
