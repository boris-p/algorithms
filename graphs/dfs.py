import init


class Vertex:
    def __init__(self, value):
        self.explored = False
        self.index = None
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


# DFS to check if item exists in the graph
def checkIfItemExists(graph, vertex, lookupValue):
    # break condition
    if vertex.value == lookupValue:
        return True
    vertex.explored = True

    for e in vertex.edges:
        if e.destination.explored == False:
            # if we found the item return - we don't need to go any further
            if checkIfItemExists(graph, e.destination, lookupValue) == True:
                return True
    return False


def outerCheckIfItemExists(graph, vertex, lookupValue):
    itemExists = checkIfItemExists(graph, graph.vertices[0], lookupValue)
    message = 'found. nice!' if itemExists else 'sorry, no luck homebro'
    print('looking for {0}: {1}'.format(lookupValue, message))
    graph.resetExplored()


def topologiocalSort(graph, Vertex):
    Vertex.explored = True


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

outerCheckIfItemExists(graph, graph.vertices[0], 'o')
outerCheckIfItemExists(graph, graph.vertices[0], 's')
outerCheckIfItemExists(graph, graph.vertices[0], 'should not find value')
