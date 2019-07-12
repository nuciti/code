import networkx as nx
import matplotlib.pyplot as plt 

def fitness(graph) : 
    dc = nx.betweenness_centrality(graph, weight='weight')
    dc = dc.values()
    highests = sorted(dc)
    return sum(highests[-10:])
    

# nx.draw(G)
# plt.show()

#print 'Fitness = ', fitness(G)
