


# # Import libraries
# import random
# #from deap import base, creator, tools

# # Define items as (value, weight) tuples
# items = [(60, 10), (100, 20), (120, 30), (80, 15), (90, 25), (70, 12), (50, 8)]

# # Define knapsack capacity
# capacity = 50

# # Define fitness function
# def fitness(individual):
#     # Calculate total value and weight of selected items
#     total_value = 0
#     total_weight = 0
#     for i in range(len(individual)):
#         if individual[i] == 1:
#             total_value += items[i][0]
#             total_weight += items[i][1]
#     # Return fitness as a tuple of total value and negative total weight
#     return (total_value, -total_weight)

# # Define validity function
# def valid(individual):
#     # Calculate total weight of selected items
#     total_weight = 0
#     for i in range(len(individual)):
#         if individual[i] == 1:
#             total_weight += items[i][1]
#     # Return True if total weight is less than or equal to capacity, False otherwise
#     return total_weight <= capacity

# # Create types for individuals and fitness
# creator.create("Fitness", base.Fitness, weights=(1.0, -1.0)) # Maximize value and minimize weight
# creator.create("Individual", list, fitness=creator.Fitness)

# # Create toolbox
# toolbox = base.Toolbox()

# # Register attribute as a random bit (0 or 1)
# toolbox.register("attr", random.randint, 0, 1)

# # Register individual as a list of attributes
# toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr, n=len(items))

# # Register population as a list of individuals
# toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# # Register evaluation function
# toolbox.register("evaluate", fitness)

# # Register validity function
# toolbox.decorate("evaluate", tools.DeltaPenalty(valid, (-1000,-1000))) # Penalize invalid solutions

# # Register crossover operator as uniform crossover
# toolbox.register("mate", tools.cxUniform, indpb=0.5)

# # Register mutation operator as bit flip mutation
# toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)

# # Register selection operator as tournament selection
# toolbox.register("select", tools.selTournament, tournsize=3)

# # Set random seed for reproducibility
# random.seed(42)

# # Initialize population
# pop = toolbox.population(n=100)

# # Set number of generations
# ngen = 50

# # Run genetic algorithm
# for gen in range(ngen):
#     # Select offspring
#     offspring = toolbox.select(pop, len(pop))
#     # Clone offspring
#     offspring = list(map(toolbox.clone, offspring))
#     # Apply crossover and mutation to offspring
#     for child1, child2 in zip(offspring[::2], offspring[1::2]):
#         if random.random() < 0.7: # Crossover probability
#             toolbox.mate(child1, child2)
#             del child1.fitness.values
#             del child2.fitness.values
#     for mutant in offspring:
#         if random.random() < 0.2: # Mutation probability
#             toolbox.mutate(mutant)
#             del mutant.fitness.values
#     # Evaluate offspring
#     invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
#     fitnesses = map(toolbox.evaluate, invalid_ind)
#     for ind, fit in zip(invalid_ind, fitnesses):
#         ind.fitness.values = fit
#     # Replace population with offspring
#     pop[:] = offspring

# # Print best solution and its fitness
# best_ind = tools.selBest(pop, 1)[0]
# print("Best solution: ", best_ind)
# print("Best solution fitness: ", best_ind.fitness.values)


# Import libraries
import random
from deap import base, creator, tools

# Define items as (value, weight) tuples
items = [(60, 10), (100, 20), (120, 30), (80, 15), (90, 25), (70, 12), (50, 8)]

# Define knapsack capacity
capacity = 50

# Define fitness function
def fitness(individual):
    # Calculate total value and weight of selected items
    total_value = 0
    total_weight = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            total_value += items[i][0]
            total_weight += items[i][1]
    # Return fitness as a tuple of total value and negative total weight
    return (total_value, -total_weight)

# Define validity function
def valid(individual):
    # Calculate total weight of selected items
    total_weight = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            total_weight += items[i][1]
    # Return True if total weight is less than or equal to capacity, False otherwise
    return total_weight <= capacity

# Create types for individuals and fitness
creator.create("Fitness", base.Fitness, weights=(1.0, -1.0)) # Maximize value and minimize weight
creator.create("Individual", list, fitness=creator.Fitness)

# Create toolbox
toolbox = base.Toolbox()

# Register attribute as a random bit (0 or 1)
toolbox.register("attr", random.randint, 0, 1)

# Register individual as a list of attributes
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr, n=len(items))

# Register population as a list of individuals
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Register evaluation function
toolbox.register("evaluate", fitness)

# Register validity function
toolbox.decorate("evaluate", tools.DeltaPenalty(valid, (-1000,-1000))) # Penalize invalid solutions

# Register crossover operator as uniform crossover
toolbox.register("mate", tools.cxUniform, indpb=0.5)

# Register mutation operator as bit flip mutation
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)

# Register selection operator as tournament selection
toolbox.register("select", tools.selTournament, tournsize=3)

# Set random seed for reproducibility
random.seed(42)

# Initialize population
pop = toolbox.population(n=100)

# Set number of generations
ngen = 50

# Run genetic algorithm
for gen in range(ngen):
    # Select offspring
    offspring = toolbox.select(pop, len(pop))
    # Clone offspring
    offspring = list(map(toolbox.clone, offspring))
    # Apply crossover and mutation to offspring
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < 0.7: # Crossover probability
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values
    for mutant in offspring:
        if random.random() < 0.2: # Mutation probability
            toolbox.mutate(mutant)
            del mutant.fitness.values
    # Evaluate offspring
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit
    # Replace population with offspring
    pop[:] = offspring

# Print best solution and its fitness
best_ind = tools.selBest(pop, 1)[0]
print("Best solution: ", best_ind)
print("Best solution fitness: ", best_ind.fitness.values)
