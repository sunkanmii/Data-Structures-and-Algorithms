from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addNode(self, v, u):
        self.graph[v].append(u)

    
    def BFS(self, v):
        visited = [False] * (max(self.graph) + 1)

        queue = []
        queue.append(v)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            visited[s] = True
            for node in self.graph[s]:
                if visited[node] is False:
                    visited[node] = True
                    queue.append(node)
g = Graph()
g.addNode(0, 1)
g.addNode(0, 2)
g.addNode(1, 2)
g.addNode(2, 0)
g.addNode(2, 3)
g.addNode(3, 3)

g.BFS(2)
