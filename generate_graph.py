import networkx as nx

def generate_graph(num_nodes, max_):
    # Written by Nono, I just moved it here (George)
    return nx.watts_strogatz_graph(100, 7, 0.3)
