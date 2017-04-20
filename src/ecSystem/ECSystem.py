from src.ecSystem.CalculateDelta import CalculateDelta
from src.ecSystem.ECSystemStatistics import ECSystemStatistics
import random

from src.genome.Individual import Individual
from src.randomExpression.RandomStringExpression import RandomStringExpression


class ECSystem:
    """
    This class, when given a set of parameters (which include x and y coordinates),
    can find an expression which will evaluate to those values.
    """

    def __init__(self, ec_parameters):
        self.parameters = ec_parameters
        self.stats = ECSystemStatistics()
        self.generation = []
        self.stagnation_count = 0
        self.calc = CalculateDelta()

    def reset_ec_system(self):
        self.stats = ECSystemStatistics()
        self.generation = []
        self.stagnation_count = 0

    def run_ec_system(self):
        """
        Finds an equivalent expression for the provided parameters.
        :return: Boolean Returns true when expression is found, false if any parameter not set
        """

        # makes sure we start with a clean system
        self.reset_ec_system()

        if not self.parameters.all_parameters_set():
            print("You have not set all system parameters to run this EC System")
            return False

        # start counting
        self.stats.start_stop_watch()
        print("EC System Running...")

        # create our first generation Individuals
        self.generation = self._create_initial_population(1)

        equivalent_expression_found = False
        while not equivalent_expression_found:

            self._evaluate_each_expression()

            # sort all expression fitness from lowest values to highest
            self.generation.sort(key=lambda genome: genome.fitness)

            # if an Individual has a divide by 0 error for any value,
            # its fitness is set to -1
            # this gets rid of all Individuals with a fitness of -1
            self._discard_unfit_individuals()

            # record all our current fitness levels
            if len(self.generation) > 0:
                self.stats.add_most_fit_in_generation(self.generation[0])
                print(self.generation[0].fitness)

            # determines if we found an equivalent expression
            if len(self.generation) > 0 and 0 <= self.generation[0].fitness <= self.parameters.success_threshold:

                equivalent_expression_found = True
                self.stats.set_successful_genome(self.generation[0])
            else:
                # if we have not, start mutation and crossover to get next generation
                self._create_new_generation()

            # record number of generations without rebooting system
            self.stagnation_count += 1

        # we have found an equivalent expression, stop counting the seconds
        self.stats.end_stop_watch()
        return True

    def _create_new_generation(self):
        """
        Creates a new generation from the most fit Individuals who were both mutated
        and crossed
        :return:
        """

        # make sure we only dealing with the most fit Individuals
        most_fit_individuals = self._perform_selection()

        self.stats.add_generation()

        # makes sure we have Individuals to work with, there are occasions when all
        # expressions have divide by zero errors where we just need to reboot the system
        if len(most_fit_individuals) > 1 and self._fitness_improving(most_fit_individuals[0]):

            # remove and mutate selected Individuals from the List
            mutated_individuals = self._mutation_selection(most_fit_individuals)

            # each generation is kept at the same size, this determines how many children
            # are need to make this next generation equal the generation size parameter
            num_of_children_needed = self.parameters.generation_size \
                                     - len(most_fit_individuals) - len(mutated_individuals)

            # cross the non mutated Individuals as many times as needed
            children = self._crossover_selection(most_fit_individuals,
                                                 num_of_children_needed,
                                                 self.stats.number_of_gen)

            # combine all three lists to create new generation
            self.generation = mutated_individuals + most_fit_individuals + children
        else:

            # reboot system but continue to keep track of generation count
            self.generation = self._create_initial_population(self.stats.number_of_gen)
            self.stagnation_count = 0
            self.stats.add_system_rebooted()

    def _create_initial_population(self, gen_num):
        """
        Creates our first population of Individuals based on the provided parameters.
        :param gen_num: int The current generation
        :return: List of Individuals totalling the number specified in parameters
        """

        population = []

        for _ in range(self.parameters.generation_size):
            population.append(Individual(RandomStringExpression(self.parameters.genome_size), gen_num))
            self.stats.add_operation()

        self.stats.add_generation()
        self.stagnation_count += 1

        return population

    def _evaluate_each_expression(self):
        """
        Loop through each Individual and determine their fitness
        :return:
        """

        for i in range(len(self.generation)):

            self.calc.calculate_delta(self.generation[i].get_program_genome(),
                                      self.parameters.x_training_data,
                                      self.parameters.y_training_data)

            self.generation[i].fitness = self.calc.delta
            self.generation[i].y_values = self.calc.y_values

            self.stats.add_operation()

    def _discard_unfit_individuals(self):
        """
        Individuals whose fitness is -1 are removed from the population. A fitnes
        of -1 means that their expression had a divide by zero error
        :return:
        """

        while self.generation[0].fitness == -1.0:
            self.generation.remove(self.generation[0])
            self.stats.add_operation()

    def _perform_selection(self):
        """
        This returns the most fit Individuals in the generation based on the
        fitness threshold set in the parameters
        :return: List containing the most fit Individuals in that generation
        """

        selected_individuals = []

        for i in range(int(len(self.generation) * self.parameters.fitness_threshold)):

            selected_individuals.append(self.generation[i])
            self.stats.add_operation()

        return selected_individuals

    def _fitness_improving(self, most_fit):
        """
        If our stagnation count has reached our threshold, determine if our fitness is
        improving.
        :param most_fit: Individual the most fit Individual in the population
        :return: Boolean True if fitness is improving, False if it is not
        """

        self.stats.add_operation()

        if self.stagnation_count <= self.parameters.stagnation_threshold:
            return True
        else:
            return most_fit.fitness - self._past_gen_average() < -1.0

    def _past_gen_average(self):
        """
        Finds the average fitness of the past generation
        :return: float the average fitness of the past generation
        """

        total = 0.0
        position = len(self.stats.most_fit_values) - self.parameters.stagnation_threshold - 1

        for i in range(self.parameters.stagnation_threshold):

            total += self.stats.most_fit_values[position]
            position += 1
            self.stats.add_operation()

        return total / self.parameters.stagnation_threshold

    def _mutation_selection(self, population):
        """
        Randomly selects and mutates Individuals in the population
        :param population: List of Individuals making up our population
        :return: List of newly mutated Individuals
        """

        mutated_population = []

        for i in range(int(len(population) * self.parameters.mutation_percentage)):

            selection = random.randrange(len(population))

            population[selection].mutate(self.stats.number_of_gen)

            mutated_population.append(population[selection])

            population.remove(population[selection])

            self.stats.add_operation()

        return mutated_population

    def _crossover_selection(self, population, num_children_needed, gen_num):
        """
        Selects two Individuals randomly from the generation and crosses them.
        :param population: List of Individuals making up our population
        :param num_children_needed: int Each population size is set,
                                    this determines how many crossovers are needed
        :param gen_num: int Records what generation we are in
        :return: List of newly created Individuals
        """

        children = []

        for i in range(num_children_needed):

            parent_one = random.randrange(len(population))
            parent_two = random.randrange(len(population))

            children.append(population[parent_one].crossover(population[parent_two], gen_num))

            self.stats.add_operation()

        return children
