import random

import numpy as np

import data
import fitness
import operators

# must be even
POP_SIZE = 20
EPOCHS = 100

P_CROSSOVER = 0.4
P_MUTATION_POP = 0.5
P_MUTATION_SPECIMEN = 0.1


def init_pop(pop_size: int):
    graph = data.generate()
    pop = []

    for i in range(pop_size):
        specimen = operators.random_individual(graph)
        pop.append(specimen)

    return pop


def crossover(pop):
    new_pop = []

    for specimen in pop:
        if random.random() < P_CROSSOVER:

            mate = pop[random.randrange(len(pop))]
            child = operators.crossover(specimen, mate)

            new_pop.append(child)

        else:
            new_pop.append(specimen)

    return new_pop


def mutation(pop):
    new_pop = []

    for specimen in pop:
        if random.random() < P_MUTATION_POP:
            mutated = operators.mutation(specimen, P_MUTATION_SPECIMEN)
            new_pop.append(mutated)
        else:
            new_pop.append(specimen)

    return new_pop


def evaluate_pop(pop):
    scores = []

    for specimen in pop:
        score = fitness.calculate(specimen)
        scores.append(score)

    return scores


def selection(old_pop, old_scores, new_pop):
    new_scores = evaluate_pop(new_pop)

    pop = old_pop + new_pop
    scores = old_scores + new_scores

    selected = []
    selected_scores = []

    for index in np.argsort(scores):
        selected.append(pop[index])
        selected_scores.append(scores[index])

    pop_size = len(old_pop)

    selected = selected[-pop_size:]
    selected_scores = selected_scores[-pop_size:]

    return selected, selected_scores


def main():
    stats = []

    # Initialise population
    pop = init_pop(POP_SIZE)
    scores = evaluate_pop(pop)
    stats.append(scores)

    for i in range(EPOCHS):
        new_pop = crossover(pop)
        new_pop = mutation(new_pop)
        new_pop, new_scores = selection(pop, scores, new_pop)

        stats.append(new_scores)

        pop = new_pop
        scores = new_scores


if __name__ == "__main__":
    main()
