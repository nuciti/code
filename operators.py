import numpy as np
import networkx as nx
import copy

np.random.seed(42)


'''
Takes as input a graph structure and returns a copy of the graph with random weights.
'''
def random_individual(graph):
    random_graph = copy.deepcopy(graph)
    for (u,v) in random_graph.edges:
        random_graph[u][v]['weight'] = np.random.random()
    return random_graph

# new function please test 

def graph_weights(graph):
    return [graph.edges[x]['weight'] for x in graph.edges] 


'''
Does the crossover operation. Takes as input two graphs with weights and produces a new graph with weights. Each weight
is randomly and independently picked from either of the two original graphs.
'''
def crossover(graph1, graph2):
    new_graph = copy.deepcopy(graph1)
    for (u, v) in new_graph.edges:
        if np.random.choice([True, False]):
            new_graph[u][v]['weight'] = graph2[u][v]['weight']
    return new_graph
