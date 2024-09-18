class Node:
    def __init__(self, name) -> None:
        self.name = name
    
    def getName(self):
        return self.name
    def __str__(self) -> str:
        return self.name
    
class Edge:
    def __init__(self,src:Node,dest:Node) -> None:
        self.src = src
        self.dest = dest
    
    def getDestination(self):
        return self.dest
    
    def getSource(self):
        return self.src
    
    def __str__(self) -> str:
        return self.src.getName() + '->' + self.dest.getName()

class DiGraph:
    def __init__(self) -> None:
        self.edges = {}

    def addNode(self,node:Node):
        if node in self.edges:
            raise ValueError("Duplicate node")
        else:
            self.edges[node] = []

    def addEdge(self,edge:Edge):
        src,dest = edge.getSource(), edge.getDesination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)

    def childOf(self,node: Node):
        return self.edges[node]

    
    def hasNode(self,node: Node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self,name):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]

class Graph(DiGraph):
    def addEdge(self, edge: Edge):
        DiGraph.addEdge(self,edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        DiGraph.addEdge(self,rev)
        return super().addEdge(edge)

