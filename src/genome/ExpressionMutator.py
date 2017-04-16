from random import randint

from src.genome.RandomPointsFinder import RandomPointsFinder
from src.randomExpression.ExpressionBranch import ExpressionBranch


class ExpressionMutator:
    """
    This class is able to take a string expression and alter it
    in a random way.
    """

    def __init__(self):
        self._mutated_expression = None
        self._original_expression = None
        self._find_valid_points = RandomPointsFinder(self._mutated_expression)

    def __str__(self):
        return "Original Expression: " + self._original_expression \
               + "\nMutated Expression: " + self._mutated_expression

    def mutate_expression(self, expression):
        """
        Alters the provided string expression into a slightly different one.
        :param expression: String Any string expression
        :return: String The altered string expression
        """
        self._mutated_expression = expression
        self._original_expression = expression
        self._mutate()
        return self._mutated_expression

    def _mutate(self):
        """
        Selects if we are going to mutate the left branch, the root operator,
        or the right branch of the expression
        :return:
        """

        num_selection = randint(0, 10)

        if num_selection < 3:
            self._root_operator_mutation()
        else:
            self._branch_mutation(num_selection)

    def _branch_mutation(self, num_selection):
        """
        Here we select either the left or right branch, find a random selection within it,
        create a new expression, and the replace the random selection portion of the branch
        with the new expression we just created to form a mutated branch
        :param num_selection: int Determines if we are going to select the left or right branch
        :return:
        """

        branch_to_alter = self._mutated_expression.left_branch \
            if num_selection < 7 else self._mutated_expression.right_branch

        self._find_valid_points.set_expression(branch_to_alter)

        genome_selection = self._find_valid_points.get_points()
        mutated_size = genome_selection[1] - genome_selection[0] if genome_selection[1] - genome_selection[0] > 0 else 1

        mutated_section = ExpressionBranch(mutated_size)
        first_part = branch_to_alter[:genome_selection[0]]
        second_part = branch_to_alter[genome_selection[1] + 1:]
        altered_branch = first_part + mutated_section.get_branch() + second_part

        if num_selection < 7:
            self._mutated_expression.left_branch = altered_branch
        else:
            self._mutated_expression.right_branch = altered_branch

    def _root_operator_mutation(self):
        """
        Alters the root operator of the expression. Determines what the operator currently
        is and makes sure the new operator is different.
        :return:
        """

        current_root = self._mutated_expression.root_operator

        something_new = False
        while not something_new:

            operand = self._mutated_expression.expression.operator.generate_operator()

            if operand != current_root:
                self._mutated_expression.root_operator = operand
                something_new = True
