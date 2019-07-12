import networkx as nx


def generate() -> nx.Graph:
    return nx.watts_strogatz_graph(20, 7, 0.3)
