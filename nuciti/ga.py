import random
from dataclasses import dataclass
from typing import List

import numpy as np
from tqdm import tqdm

import data
import fitness
import operators


@dataclass(init=True)
class Params():
    epochs: int
    pop_size: int
    p_crossover: float
    p_mutation_pop: float
    p_mutation_specimen: float

    def as_dict(self):
        return self.__dict__


@dataclass(init=True)
class EpochStats():
    scores: List[float]


def __init_pop(graph, pop_size: int):
    pop = []

    for i in range(pop_size):
        specimen = operators.random_individual(graph)
        pop.append(specimen)

    return pop


def __crossover(pop, p_crossover):
    new_pop = []

    for specimen in pop:
        if random.random() < p_crossover:

            mate = pop[random.randrange(len(pop))]
            child = operators.crossover(specimen, mate)

            new_pop.append(child)

        else:
            new_pop.append(specimen)

    return new_pop


def __mutation(pop, p_mutation_pop, p_mutation_specimen):
    new_pop = []

    for specimen in pop:
        if random.random() < p_mutation_pop:
            mutated = operators.mutation(specimen, p_mutation_specimen)
            new_pop.append(mutated)
        else:
            new_pop.append(specimen)

    return new_pop


def __evaluate_pop(pop):
    scores = []

    for specimen in pop:
        score = fitness.calculate(specimen)
        scores.append(score)

    return scores


def __selection(old_pop, old_scores, new_pop):
    new_scores = __evaluate_pop(new_pop)

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


def run(graph, params: Params) -> List[EpochStats]:
    stats = []

    # Initialise population
    graph = data.generate()
    pop = __init_pop(graph, params.pop_size)
    scores = __evaluate_pop(pop)
    stats.append(EpochStats(scores))

    for i in tqdm(range(params.epochs)):
        new_pop = __crossover(pop, params.p_crossover)
        new_pop = __mutation(new_pop, params.p_mutation_pop, params.p_mutation_specimen)
        new_pop, new_scores = __selection(pop, scores, new_pop)

        stats.append(EpochStats(scores))

        pop = new_pop
        scores = new_scores

    return stats
