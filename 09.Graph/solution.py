from Stack_Queue import *

class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adj = [[0 for i in range(vertex)] for j in range(vertex)]
        
    def AddEdge(self, src, dest):
        self.adj[src][dest] = 1
        self.adj[dest][src] = 1

    def PrintMatrix(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                print(self.adj[i][j], end =' ')
            print()

    def GetNeighbours(self, vertex):
        neighbours = []
        for i in range(len(self.adj[vertex])):
            if self.adj[vertex][i] == 1:
                neighbours.append(i)
        return neighbours

    def BFS(self, src):
        neigh = []
        visited = []
        q = Queue(self.vertex)
        q.Enqueue(src)
        visited.append(src)  # mark source as visited

        while not q.IsEmpty():
            x = q.Dequeue()
            print(f'Visited: {x}')
            neigh = self.GetNeighbours(x)
            
            for n in neigh:
                if n not in visited:
                    q.Enqueue(n)
                    visited.append(n)
            
    def DFS(self, src):
        neigh = []
        visited = []
        s = Stack(self.vertex)
        s.Push(src)
        visited.append(src)  # mark source as visited
        
        while not s.IsEmpty():
            x = s.Pop()
            print(f'Visited: {x}')
            neigh = self.GetNeighbours(x)
            
            for n in neigh:
                if n not in visited:
                    s.Push(n)
                    visited.append(n)

                    
obj = Graph(5)
obj.AddEdge(0,1)
obj.AddEdge(0,2)
obj.AddEdge(1,2)
obj.AddEdge(1,3)
obj.AddEdge(2,3)
obj.AddEdge(2,4)
obj.AddEdge(3,4)
obj.DFS(1)
