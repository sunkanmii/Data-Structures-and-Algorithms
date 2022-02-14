from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addNode(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v):
        visited = set()

        self.DFSUtil(v, visited)
    def DFSUtil(self, u, visited):
        visited.add(u)
        print(u, end=" ")

        for nextPointer in self.graph[u]:
            if nextPointer not in visited:
                self.DFSUtil(nextPointer, visited)

g = Graph()
g.addNode(0, 1)
g.addNode(0, 2)
g.addNode(1, 2)
g.addNode(1, 3)
g.addNode(2, 0)
g.addNode(2, 3)
g.addNode(3, 3)
print ("Following is Breadth First Traversal (starting from vertex 2):")
g.DFS(2)