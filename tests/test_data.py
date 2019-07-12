from nuciti import data


def test_generate_graph():
    graph = data.generate()

    assert graph is not None
    assert graph.number_of_nodes() > 0
    assert graph.number_of_edges() > 0
