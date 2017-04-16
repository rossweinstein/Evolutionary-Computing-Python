class IndividualStatistics:
    """
    This class keeps track of various data for the Individual class.
    Things we want to be aware of are how many times an Individual mutates,
    in what generation it mutated, who the Individuals parents were,
    whether it was used for any crossovers, and its birth generation.
    """

    def __init__(self, birth_gen=None, parents=None):

        self.mutation_count = 0
        self.mutation_generation = []
        self.cross_total = 0
        self.parents = None
        self.birth_generation = 0

        if birth_gen is not None and parents is not None:
            self.parents = parents
            self.birth_generation = birth_gen
        elif birth_gen is not None:
            self.birth_generation = birth_gen

    def __str__(self):
        return "Birth Generation: " + str(self.birth_generation) + "\n" + self._get_parents() \
               + "\nMutation Count: " + str(self.mutation_count) + "\nMutation Generation: " \
               + str(self.mutation_generation) + "\nTimes Crossed: " + str(self.cross_total)

    def _get_parents(self):
        """
        Determines if the expression has parents or if it is a first generation expression
        and returns the appropriate information
        :return: String the parents if they have no; 1st generation if no parents
        """

        the_parents = "Parents: "

        if self.parents is not None:
            return the_parents + self.parents[0].get_random_expression() \
                   + ", " + self.parents[1].get_random_expression()
        else:
            return the_parents + "No Parents, 1st Generation"

    def expression_mutated(self, gen_mutate):
        """
        This updates both mutation count and mutation generation. It increments mutation count
        while adding the current generation to the mutation generation list.
        :param gen_mutate: The generation the Individual mutated in
        :return:
        """
        self.mutation_count += 1
        self.mutation_generation.append(gen_mutate)

    def expression_crossed(self):
        """
        Increments our count for the number of times the expression was crossed.
        :return:
        """
        self.cross_total += 1
