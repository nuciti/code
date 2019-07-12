from nuciti.generate_graph import generate_graph


def test_generate_graph():
    graph = generate_graph()

    assert graph is not None
    assert graph.number_of_nodes() > 0
    assert graph.number_of_edges() > 0
