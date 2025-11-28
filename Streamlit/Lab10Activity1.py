import random

L = 8                 # length of bitstring
POP_SIZE = 20         # population size
CROSSOVER_RATE = 0.8  
MUTATION_RATE = 0.01  
MAX_GENERATIONS = 200

def create_individual():
    """Creates a random individual (bitstring)."""
    return [random.randint(0, 1) for _ in range(L)]

def fitness(individual):
    """Fitness is number of 1s in the bitstring."""
    return sum(individual)

def select_parent(population):
    """Roulette wheel selection."""
    total_fitness = sum(fitness(ind) for ind in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for ind in population:
        current += fitness(ind)
        if current >= pick:
            return ind
    return population[-1]

def crossover(parent1, parent2):
    """Single-point crossover."""
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, L - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    else:
        return parent1[:], parent2[:]

def mutate(individual):
    """Bit-flip mutation."""
    for i in range(L):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]

def genetic_algorithm():
    population = [create_individual() for _ in range(POP_SIZE)]

    for generation in range(MAX_GENERATIONS):
        # Check if solution found
        best_ind = max(population, key=fitness)
        if fitness(best_ind) == L:
            print(f"Solution found in generation {generation}!")
            print("Solution:", best_ind)
            return best_ind

        new_population = []

        # Create next generation
        while len(new_population) < POP_SIZE:
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = new_population[:POP_SIZE]

    print("Solution not found within max generations.")
    return None

genetic_algorithm()
