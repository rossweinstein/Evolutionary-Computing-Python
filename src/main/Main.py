from src.ecSystem.ECSystem import ECSystem
from src.ecSystem.ECSystemParameters import ECSystemParameters

# Where we actually run our EC System

# First we get out x and y training data
# The equation used here is (x^2 - 1) / 2
x_data = [-55.0, -35.0, -11.0, -1.0, 1.0, 19.0, 87.0, 101.0]
y_data = [1512.0, 612.0, 60, 0.0, 0.0, 180.0, 3784, 5100.0]

# Then we set up our parameters for the system
params = ECSystemParameters()
params.generation_size = 200
params.genome_size = 15
params.fitness_threshold = 0.2
params.stagnation_threshold = 30
params.mutation_percentage = .1
params.success_threshold = 0.01
params.x_training_data = x_data
params.y_training_data = y_data

# Then we run our system and print out the results
ec_system = ECSystem(params)
ec_system.run_ec_system()
print(ec_system.stats)
