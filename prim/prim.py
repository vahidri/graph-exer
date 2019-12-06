import sys
from platform import node
import networkx as nx
import matplotlib.pyplot as plot
import collections

class graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")

        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
            G.add_edge(parent[i], i, color='b')

    def minKey(self, key, mstSet):
        min = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        key[0] = 0  # start vertix
        parent = [None] * self.V
        mstSet = [False] * self.V

        parent[0] = -1  # root of a tree has no parent

        for i in range(self.V):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for v in range(self.V):

                if key[v] > self.graph[u][v] > 0 and mstSet[v] == False:
                    key[v] = self.graph[u][v]
                    parent[v] = u


        self.printMST(parent)


print("Enter number of vertices and edges : ")
# number of vertices
vertices = int(input())
# number of edges
edges = int(input())

g = graph(vertices)

G = nx.Graph()
edge = collections.defaultdict(list)
edge_labels = {}

for i in range(vertices):
    G.add_node(i)

for i in range(vertices):
    g.graph[0].append(0)
print("Enter edges and their weights : ")
for i in range(edges):
    u, v, w = [int(x) for x in input().split()]
    g.graph[u][v] = w
    g.graph[v][u] = w
    edge[w].append((u, v))
    edge_labels.update({(u, v): w})
    G.add_edge(u, v, color='r')

edge = sorted(edge.items())



g.primMST()


position = nx.spring_layout(G)
colors = [G[u][v]['color'] for u, v in G.edges()]
nx.draw(G, position, edge_color=colors, with_labels=True)
nx.draw_networkx_edge_labels(G, position, edge_labels=edge_labels)
plot.savefig("prim.png")
plot.show()
