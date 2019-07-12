from nuciti import data, fitness


def test_fitness():
    graph = data.generate()
    score = fitness.calculate(graph)

    assert score is not None
    assert score >= 0
