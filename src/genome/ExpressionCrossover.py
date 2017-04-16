from random import getrandbits

from src.genome.RandomPointsFinder import RandomPointsFinder
from src.randomExpression.RandomStringExpression import RandomStringExpression


class ExpressionCrossover:
    """
    This class takes two Individuals and is able to create a new Individual by
    selecting random parts of the parent expressions.
    """

    def __init__(self):
        self.mom = None
        self.dad = None
        self._find_valid_points = RandomPointsFinder()

    def set_parents(self, mom, dad):
        """
        Setter for the class.
        :param mom: RandomStringExpression One of the expressions to cross
        :param dad: RandomStringExpression The other expression to cross
        :return:
        """
        self.mom = mom
        self.dad = dad

    def perform_crossover(self):
        """
        Crosses the two Individuals to create a new one. If both Individuals
        have not been provided, does nothing.
        :return: Dictionary containing the information need to create a new Individual
        """

        if self.mom is not None and self.dad is not None:
            return self._crossover()

    def _crossover(self):
        """
        Creates a new child RandomStringExpression and returns a dictionary with its
        information as well as its parents
        :return: Dictionary containing the information need to create a new Individual
        """

        child = self._cross_genomes()

        crossed_child = RandomStringExpression(child_expression=child)

        return {"child genomeTest": crossed_child, "parents": [self.mom, self.dad]}

    def _cross_genomes(self):
        """
        Where the cross actually happens. Randomly selects portions of the parents
        genome and combines them into a new expression
        :return: List containing the child's left branch, root operator, and right branch
        """

        child = []

        moms_left_side = bool(getrandbits(1))
        dads_left_side = bool(getrandbits(1))

        gene_sequence = self._swamp_genome([moms_left_side, dads_left_side])

        if moms_left_side and dads_left_side:
            child.append(gene_sequence[0])
            child.append(self.mom.root_operator)
            child.append(self.dad.right_branch)
        elif moms_left_side and not dads_left_side:
            child.append(gene_sequence[0])
            child.append(self.mom.root_operator)
            child.append(gene_sequence[1])
        elif not moms_left_side and dads_left_side:
            child.append(gene_sequence[1])
            child.append(self.dad.root_operator)
            child.append(self.mom.left_branch)
        else:
            child.append(gene_sequence[1])
            child.append(self.dad.root_operator)
            child.append(gene_sequence[0])

        return child

    def _swamp_genome(self, sides):
        """
        This method has each parent
        :param sides: List of booleans will determine which branch side we will cross with
        :return: Dictionary containing random parts of the parents expressions
        """

        mom_genome = self._genome_cross(sides[0], self.mom)
        dad_genome = self._genome_cross(sides[1], self.dad)

        return self._alter_genome(mom_genome, dad_genome)

    def _genome_cross(self, side, the_genome):
        """
        This method captures a random section of the parents expression and puts
        that information in a dictionary.
        genome branch => either the left or right branch of the expression
        selected points => the randomly selected indexes within that string
        sequence => the substring returned from the selected points

        :param side: boolean Will determine which branch we use
        :param the_genome: RandomStringExpression the expression we are going to cross
        :return: Dictionary containing a random selection from the parent expression
        """
        branch = self._get_sides(side, the_genome)

        self._find_valid_points.set_expression(branch)
        selection = self._find_valid_points.get_points()
        the_selection = branch[selection[0]: selection[1] + 1]

        return {"genome branch": branch, "selected points": selection, "gene sequence": the_selection}

    def _alter_genome(self, mom_sequence, dad_sequence):
        """
        Takes the randomly selected information needed to cross both parents
        :param mom_sequence: Dictionary containing randomly selected information from the mother
        :param dad_sequence: Dictionary containing randomly selected information from the father
        :return: List containing strings of randomly combined parts from each parent
        """
        mom_alter = self._compile_gene_sequence(mom_sequence["genome branch"],
                                                  mom_sequence["selected points"],
                                                  dad_sequence["gene sequence"])

        dad_alter = self._compile_gene_sequence(dad_sequence["genome branch"],
                                                   dad_sequence["selected points"],
                                                   mom_sequence["gene sequence"])
        return [mom_alter, dad_alter]

    def _compile_gene_sequence(self, genome_branch, selection_points, other_parent_sequence):
        """
        Takes the information from one parent and injects a small part of the expression from another
        :param genome_branch: String either the left or right branch of the expression
        :param selection_points: List selecting a random area within genome branch
        :param other_parent_sequence: String A random selection from the other parent
        :return: String an expression with information from both parents
        """
        return genome_branch[:selection_points[0]] + other_parent_sequence + genome_branch[selection_points[1] + 1: len(genome_branch)]

    def _get_sides(self, left, parent):
        """
        If we are dealing with the branches of the expression. This will return one side
        based on a boolean
        :param left: boolean Do we want the left side?
        :param parent: RandomStringExpression The parent
        :return: String either the parents left or right branch
        """
        return parent.left_branch if left else parent.right_branch
