from random import randint

from src.randomExpression.RandomOperand import RandomOperand
from src.randomExpression.RandomOperator import RandomOperator


class ExpressionBranch:

    def __init__(self, size):
        """
        This class create a random expression of a given length.  The operands
        will only be 0-9 or x and the operators will only be '+', '-', '/', '*'.
        :param size: Determines how long the expression can be
        """

        self._branch_expression = ""
        self._branch_length = 1 if size is None else size
        self.operator = RandomOperator()
        self.operand = RandomOperand(9)
        self.create_branch()

    def __str__(self):
        """
        :return: String the most recent constructed expression with a title
        """
        return "Expression: " + self._branch_expression

    def get_branch(self):
        """
        :return: String The most recent constructed expression
        """
        return self._branch_expression

    def create_branch(self):
        """
        Creates a new math expression within the provided length.
        The expression can contain operands 0-9 and operators +, -, *, /
        :return: A random mathematical expression
        """
        constructed_expression = ""

        for i in range(self._ensure_odd_length()):

            if i % 2 == 0:
                constructed_expression += self.operand.generate_operand()
            else:
                constructed_expression += self.operator.generate_operator()

        self._branch_expression = constructed_expression
        return self._branch_expression

    def _ensure_odd_length(self):
        """
        An equation must have an odd length (i.e. 1 + 2). If we
        end up with an even number, we will have an invalid equation
        so this ensures that our equation will be of the correct length.
        1 is added to handle if the random number selected is 0
        :return: An odd number within a given range
        """
        eq_length = randint(0, self._branch_length - 1)
        return eq_length + 1 if eq_length % 2 == 0 else eq_length

    def is_valid_branch(self, branch):
        """
        Loops through the supplied equation and determines if the equation
        is of an odd length and alternates operands and operators.
        :return: Whether the entire equation is valid or not
        """
        if len(branch) % 2 == 0:
            return False

        for i in range(len(branch)):

            if i % 2 == 0:
                if not self.operand.valid_operand(branch[i]):
                    return False
            else:
                if not self.operator.valid_operator(branch[i]):
                    return False
        return True

if __name__ == '__main__':
    exp = ExpressionBranch(10)
    print(exp)
    print(exp.is_valid_branch(exp.get_branch()))

