import networkx as nx


def generate() -> nx.Graph:
    # Written by Nono, I just moved it here (George)
    return nx.watts_strogatz_graph(100, 7, 0.3)
