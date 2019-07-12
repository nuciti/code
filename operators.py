import numpy as np
import networkx as nx
import copy

np.random.seed(42)


'''
Takes as input a graph structure and returns a copy of the graph with random weights.
'''
def random_individual(graph: nx.Graph) -> nx.Graph:
    random_graph = copy.deepcopy(graph)
    for (u,v) in random_graph.edges:
        random_graph[u][v]['weight'] = np.random.random()
    return random_graph

# new function please test 

def graph_weights(graph):
    return [graph.edges[x]['weight'] for x in graph.edges] 
