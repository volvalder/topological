from collections import defaultdict

# Topological sort

class Graph:
    # pairs List[List[str]]
    def __init__(self, pairs):
        self.adjList = defaultdict()
        self.q = []
        for pair in pairs:
            self.addNode(pair[0])
            self.addNode(pair[1])
            self.addEdge(pair[0], pair[1])
    
    def addNode(self, n):
        if n not in self.adjList:
            self.adjList[n] = []
    
    def addEdge(self, n, e):
        self.adjList[n].append(e)
    
    def dfs(self, v, visited = set()):
        visited.add(v)
        for neighbor in self.adjList[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
                # all that is different vs regular dfs
                # is that we enqueue vertices on the way back
                self.q.append(neighbor)
    
    def topological(self, target):
        self.dfs(target)
        print(self.q[::-1])