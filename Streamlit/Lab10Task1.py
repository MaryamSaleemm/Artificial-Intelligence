import random

N = 8                   # Number of queens
POP_SIZE = 200          # Population size
MUTATION_RATE = 0.2     # Bit higher to improve diversity
MAX_GENERATIONS = 2000  # Maximum number of iterations


def fitness(state):
    non_attacking = 0
    for i in range(N):
        for j in range(i + 1, N):
            # If rows are same → attacking
            if state[i] == state[j]:
                continue
            # If diagonal conflicts → attacking
            if abs(state[i] - state[j]) == abs(i - j):
                continue
            # Otherwise safe pair
            non_attacking += 1
    return non_attacking


def create_individual():
    return [random.randint(1, N) for _ in range(N)]


def select_parent(population):
    total_fit = sum(fitness(ind) for ind in population)
    pick = random.uniform(0, total_fit)
    current = 0
    for ind in population:
        current += fitness(ind)
        if current >= pick:
            return ind
    return population[-1]

def crossover(p1, p2):
    point = random.randint(1, N - 1)
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p1[point:]
    return child1, child2

def mutate(ind):
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, N - 1)
        ind[idx] = random.randint(1, N)

def genetic_algorithm():
    population = [create_individual() for _ in range(POP_SIZE)]
    max_fitness = (N * (N - 1)) // 2  # 28 for 8 queens

    for generation in range(MAX_GENERATIONS):

        # Check if solution exists
        best = max(population, key=fitness)
        if fitness(best) == max_fitness:
            print(f"Solution found in generation {generation}:")
            print(best)
            return best

        new_population = []

        while len(new_population) < POP_SIZE:
            parent1 = select_parent(population)
            parent2 = select_parent(population)

            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)

            new_population.extend([child1, child2])

        population = new_population

    print("No solution found within generation limit.")
    return None

genetic_algorithm()
