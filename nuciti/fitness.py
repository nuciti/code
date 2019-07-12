import networkx as nx
import numpy as np


def calculate(graph):
    dc = nx.betweenness_centrality(graph, weight='weight')
    dc = list(dc.values())
    sorted = np.sort(dc)
    highest_10 = sorted[-10:]
    return np.sum(highest_10)
