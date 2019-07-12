import networkx as nx

def generate_graph():
    # Written by Nono, I just moved it here (George)
    return nx.watts_strogatz_graph(100, 7, 0.3)
