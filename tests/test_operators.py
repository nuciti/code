from nuciti import data, operators


def test_random_individual():
    graph = data.generate()
    individual = operators.random_individual(graph)

    assert individual is not None
    assert individual.number_of_nodes() == graph.number_of_nodes()
    assert individual.number_of_edges() == graph.number_of_edges()


def test_crossover():
    graph = data.generate()

    parent_1 = operators.random_individual(graph)
    parent_2 = operators.random_individual(graph)

    assert parent_1.number_of_nodes() == parent_2.number_of_nodes()
    assert parent_1.number_of_edges() == parent_2.number_of_edges()

    child = operators.crossover(parent_1, parent_2)

    assert child is not None
    assert child.number_of_nodes() == parent_1.number_of_nodes()
    assert child.number_of_edges() == parent_1.number_of_edges()


def mutation():
    graph = data.generate()

    individual = operators.random_individual(graph)
    mutated = operators.mutation(individual, 0.5)

    assert mutated is not None
    assert mutated.number_of_nodes() == individual.number_of_nodes()
    assert mutated.number_of_edges() == individual.number_of_edges()
