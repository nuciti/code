import random 
import fitness
import generate_graph
import operators

def dummy_crossover(l):
    return l

def dummy_mutation(l):
    return l

pop_size = 20 # Keep even

# Initialise population
individuals = {}
for individual in [operators.random_individual(generate_graph.generate_graph()) for _ in xrange(pop_size)]:
    individuals[individual] = fitness.fitness(individual)

p_crossover = 0.1
p_mutation = 0.1

for i in xrange(1):
    new_individuals = {}
    for indivudual in individuals.keys():
        if random.random() < p_mutation:
            new_individual = dummy_mutation(individual)
            new_individual_fitness = fitness.fitness(new_individual)
            new_individuals[new_individual] = new_individual_fitness
    # Need to do crossover
    
    all_individuals = dict(individuals.items() + new_individuals.items())
    sorted_individuals = sorted(all_individuals.values())
    new_population = []
    for fitness in sorted_individuals[:(pop_size/2)]:
        for (k,v) in all_individuals.items():
            if v==fitness:
                new_population.append(k)
    print sorted_individuals
    print new_population

#     parents_and_offspring = individuals + new_individuals
#     print parents_and_offspring
#     sorted_fitnesses = 
