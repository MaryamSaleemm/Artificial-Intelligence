import random



def fitness(board):
    n = len(board)
    non_attacking = 0
    total_pairs = n * (n - 1) // 2

    attacking = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacking += 1

    non_attacking = total_pairs - attacking
    return non_attacking


def selection(population):
    total_fit = sum(fitness(ch) for ch in population)
    pick = random.uniform(0, total_fit)
    current = 0
    for ch in population:
        current += fitness(ch)
        if current >= pick:
            return ch


def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 2)
    child = parent1[:point] + parent2[point:]
    # repair duplicates
    child = repair(child)
    return child


def repair(chrom):
    n = len(chrom)
    seen = set()
    for i in range(n):
        if chrom[i] in seen:
            for j in range(1, n + 1):
                if j not in chrom:
                    chrom[i] = j
                    break
        else:
            seen.add(chrom[i])
    return chrom


def mutate(chrom, rate=0.1):
    if random.random() < rate:
        i, j = random.sample(range(len(chrom)), 2)
        chrom[i], chrom[j] = chrom[j], chrom[i]
    return chrom


def genetic_algorithm(n=8, pop_size=100, generations=1000):
    population = [random.sample(range(1, n + 1), n) for _ in range(pop_size)]
    max_fitness = n * (n - 1) // 2

    for gen in range(generations):
        population = sorted(population, key=fitness, reverse=True)

        if fitness(population[0]) == max_fitness:
            print(f"\n✅ Solution found in generation {gen}: {population[0]}")
            return population[0]

        new_population = population[:10]  # Elitism: keep best 10
        while len(new_population) < pop_size:
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    print("\n No perfect solution found.")
    return population[0]

print("Solving 4-Queens Problem:")
solution_4 = genetic_algorithm(n=4, pop_size=50, generations=500)


print("\nSolving 8-Queens Problem:")
solution_8 = genetic_algorithm(n=8, pop_size=100, generations=1000)
