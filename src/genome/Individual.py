from src.genome.ExpressionCrossover import ExpressionCrossover
from src.genome.ExpressionMutator import ExpressionMutator
from src.genome.IndividualStatistics import IndividualStatistics


class Individual:
    """
    This class has all the information needed for our expressions in the EC System.
    It contains an expression, a fitness value, and it's output (or Y-values)

    """
    def __init__(self, genome, birth_gen=None, parents=None):

        self.genome = genome
        self.fitness = -1.0
        self.y_values = []
        self._mutator = ExpressionMutator()
        self._cross_expressions = ExpressionCrossover()

        if parents is None and birth_gen is None:
            self.stats = IndividualStatistics()
        elif birth_gen is not None and parents is None:
            self.stats = IndividualStatistics(birth_gen)
        else:
            self.stats = IndividualStatistics(birth_gen, parents)

    def __str__(self):
        return "Genome: " + self.get_program_genome() + "\nFitness: " \
               + str(self.fitness) + "\nY Values: " + str(self.y_values) + "\n" + str(self.stats)

    def get_program_genome(self):
        """
        The current for of the expression (can mutate)
        :return: String the expression in the appropriate format
        """
        return self.genome.get_random_expression()

    def mutate(self, gen_number):
        """
        Alters the expression in a random way.
        :param gen_number: int Records the generation the Individual mutated in
        :return:
        """

        self._mutator.mutate_expression(self.genome)
        self.stats.expression_mutated(gen_number)

    def crossover(self, other_genome, gen_number):
        """
        With another Individual, this will create a new Individual with a random
        combination of the parents expressions
        :param other_genome: Individual The Individual to crossover with
        :param gen_number: int Records the generation the Individual crossover in
        :return: Individual A newly created Individual from the two parent Individuals
        """

        self.stats.expression_crossed()

        self._cross_expressions.set_parents(self.genome, other_genome.genome)
        child = self._cross_expressions.perform_crossover()

        return Individual(child["child genomeTest"], gen_number, child["parents"])
