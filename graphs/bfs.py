#!/usr/bin/python
class QueueAsArr:
    def __init__(self):
        self.queueList = []

    def push(self, value):
        self.queueList.insert(0, value)

    def isEmpty(self):
        if len(self.queueList) == 0:
            return True
        else:
            return False

    def pop(self):
        listLength = len(self.queueList)
        if listLength == 0:
            print("queue empty")
            return None
        else:
            item = self.queueList[listLength - 1]
            del self.queueList[listLength - 1]
            return item


class Edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Vertex:
    def __init__(self, value):
        self.explored = False
        self.index = None
        self.edges = []
        self.value = value


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


def getMaxDepth(graph):
    q = QueueAsArr()
    firstElement = graph.vertices[0]
    firstElement.index = 1
    q.push(graph.vertices[0])

    maxIndex = 0
    while q.isEmpty() == False:
        v = q.pop()
        for e in v.edges:
            # how do we know better that the node we left is p1 or p2, this seems like a dumb check
            secondVertex = e.p1 if e.p1 != v else e.p2
            if secondVertex.explored == False:
                secondVertex.explored = True
                newIndex = v.index + 1
                if newIndex > maxIndex:
                    maxIndex = newIndex
                secondVertex.index = v.index + 1
                q.push(secondVertex)
    print('largest index is', maxIndex)


def getShortestPath(graph, lookupVal):
    q = QueueAsArr()
    firstElement = graph.vertices[0]
    firstElement.index = 1
    q.push(graph.vertices[0])

    maxIndex = 0
    while q.isEmpty() == False:
        v = q.pop()
        if v.value == lookupVal:
            print('value found in depth', v.index)
            return
        for e in v.edges:
            # how do we know better that the node we left is p1 or p2, this seems like a dumb check
            secondVertex = e.p1 if e.p1 != v else e.p2
            if secondVertex.explored == False:
                secondVertex.explored = True
                newIndex = v.index + 1
                if newIndex > maxIndex:
                    maxIndex = newIndex
                secondVertex.index = v.index + 1
                q.push(secondVertex)
    print('value not found in the graph')


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
