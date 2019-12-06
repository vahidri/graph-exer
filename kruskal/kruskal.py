import networkx as nx
import matplotlib.pyplot as plt
import collections

G=nx.Graph()

edge = collections.defaultdict(list)
edge_labels = {}
n = int(input())
m = int(input())
par = [0]*(n+1)
ans = 0

def calc_par(v):
	if v == par[v]:
		return v
	par[v] = calc_par(par[v])
	return par[v]

for i in range(1,n+1):
	par[i] = i

for i in range(1,n+1):
	G.add_node(i)

for i in range(m):
	x, y,w = [int(j) for j in input().split()]
	edge[w].append((x,y))
	edge_labels.update({(x,y):w})

#print(sorted(edge.items()))
edge = sorted(edge.items())

for i, j in edge:
	for u,v in j:
		if calc_par(v)!=calc_par(u):
			G.add_edge(u,v,color='b')
			par[calc_par(v)] = calc_par(u)
			ans += i
		else:
			G.add_edge(u,v,color='r')

print(ans)

pos =nx.spring_layout(G)
colors = [G[u][v]['color'] for u,v in G.edges()]
nx.draw(G,pos,edge_color=colors,with_labels=True)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
plt.savefig("kruskal.png")
plt.show()
