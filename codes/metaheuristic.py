import random

def GeneratesPopulation(Populations, Vertex, AvaibleColors):
    populate = []
    colors = list(range(AvaibleColors))

    for _ in range(Populations):
        chromosome = [[0] * Vertex for _ in range(2)]

        for i in range(Vertex):
            color1 = i % AvaibleColors
            color2 = (i + 1) % AvaibleColors

            chromosome[0][i] = color1
            chromosome[1][i] = color2

        # Shuffle the colors for diversity
        random.shuffle(colors)
        for i in range(Vertex):
            chromosome[0][i] = colors[chromosome[0][i]]
            chromosome[1][i] = colors[chromosome[1][i]]

        populate.append(chromosome)

    return populate

def CheckColoring(Color, Matrix):
    for i in range(len(Color[0])):
        for j in range(len(Color[0])):
            if Matrix[i][j] == 1 and (Color[0][i] == Color[0][j] or Color[1][i] == Color[1][j] or Color[0][i] == Color[1][j] or Color[1][i] == Color[0][j]):
                return False
    return True

def Fitness(Color, Matrix):
    conflicts = 0
    for i in range(len(Color[0])):
        for j in range(len(Color[0])):
            if Matrix[i][j] == 1 and (Color[0][i] == Color[0][j] or Color[1][i] == Color[1][j] or Color[0][i] == Color[1][j] or Color[1][i] == Color[0][j]):
                conflicts += 1
    return conflicts

def Crossover(P1, P2, Matrix):

    child = [[0] * len(P1[0]) for _ in range(2)]

    for i in range(len(P1[0])):
        if random.uniform(0, 1) < 0.5:
            child[0][i] = P2[0][i]
            child[1][i] = P2[1][i]
        else:
            child[0][i] = P1[0][i]
            child[1][i] = P1[1][i]

    return child


def Mutate(chromosome, mutation_rate, AvaibleColors):
    for i in range(len(chromosome[0])):
        if random.uniform(0, 1) < mutation_rate:
            chromosome[0][i] = random.randint(0, AvaibleColors-1)
            chromosome[1][i] = chromosome[0][i]+1
    return chromosome

def Genetic(Matrix, Vertex, AvaibleColors, Size, Generations, Mutation, save):
    # Population
    Population = GeneratesPopulation(Size, Vertex, AvaibleColors)

    for i in range(Generations):
        Population = sorted(Population, key=lambda x: Fitness(x, Matrix))

        # Saving 50% upper of population => parents
        parents = Population[:Size//2]

        # Create new population through crossover and mutation
        kids = []
        while len(kids) < (Size-len(parents)):
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child = Crossover(parent1, parent2, Matrix)
            child = Mutate(child, Mutation, AvaibleColors)

            # Ensure the child's coloring is valid
            while not CheckColoring(child, Matrix):
                child = Crossover(parent1, parent2, Matrix)
                child = Mutate(child, Mutation, AvaibleColors)

            kids.append(child)

        Population = parents+kids

    best_solution = min(Population, key=lambda x: Fitness(x, Matrix))
    ValidPairs = []

    for i in range(Vertex):
        ValidPairs.append( (best_solution[0][i], best_solution[1][i]) )

    cols = []

    for i in range(len(ValidPairs)):
        if ValidPairs[i][0] not in cols:
            cols.append(ValidPairs[i][0])
        if ValidPairs[i][1] not in cols:
            cols.append(ValidPairs[i][1])

    save["ChromaticNum"] = len(cols)
    save["Colors"] = ValidPairs
