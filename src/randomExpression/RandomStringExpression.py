from src.randomExpression.ExpressionBranch import ExpressionBranch


class RandomStringExpression:
    """
    This class creates an expression into the desired format.
    The format is of a left branch, root operator, and right branch.
    This creates an equation that looks like:

        ( expression ) operator ( expression )
    """

    def __init__(self, size=None, child_expression=None):
        """
        :param size: If we supply a size as int, it will generate an expression within the size constraint
        :param child_expression: If we supply a child, no need to generate anything, we simple assign
        """
        self.expression = ExpressionBranch(size)

        if size is not None:
            self.left_branch = self.expression.create_branch()
            self.right_branch = self.expression.create_branch()
            self.root_operator = self.expression.operator.generate_operator()
        elif child_expression is not None:
            self.left_branch = child_expression[0]
            self.root_operator = child_expression[1]
            self.right_branch = child_expression[2]

            if not self.is_valid_expression():
                raise Exception("You did not supply a valid expression")

    def __str__(self):
        """
        :return: String The current equation formatted in the correct form
        """
        return "Random Expression: " + self.get_random_expression()

    def get_random_expression(self):
        """
        Formats the equation into the desired ( expression ) operator ( expression ) form
        """
        return "(" + str(self.left_branch) + ")" \
               + str(self.root_operator) + "(" + str(self.right_branch) + ")"

    def is_valid_expression(self):
        """
        Determines if our equation is valid
        :return: Boolean Whether all parts of the expression pass validation
        """
        return self.expression.is_valid_branch(self.left_branch) \
               and self.expression.operator.valid_operator(self.root_operator) \
               and self.expression.is_valid_branch(self.right_branch)

if __name__ == '__main__':
    rand_str_exp = RandomStringExpression(size=10)
    print(rand_str_exp)
    print(rand_str_exp.is_valid_expression())

    child = ["x+5+2-x", "/", "x/4-2"]
    rand_str_exp2 = RandomStringExpression(child_expression=child)
    print(rand_str_exp2)
    print(rand_str_exp2.is_valid_expression())
    print(type(rand_str_exp.left_branch))
