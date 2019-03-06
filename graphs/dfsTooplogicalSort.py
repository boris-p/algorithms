import init


class Vertex:
    def __init__(self, value):
        self.explored = False
        self.label = None  # for the topological sort
        self.edges = []
        self.value = value


class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


class AdjacencyList:
    def __init__(self, vertices, edges):
        self.vertices = []
        self.edges = []
        for v in vertices:
            self.vertices.append(Vertex(v[1]))
        for e in edges:
            # create a new edge with a source and destination vertex
            edge = Edge(self.vertices[e[0]], self.vertices[e[1]])
            # add source edges to the array of edges of each vertex
            self.vertices[e[0]].edges.append(edge)

            self.edges.append(edge)

    def resetExplored(self):
        for v in self.vertices:
            v.explored = False
            v.label = None


# DFS for topologically sorting acyclical connected graphs
def tolologicalSortOuter(graph):
    # making this in an array to pass it be reference
    currentLabel = [len(graph.vertices)]
    for v in graph.vertices:
        if v.explored == False:
            topologiocalSort(v, currentLabel)


def topologiocalSort(vertex, label):
    vertex.explored = True
    for e in vertex.edges:
        if e.destination.explored == False:
            topologiocalSort(e.destination, label)
    vertex.label = label[0]
    label[0] -= 1


# vertices indexes
# index, value, other linked vertices
# writing the index to make the connection between the vertices more explicit - id doesn't really do anything
vertices = [[0, 's'],
            [1, 'a'],
            [2, 'b'],
            [3, 'c'],
            [4, 'd'],
            [5, 'o']
            ]
edges = [[0, 1],
         [0, 2],
         [1, 3],
         [2, 3],
         [3, 4],
         [2, 4],
         [3, 5],
         [4, 5],
         ]
graph = AdjacencyList(vertices, edges)
tolologicalSortOuter(graph)


vertices = [[0, 's'],
            [1, 'a'],
            [2, 'b']
            ]
edges = [[0, 1],
         [2, 1]
         ]

graph = AdjacencyList(vertices, edges)
tolologicalSortOuter(graph)
print(graph)
