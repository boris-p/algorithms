import init


class Vertex:
    def __init__(self, value):
        self.explored = False
        self.index = None
        self.edges = []
        self.value = value


class Edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class AdjacencyList:
    def __init__(self, vertices, edges):
        self.vertices = []
        self.edges = []
        for v in vertices:
            self.vertices.append(Vertex(v[1]))
        for e in edges:
            edge = Edge(self.vertices[e[0]], self.vertices[e[1]])
            self.vertices[e[0]].edges.append(edge)
            self.vertices[e[1]].edges.append(edge)
            self.edges.append(edge)

    def resetExplored(self):
        for v in self.vertices:
            v.explored = False


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

getMaxDepth(graph)
getShortestPath(graph, 's')
graph.resetExplored()
getShortestPath(graph, 'a')
graph.resetExplored()
getShortestPath(graph, 'c')
graph.resetExplored()
getShortestPath(graph, 'o')
