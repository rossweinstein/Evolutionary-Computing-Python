from src.ecSystem.ECSystem import ECSystem
from src.ecSystem.ECSystemParameters import ECSystemParameters

# Where we actually run our EC System

params = ECSystemParameters()

# Governs the number of expressions in each generation
params.generation_size = 200

# Governs the length of the expressions in the initial population
params.genome_size = 15

# The percentage of the population selected for the next generation
params.fitness_threshold = 0.2

# If our fitness is not improving over this set number of generations, the EC System reboots
params.stagnation_threshold = 30

# The percentage of the population selected for mutation
params.mutation_percentage = .1

# Minimum fitness value required for the system to deem the expression equivalent to training data
params.success_threshold = 0.01

# Trainging Data: The x and y values used to evaluate the expression's fitness
params.x_training_data = [-55.0, -35.0, -11.0, -1.0, 1.0, 19.0, 87.0, 101.0]
params.y_training_data = [1512.0, 612.0, 60, 0.0, 0.0, 180.0, 3784, 5100.0]

ec_system = ECSystem(params)
ec_system.run_ec_system()

# System results
print(ec_system.stats)
