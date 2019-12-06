import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
from pprint import pprint as ppt

from hck import HopcroftKarp as hopcroft

def lbl(inp): ##LaBeL
    return chr(96+inp)

m, n, e = map(int, input('enter m n e:').split() )
G=nx.Graph()
ncolors = []
graph = {}
print('enter edges (format: x y)')
for i in range(e):
    x, y = map(int, input().split() )
    G.add_edge(x, lbl(y), color='k')
    if x in graph:
        graph[x].add(lbl(y) )
    else:
        graph[x] = set([lbl(y) ])

##check if it's bipartate
try:
    ##test
    c = bipartite.color(G)
    for i in range(0,m):
        G.add_node(i+1)
        ncolors += 'r'
    for j in range(1,n+1):
        G.add_node(lbl(j) )
        ncolors += 'g'
except NetworkXError:
    print('the given graph is not bipartite')
    quit()

print('graph:')
ppt(graph)
output = hopcroft(graph).maximum_matching()
m2n = { x: output[x] for x in range(1, m+1) }
print()
print('matchings (', len(m2n), ') :', sep='')
ppt(m2n)
for u in m2n:
    G[u][m2n[u]]['color']='b'

pos = nx.spring_layout(G)
ecolors = [G[u][v]['color'] for u, v in G.edges()]
nx.draw(G, pos, node_color=ncolors, edge_color=ecolors, with_labels=True)
plt.savefig("hopcroft.png")
plt.show()

