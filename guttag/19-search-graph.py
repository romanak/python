class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest, weight = 1.0):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
        self.weight = weight
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->(' + str(self.getWeight()) + ')' + self.dest.getName()
               
class Digraph(object):
    """edges is a dict mapping each node to a list of its children"""
    def __init__(self):
        self.nodes = []
        self.edges = []
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if src not in self.nodes:
            self.nodes.append(src)
        if dest not in self.nodes:
            self.nodes.append(dest)
        self.edges.append(edge)
    def childrenOf(self, node):
        for edge in self.edges:
            if edge.getSource() == node:
                yield edge.getDestination()
    def hasNode(self, node):
        return node in self.nodes
    def getEdge(self, edge):
        for e in self.edges:
            if e == edge:
                return e
        raise NameError(edge)
    def getNode(self, name):
        for n in self.nodes:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for edge in self.edges:
            result = result + str(edge) + '\n'
        return result[:-1] #omit final newline

class Graph(Digraph):
    def __init__(self):
        Digraph.__init__(self)
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
    
def buildGraph(graphType):
    g = graphType()
    for name in range(6):
        g.addNode(Node(str(name)))
    g.addEdge(Edge(g.getNode('0'), g.getNode('1')))
    g.addEdge(Edge(g.getNode('1'), g.getNode('2')))
    g.addEdge(Edge(g.getNode('2'), g.getNode('3')))
    g.addEdge(Edge(g.getNode('2'), g.getNode('4')))
    g.addEdge(Edge(g.getNode('3'), g.getNode('4')))
    g.addEdge(Edge(g.getNode('3'), g.getNode('5')))
    g.addEdge(Edge(g.getNode('0'), g.getNode('2')))
    g.addEdge(Edge(g.getNode('1'), g.getNode('0')))
    g.addEdge(Edge(g.getNode('3'), g.getNode('1')))
    g.addEdge(Edge(g.getNode('4'), g.getNode('0')))
    return g

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 

def DFS(graph, start, end, toPrint = False, path=[], shortest=None):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, toPrint, path, shortest)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest

def BFS(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    pathQueue = [[start]]
    while len(pathQueue) != 0:
        # get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        # as soon as end is found, return the path that led to it
        if lastNode == end:
            return tmpPath
        # add children of the current path to the pathQueue
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

def shortestPath(graph, start, end, searchAlgorithm, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return searchAlgorithm(graph, start, end, toPrint)

def testSP(graph, source, destination, searchAlgorithm, toPrint):
    
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), searchAlgorithm, toPrint)
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)

g = buildGraph(Digraph)
testSP(g, '0', '5', DFS, True)
print()
testSP(g, '0', '5', BFS, True)