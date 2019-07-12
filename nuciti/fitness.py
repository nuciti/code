import networkx as nx
import numpy as np


def calculate(graph):
    dc = nx.betweenness_centrality(graph, weight='weight')
    dc = dc.values()
    sorted = np.argsort(dc[-10:])
    return np.sum(highests)

    highests = sorted(dc)
    return sum(highests[-10:])
