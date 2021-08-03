class Vertex:
    def __init__(self, value):
        self.value = value     # vertex number
        self.dist = float('inf')
        self.pi = value
        self.visited = False


# Min Priority Queue
class PriorityQueue:
    def __init__(self):
        self.data = []
        
    def IsEmpty(self):
        return len(self.data)==0
    
    def Enqueue(self, v):
        # v will be object of vertex
        self.data.append(v)
        
    def Dequeue(self):
        removed = self.data[0]
        self.data.remove(removed)
        return removed
    
    def ExtractMin(self):
        Min = self.__FindMin()
        rem = self.data[Min]
        self.data.remove(rem)
        return rem
    
    def __FindMin(self):
        Min = self.data[0]
        loc = 0
        for i in range(len(self.data)):
            if self.data[i].dist < Min.dist:
                Min = self.data[i]
                loc = i
        return loc


class DGraph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.CostMatrix = [[0 for i in range(vertex)] for j in range(vertex)]

    def AddDirectedEdges(self, src, dest, cost):
        self.CostMatrix[src][dest] = cost
        
    def GetDirectedNeighbours(self, source):
        neigh = []
        for i in range(self.vertex):
            if self.CostMatrix[source][i] > 0:
                neigh.append(i)
        return neigh
    
    def DijkstraShortestPath(self,source):
        
        # initialize empty list for vertex objects
        cost = []
        
        # initialize p-queue
        q = PriorityQueue()
        
        # create vertex objects
        for i in range(self.vertex):
            cost.append(Vertex(i))
        
        # set distances from src to vertex infinity
        for i in range(self.vertex):
            cost[i].dist = float('inf')
        
        # set source to source distance 0
        cost[source].dist = 0
        
        # enqueue the cost list objects
        for i in range(self.vertex):
            q.Enqueue(cost[i])
            
        # visit 
        while not q.IsEmpty():
            Min = q.ExtractMin()
            Min.visited = True
            neighbours = self.GetDirectedNeighbours(Min.value)
            
            for i in neighbours:
                if cost[i].visited == False and cost[i].dist > Min.dist + self.CostMatrix[Min.value][i]:
                    cost[i].dist = Min.dist + self.CostMatrix[Min.value][i]
                    cost[i].pi = Min.value
                    
        for j in cost:
            print(j.value, j.dist, j.pi)
            

# Driver code
d = DGraph(5)
d.AddDirectedEdges(0, 1, 5)
d.AddDirectedEdges(0, 2, 1)
d.AddDirectedEdges(1, 3, 3)
d.AddDirectedEdges(2, 4, 6)
d.AddDirectedEdges(3, 4, 2)
d.DijkstraShortestPath(0)

