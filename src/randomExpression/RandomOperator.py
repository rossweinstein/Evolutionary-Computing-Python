from random import randint


class RandomOperator:
    """
       This class handles operators for an expression.  It is able
       to create a random operator and check if a value is deemed a
       valid operator.
       """

    def __init__(self):
        self.operator = ""
        self._possible_operators = ["+", "-", "*", "/"]

    def __str__(self):
        """
        :return: String representation of the most recent created operator
        """
        return "Operator: " + self.operator

    def generate_operator(self):
        """
        Randomly generates a '+', '-', '*', or '/' as a String
        :return: String a newly created operator
        """
        self.operator = self._possible_operators[randint(0, 3)]
        return self.operator

    def valid_operator(self, the_operator):
        """
        Checks whether a String is a valid operator or not
        :param the_operator: The String to validate
        :return: Boolean if the supplied String is a operator or not
        """
        if type(the_operator) is str and len(the_operator) == 1:
            return the_operator == "+" or the_operator == "-" or the_operator == "/" or the_operator == "*"
        else:
            return False

if __name__ == '__main__':
    operator = RandomOperator()
    print(operator.generate_operator())
    print(operator.valid_operator("+"))
    print(operator.valid_operator("-"))
    print(operator.valid_operator("*"))
    print(operator.valid_operator("/"))
    print(operator.valid_operator("32"))