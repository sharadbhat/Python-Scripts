"""
- Sharad Bhat
- 10th November, 2017
"""

from random import random, randint
from operator import add
from functools import reduce

def individual(length, minimun, maximum):
    """
    - Each individual is made of a list of numbers.
    """
    return [randint(minimun, maximum) for i in range(length)]

def population(count, length, minimun, maximum):
    """
    - Population made of number of individuals.
    """
    return [individual(length, minimun, maximum) for i in range(count)]

def fitness(individual, target):
    """
    - Determine how good a solution is.
    - Lower value better. 0 best.
    """
    sum = reduce(add, individual, 0)
    return abs(target - sum)

def grade(population, target):
    """
    - Get average fitness of entire population.
    """
    summed = reduce(add, (fitness(x, target) for x in population), 0)
    return (summed / float(len(population)))

def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.01):
    """
    - Get the best individuals to create new individuals.
    - Randomly select other individuals to include diversity.
    - Randomly mutate new individuals.
    """
    graded = [(fitness(x, target), x) for x in pop]
    graded = [x[1] for x in sorted(graded)]

    # Choose top 20% individuals from the population as possible parents
    retain_length = int(len(graded) * retain)
    parents = graded[:retain_length]

    # randomly add other individuals from rest 80% of the population to add diversity
    for individual in graded[retain_length:]:
        if random_select > random():
            parents.append(individual)

    # mutate some individuals
    for individual in parents:
        if mutate > random():
            position_to_mutate = randint(0, len(individual) - 1)
            individual[position_to_mutate] = randint(min(individual), max(individual))


    parents_length = len(parents) # 20% of population + random individuals from 80%
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            # Select halves from both parents to create children
            half = int(len(male) / 2)
            child = male[:half] + female[half:]
            children.append(child)

    # Add children to population
    parents.extend(children)
    return parents

if __name__ == '__main__':
    target = int(input("Enter target : "))
    population_count = int(input("Enter population count : "))
    individual_len = int(input("Enter individual length : "))
    individual_min = int(input("Enter minimum value : "))
    individual_max = int(input("Enter maximum value : "))

    p = population(population_count, individual_len, individual_min, individual_max)
    fitness_history = [grade(p, target),]

    for i in range(100):
        p = evolve(p, target)
        fitness_history.append(grade(p, target))

    print("The fitness values are as follows")
    for i in range(len(fitness_history)):
        print("Generation {} : {}".format(i, fitness_history[i]))
