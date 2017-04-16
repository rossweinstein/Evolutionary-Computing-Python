
class ECSystemParameters:
    """
    This class governs all the parameters needed to run our EC System.
    Initially set to invalid values to prevent system for running.

    Generation size => How many Individuals do we want in each generation?
    Genome size => We can cap the length for how long we want our initial
                   population's expressions to be
    X-Training Data => The x value we will plug into our random expressions
    Y-Training Data => The y values we will match our output to to determine fitness
    Fitness Threshold => What percentage of the population will be selected to
                         go on to the next generation
    Stagnation Threshold => If our fitness is not improving overall over this set
                            number of generations, we reboot the system and start over
    Mutation Percentage => Of the Individuals selected for the next generation, what
                           percentage will we mutate instead of crossover
    Success Threshold => Determines when we have found an equivalent expression. Their
                          fitness is at or below this value.
    """

    def __init__(self):
        self.generation_size = 0
        self.genome_size = 0
        self.x_training_data = []
        self.y_training_data = []
        self.fitness_threshold = -1.0
        self.stagnation_threshold = -1
        self.mutation_percentage = -1.0
        self.success_threshold = -1.0

    def all_parameters_set(self):
        """
        Make sure that all values are appropriately set
        :return: Boolean true if system is ready, false otherwise
        """
        return self.generation_size > 49 and self.genome_size > 4 and self._valid_training_data() \
               and self.fitness_threshold > 0.0 and self.stagnation_threshold > 0 \
               and self.mutation_percentage >= 0.0 and self.success_threshold >= 0.0

    def _valid_training_data(self):
        """
        Make sure our training data exists and that we have a x for every y
        :return: Boolean true if valid data, false othewise
        """
        return len(self.x_training_data) > 0 and len(self.x_training_data) == len(self.y_training_data)
