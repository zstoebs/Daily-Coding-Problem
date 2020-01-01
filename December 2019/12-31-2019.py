"""
@author Zach Stoebner
@date 12-31-2019
@descrip Recall that the minimum spanning tree is the subset of edges of a tree that
connect all its vertices with the smallest possible total edge weight. Given an
undirected graph with weighted edges, compute the maximum weight spanning tree.
"""

"""
This problem is the inverse of Prim's or Kruskal's MST in that the greedy choice takes the
greatest weighted edge available.
"""



# max_ST
# Computes the maximum spanning tree (via Kruskal's) of a graph (adj list)
# Complexity: O(ElogV)
def max_ST(graph: dict):

    """
    Example structure of adj list graph:
    {
    'a': [('b',4),('c',3)],
    'b': [('a',4),('c',1)],
    'c': [('a',3),('b',1)]
    }
    """

    def find_set(sets,vertex):
        for set in sets.keys():
            if set == vertex or vertex in sets[set]:
                return set

    def union_set(sets,s1,s2):
        assert s1 in sets.keys() and s2 in sets.keys()

        deg1 = len(sets[s1])
        deg2 = len(sets[s2])
        root = s1 if deg1 >= deg2 else s2
        absorb = s2 if deg1 >= deg2 else s1
        sets[root].append(absorb)
        sets[root].extend(sets[absorb])
        del sets[absorb]

    desc_edges = []

    # getting edges --> O(V+E)
    for vertex in graph.keys():
        v_i = vertex
        for edge in graph[vertex]:
            v_j = edge[0]
            w = edge[1]
            edge_tuple = (v_i,v_j,w) if v_i < v_j else (v_j,v_i,w)
            if edge_tuple not in desc_edges:
                desc_edges.append(edge_tuple)

    # sorting edges in descending order --> O(ElogV)
    desc_edges.sort(key=lambda edge: edge[2],reverse=True)

    sets = {vertex: [] for vertex in graph.keys()}
    max_span = []

    for edge in desc_edges:
        s1 = find_set(sets,edge[0])
        s2 = find_set(sets,edge[1])
        if s1 != s2:
            max_span.append(edge)
            union_set(sets,s1,s2)

    return max_span

### TESTS
t1 = {
    'a': [('b',4),('c',3)],
    'b': [('a',4),('c',1)],
    'c': [('a',3),('b',1)]
    }
print(max_ST(t1)) # [('a', 'b', 4), ('a', 'c', 3)]

### ADMIN SOLUTION
class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n

    def find(self, v):
        root = v
        while root != self.parents[root]:
            root = self.parents[root]

        step = v
        while step != root:
            step, self.parents[step] = self.parents[step], root
        return root

    def join(self, v1, v2):
        s1 = self.find(v1)
        s2 = self.find(v2)

        small, big = (s1, s2) if self.sizes[s1] < self.sizes[s2] else (s2, s1)
        self.parents[small] = big
        self.sizes[big] += self.sizes[small]

def max_spanning_tree(graph):
    """
    Keep adding edges of maximal weight if they join together disjoint sets of vertices.
    Graph is a dict containing a list of vertices and a list of (v1, v2, weight) edges.
    """
    tree = set()
    n = len(graph['vertices'])
    ds = DisjointSet(n)
    graph['edges'].sort(key=lambda x: x[2], reverse=True)

    for edge in graph['edges']:
        if ds.find(edge[0]) != ds.find(edge[1]):
            tree.add(edge)
            ds.join(edge[0], edge[1])

    return tree if len(tree) == n - 1 else None
