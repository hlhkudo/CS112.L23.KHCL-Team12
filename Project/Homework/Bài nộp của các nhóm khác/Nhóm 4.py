# -*- coding: utf-8 -*-
"""DynamicProgramming: Homeworks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ORc8X7vaVVDSV4NlK0SSzItZCsFbor46
"""

class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
  
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 

    def printArr(self, dist): 
        print("Vertex Distance from Source") 
        for i in range(self.V): 
            print("{0}\t\t{1}".format(i, dist[i])) 
      
    def dynamic_programming(self, src): 
        dist = [float("Inf")] * self.V 
        dist[src] = 0
  
        for _ in range(self.V - 1): 
            for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w 
        for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        print("Graph contains negative weight cycle")
                        return
                
        self.printArr(dist) 
## S = 0, A = 1, B = 2, C = 3, D = 4, E = 5, F = 6, T = 7
# S -> A = 1
# S -> B = 2
# S -> C = 5
# A -> D = 4
# A -> E = 11
# B -> D = 9
# B -> E = 5
# B -> F = 16
# C -> F = 2
# D -> T = 18
# E -> T = 13
# F -> T = 2
graph = Graph(8) 
graph.addEdge(0, 1, 1) 
graph.addEdge(0, 2, 2) 
graph.addEdge(0, 3, 5) 
graph.addEdge(1, 4, 4)
graph.addEdge(1, 5, 11) 
graph.addEdge(2, 4, 9) 
graph.addEdge(2, 5, 5)
graph.addEdge(2, 6, 16)
graph.addEdge(3, 6, 2)
graph.addEdge(4, 7, 18)
graph.addEdge(5, 7, 13)
graph.addEdge(6, 7, 2)
  
graph.dynamic_programming(0)