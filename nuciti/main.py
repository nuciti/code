import random 
import fitness
import generate_graph
import operators



def selection(individuals, new_individuals):
    # Returns the fittest half of the population
    all_individuals = individuals.copy()	
    all_individuals.update(new_individuals)	
    #all_individuals = dict(individuals.items() + new_individuals.items())
    sorted_individuals = sorted(all_individuals.values())
    new_population = {}
    for fitness in sorted_individuals[-(int(pop_size/2)):]:
        for (k,v) in all_individuals.items():
            if v==fitness:
                new_population[k] = v
    return new_population

pop_size = 20 # Keep even

# Initialise population
individuals = {}
for individual in [operators.random_individual(generate_graph.generate_graph()) for _ in range(pop_size)]:
    individuals[individual] = fitness.fitness(individual)

p_crossover = 0.1
p_mutation = 0.1

for i in range(1):
    new_individuals = {}

    # here we do crossover of pairs of individuals from the old population with possible crossover
    for individual1 in individuals.keys():
        for individual2 in individuals.keys():
            if individual1 is not individual2 and random.random() < p_crossover:
                new_individual = operators.crossover(individual1, individual2)
                if random.random() < p_mutation: new_individual = operators.mutation(new_individual, p_mutation)
                new_individuals[new_individual] = fitness.fitness(new_individual)

    # here we do mutation of the individuals in the population without changing them
    for individual in individuals.keys():
        if random.random() < p_mutation:
            new_individual = operators.mutation(individual,p_mutation)
            new_individuals[new_individual] = fitness.fitness(new_individual)
    # Need to do crossover
    
    individuals = selection(individuals, new_individuals)

#     parents_and_offspring = individuals + new_individuals
#     print parents_and_offspring
#     sorted_fitnesses = 
