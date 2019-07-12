import networkx as nx


def generate() -> nx.Graph:
    return nx.watts_strogatz_graph(100, 7, 0.3)
