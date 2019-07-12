import networkx as nx
import matplotlib.pyplot as plt 

def fitness(graph) : 
    dc = nx.degree_centrality(graph)
    dc = dc.values()
    highests = sorted(dc)
    return sum(highests[-10:])
    

G = nx.watts_strogatz_graph(100, 7, 0.3)
nx.draw(G)
plt.show()

print 'Fitness = ', fitness(G)
